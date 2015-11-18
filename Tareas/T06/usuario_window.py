# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
import socket
import select
import sys
import os
import json
import pickle
import threading
from time import sleep
from get_tree_path import get_tree_path
from reemplazar_emojis import reemplazar_emojis

ventana = uic.loadUiType("main_gui.ui")


class UsuarioWindow(ventana[0], ventana[1]):
    def __init__(self, usuario, host, port):
        super().__init__()
        self.setupUi(self)
        self.usuario = usuario

        self.host = host
        self.port = port
        self.setup_networking()

        self.setup_base()

    def setup_base(self):
        # Set titulo ventana a DropbPox.
        self.setWindowTitle('DrobPox')
        # Set icono ventana.
        icono = QtGui.QIcon(QtGui.QPixmap('assets/dropbox_icon_green.png'))
        self.setWindowIcon(icono)
        # Set icono esquina inferior derecha.
        self.IconoLabel.setPixmap(QtGui.QPixmap('assets/dropbox_icon_green_sinfondo.png'))
        self.IconoLabel.setScaledContents(True)

        # Set usuario conectado.
        self.UsuarioConectadoLabel.setText("Usuario conectado: {}".format(self.usuario))

        self.amigo_chat = None

        self.EnviarButton.clicked.connect(self.enviar_pressed)
        self.AgregarAmigoButton.clicked.connect(self.agregar_amigo_pressed)
        self.ActualizarTodoButton.clicked.connect(self.actualizar_todo_pressed)
        self.ConversarButton.clicked.connect(self.conversar_pressed)
        self.SubirArchivoButton.clicked.connect(self.subir_archivo_pressed)
        self.SubirCarpetaButton.clicked.connect(self.subir_carpeta_pressed)
        self.BajarArchivoButton.clicked.connect(self.bajar_archivo_pressed)
        self.BajarCarpetaButton.clicked.connect(self.bajar_carpeta_pressed)

        # Cargar todos los datos del usuario.
        self.start_up()

    def setup_networking(self):
        self.socket_usuario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket_usuario.connect((self.host, self.port))
            self.start_escuchar()

        except socket.error:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       'No ha sido posible conectarse al servidor, '
                                       'vuelva a intentarlo mas tarde.',
                                       QtGui.QMessageBox.Ok)
            sys.exit()

        aceptar_user = "ACEPTAR" + " " + self.usuario
        self.socket_usuario.send(aceptar_user.encode('utf-8'))

    def start_escuchar(self):
        self.conectado = True
        self.thread_escuchador = threading.Thread(target=self.escuchar)
        self.thread_escuchador.setDaemon(True)
        self.thread_escuchador.start()

    def escuchar(self):
        sleep(0.2)
        while self.conectado:
            data = self.socket_usuario.recv(1024)
            data_dec = data.decode('utf-8', errors="ignore")
            if data_dec.startswith("STOP_ESCUCHAR"):
                self.conectado = False

            elif data_dec.startswith("NUEVO_AMIGO"):
                self.actualizar_lista_amigos()

            elif data_dec.startswith("NUEVO_MENSAJE"):
                sender = data_dec.split("S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5")[1]
                mensaje = data_dec.split("S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5")[2]
                if sender == self.amigo_chat:
                    item_nuevo_msg = QtGui.QListWidgetItem(mensaje)
                    self.ChatList.addItem(item_nuevo_msg)
                    self.ChatList.scrollToItem(item_nuevo_msg)

    def stop_escuchar(self):
        self.socket_usuario.send("STOP_ESCUCHAR".encode('utf-8'))

    def start_up(self):
        self.actualizar_lista_amigos()
        self.stop_escuchar()
        self.actualizar_arbol_archivos()
        self.start_escuchar()

    def actualizar_todo_pressed(self):
        self.CargandoLabel.setText("Cargando...")
        self.stop_escuchar()
        self.actualizar_lista_amigos()
        self.actualizar_arbol_archivos()
        self.start_escuchar()
        self.CargandoLabel.setText(" ")

    def actualizar_lista_amigos(self):
        data_solicitar = "LISTA_AMIGOS" + " " + self.usuario
        self.socket_usuario.send(data_solicitar.encode('utf-8'))
        recibido = self.socket_usuario.recv(1024).decode('utf-8')
        lista_amigos = json.loads(recibido)
        self.AmigosList.clear()
        for amigo in lista_amigos:
            item_nuevo_amigo = QtGui.QListWidgetItem(amigo)
            self.AmigosList.addItem(item_nuevo_amigo)
            self.AmigosList.scrollToItem(item_nuevo_amigo)
            self.AgregarAmigoLineEdit.clear()

    def actualizar_arbol_archivos(self):
        data_solicitar = "LISTA_ARCHIVOS" + " " + self.usuario
        sleep(1.6)  # Espera a que el servidor efectivamente haya cargado el archivo.
        self.socket_usuario.send(data_solicitar.encode('utf-8'))
        recibido = self.socket_usuario.recv(1024)
        lista_archivos = pickle.loads(recibido)
        self.ArchivosTree.clear()
        self.mostrar_archivos(lista_archivos, self.ArchivosTree)

    def mostrar_archivos(self, lista_archivos, parent):
        for (tipo, padre, nombre, contenido) in lista_archivos:
            if tipo == "file":
                new_file = QtGui.QTreeWidgetItem(parent)
                new_file.setText(0, nombre)
            elif tipo == "folder":
                new_carpeta = QtGui.QTreeWidgetItem(parent)
                new_carpeta.setText(0, nombre)
                self.mostrar_archivos(contenido, new_carpeta)

    def conversar_pressed(self):
        amigo_seleccionado = self.AmigosList.currentItem()
        if amigo_seleccionado:
            nombre_amigo = amigo_seleccionado.text()
            self.conversar(nombre_amigo)
        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "No ha seleccionado un amigo para conversar.",
                                       QtGui.QMessageBox.Ok)

    def conversar(self, amigo):

        self.ConversandoConLabel.setText("Conversando con: {}".format(amigo))
        self.amigo_chat = amigo

        self.stop_escuchar()

        data_solicitar = "HISTORIAL_CHAT" + " " + self.usuario + " " + amigo
        self.socket_usuario.send(data_solicitar.encode('utf-8'))

        recibido = self.socket_usuario.recv(1024).decode('utf-8')
        lista_historial = json.loads(recibido)
        self.ChatList.clear()
        for msg in lista_historial:
            item_nuevo_msg = QtGui.QListWidgetItem(msg)
            self.ChatList.addItem(item_nuevo_msg)
            self.ChatList.scrollToItem(item_nuevo_msg)

        self.start_escuchar()

    def solicitar_agregar_amigo(self, amigo):
        self.stop_escuchar()

        data_solicitar = "AGREGAR_AMIGO" + " " + self.usuario + " " + amigo
        self.socket_usuario.send(data_solicitar.encode('utf-8'))
        verificacion = self.socket_usuario.recv(1024).decode('utf-8')

        self.start_escuchar()

        return verificacion

    def agregar_amigo_pressed(self):
        nuevo_amigo = self.AgregarAmigoLineEdit.text()
        if nuevo_amigo.isalnum():
            respuesta_solicitud = self.solicitar_agregar_amigo(nuevo_amigo)
            if respuesta_solicitud == 'True':
                item_nuevo_amigo = QtGui.QListWidgetItem(nuevo_amigo)
                self.AmigosList.addItem(item_nuevo_amigo)
                self.AmigosList.scrollToItem(item_nuevo_amigo)
                self.AgregarAmigoLineEdit.clear()
            else:
                QtGui.QMessageBox.critical(None, 'ERROR', respuesta_solicitud, QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.critical(None, 'ERROR', "Usuario invalido.", QtGui.QMessageBox.Ok)

    def enviar_pressed(self):
        mensaje = self.ChatTextField.toPlainText().strip()
        if mensaje and self.amigo_chat:
            mensaje_final = "{0}: {1}".format(self.usuario,
                                              mensaje)

            mensaje_final = reemplazar_emojis(mensaje_final)

            item_mensaje = QtGui.QListWidgetItem(mensaje_final)
            self.ChatList.addItem(item_mensaje)
            self.ChatList.scrollToItem(item_mensaje)

            self.enviar_mensaje(mensaje_final)
            self.ChatTextField.clear()
        else:
            QtGui.QMessageBox.critical(None, 'ERROR', "No hay ningun chat activo.", QtGui.QMessageBox.Ok)

    def enviar_mensaje(self, mensaje):
        data_enviada = "MENSAJE" \
                       + "S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5" \
                       + self.usuario \
                       + "S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5" \
                       + self.amigo_chat \
                       + "S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5" \
                       + mensaje  # Inclui ese separador para evitar problemas con los espacios del mensaje.
        self.socket_usuario.send(data_enviada.encode('utf-8'))

    def subir_archivo_pressed(self):
        self.CargandoLabel.setText("Cargando...")

        # Se selecciona el path del archivo.
        path_archivo = QtGui.QFileDialog.getOpenFileName(self)

        if path_archivo:
            # Se sube el archivo.
            self.subir_archivo(path_archivo)

        self.CargandoLabel.setText(" ")

    def subir_archivo(self, path_archivo, parent="__ROOT__"):
        self.stop_escuchar()

        (filepath, filename) = os.path.split(path_archivo)

        # Se lee el archivo en bytes y se guarda la data.
        with open(path_archivo, "rb") as nuevo_archivo:
            data_archivo = nuevo_archivo.read()

        meta = "SUBIR_ARCHIVO" \
               + "SEPARADOR123456789ESPECIAL" \
               + self.usuario \
               + "SEPARADOR123456789ESPECIAL" \
               + parent \
               + "SEPARADOR123456789ESPECIAL" \
               + filename \
               + "SEPARADOR123456789ESPECIAL"

        data_enviar = meta.encode('utf-8') + data_archivo

        self.socket_usuario.send(data_enviar)
        verificacion = self.socket_usuario.recv(1024).decode('utf-8')
        if verificacion == "ARCHIVO_SUBIDO":
            self.actualizar_arbol_archivos()

        self.start_escuchar()

    def subir_carpeta_pressed(self):
        self.CargandoLabel.setText("Cargando...")

        # Se selecciona el path de la carpeta.
        path_carpeta = QtGui.QFileDialog.getExistingDirectory(self)

        if path_carpeta:
            # Se sube la carpeta.
            self.subir_carpeta(path_carpeta)

        self.CargandoLabel.setText(" ")

    def subir_carpeta(self, path_carpeta, parent="__ROOT__"):
        (folderpath, foldername) = os.path.split(path_carpeta)

        self.stop_escuchar()

        meta = "SUBIR_CARPETA" \
               + "SEPARADOR123456789ESPECIAL" \
               + self.usuario \
               + "SEPARADOR123456789ESPECIAL" \
               + parent \
               + "SEPARADOR123456789ESPECIAL" \
               + foldername

        data_enviar = meta.encode('utf-8')
        self.socket_usuario.send(data_enviar)

        verificacion = self.socket_usuario.recv(1024).decode('utf-8')
        if verificacion == "CARPETA_SUBIDA":
            self.actualizar_arbol_archivos()

        self.start_escuchar()

        new_parent = os.path.join(parent, foldername)
        for f in os.listdir(path_carpeta):
            sleep(0.8)
            if os.path.isdir(os.path.join(path_carpeta, f)):  # Si es una carpeta.
                pathcarpeta = os.path.join(path_carpeta, f)
                self.subir_carpeta(pathcarpeta, new_parent)

            elif os.path.isfile(os.path.join(path_carpeta, f)):  # Si es un archivo.
                patharchivo = os.path.join(path_carpeta, f)
                self.subir_archivo(patharchivo, new_parent)

    def bajar_archivo_pressed(self):
        archivo_seleccionado = self.ArchivosTree.currentItem()
        if archivo_seleccionado:
            nombre_archivo = archivo_seleccionado.text(0)
            ruta_hijo = get_tree_path(archivo_seleccionado)
            path_destino = QtGui.QFileDialog.getExistingDirectory(self)
            if path_destino:
                self.bajar_archivo(nombre_archivo, ruta_hijo, path_destino)
        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "No ha seleccionado un archivo para descargar.",
                                       QtGui.QMessageBox.Ok)

    def bajar_archivo(self, nombre_archivo, ruta_hijo, path_destino):
        self.stop_escuchar()

        solicitud_bajada = "BAJAR_ARCHIVO" \
                           + "SEPARADOR123456789ESPECIAL" \
                           + self.usuario \
                           + "SEPARADOR123456789ESPECIAL" \
                           + nombre_archivo \
                           + "SEPARADOR123456789ESPECIAL" \
                           + ruta_hijo

        self.socket_usuario.send(solicitud_bajada.encode('utf-8'))

        data_recibida = self.socket_usuario.recv(1024)

        if "ERROR" not in data_recibida[:6].decode('utf-8', errors="ignore"):

            with open(os.path.join(path_destino, nombre_archivo), 'wb+') as f:
                while data_recibida:
                    f.write(data_recibida)
                    ready = select.select([self.socket_usuario], [], [], 0)
                    if (ready[0]):
                        data_recibida = self.socket_usuario.recv(1024)
                    else:
                        data_recibida = b''

        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "Si desea bajar una carpeta, utilice el boton correcto.",
                                       QtGui.QMessageBox.Ok)

        self.start_escuchar()

    def bajar_carpeta_pressed(self):
        carpeta_seleccionada = self.ArchivosTree.currentItem()
        if carpeta_seleccionada:
            nombre_carpeta = carpeta_seleccionada.text(0)
            ruta_llegar = get_tree_path(carpeta_seleccionada)
            path_destino = QtGui.QFileDialog.getExistingDirectory(self)
            if path_destino:
                self.bajar_carpeta(nombre_carpeta, ruta_llegar, path_destino)
        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "No ha seleccionado una carpeta para descargar.",
                                       QtGui.QMessageBox.Ok)

    def bajar_carpeta(self, nombre_carpeta, ruta_llegar, path_destino):
        self.stop_escuchar()

        print(nombre_carpeta)
        print(ruta_llegar)
        dir_destino = os.path.join(path_destino, nombre_carpeta)
        print(dir_destino)

        if not os.path.exists(dir_destino):

            solicitud_bajada = "BAJAR_CARPETA" \
                               + "SEPARADOR123456789ESPECIAL" \
                               + self.usuario \
                               + "SEPARADOR123456789ESPECIAL" \
                               + nombre_carpeta \
                               + "SEPARADOR123456789ESPECIAL" \
                               + ruta_llegar

            self.socket_usuario.send(solicitud_bajada.encode('utf-8'))
            print("COMIENZA RECEPCION CARPETA")
            data = self.socket_usuario.recv(1024)

            if "ERROR" not in data[:6].decode('utf-8', errors="ignore"):
                data_contenido = b''
                while data:
                    print("SIGUE RECEPCION CARPETA")
                    data_contenido += data
                    ready = select.select([self.socket_usuario], [], [], 0)
                    if (ready[0]):
                        data = self.socket_usuario.recv(1024)
                    else:
                        data = b''

                print("PROCESANDO CARPETA RECIBIDA")
                with open("carpeta_{}.txt".format(nombre_carpeta), "wb+") as file_carpeta:
                    file_carpeta.write(data_contenido)

                with open("carpeta_{}.txt".format(nombre_carpeta), "rb") as file_carpeta:
                    data_carpeta = pickle.load(file_carpeta)

                os.remove("carpeta_{}.txt".format(nombre_carpeta))

                self.escribir_carpeta(data_carpeta, path_destino)

            else:
                QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "No se ha podido descargar la carpeta.",
                                       QtGui.QMessageBox.Ok)


        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "Ya existe una carpeta con el mismo nombre en el destino seleccionado.",
                                       QtGui.QMessageBox.Ok)
        self.start_escuchar()


    def escribir_archivo(self, path_destino, file_data):
            with open(path_destino, "wb+") as new_file:
                new_file.write(file_data)

    def escribir_carpeta(self, data_carpeta, path):
        # Se crea la carpeta.
        dir_nueva_carpeta = os.path.join(path, data_carpeta[2])
        if not os.path.exists(dir_nueva_carpeta):
            os.makedirs(dir_nueva_carpeta)

            for (tipo, padre, nombre, contenido) in data_carpeta[3]:
                if tipo == "file":
                    path_file = os.path.join(dir_nueva_carpeta, nombre)
                    self.escribir_archivo(path_file, contenido)

                elif tipo == "folder":
                    self.escribir_carpeta((tipo, padre, nombre, contenido), dir_nueva_carpeta)

        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "Ya existe una carpeta con el mismo nombre en el destino seleccionado.",
                                       QtGui.QMessageBox.Ok)






    def closeEvent(self, QCloseEvent):
        self.stop_escuchar()

        data = "QUIT" + " " + self.usuario
        self.socket_usuario.send(data.encode('utf-8'))
        verificacion = self.socket_usuario.recv(1024).decode('utf-8')
        if verificacion == "QUIT":
            self.conectado = False
            self.socket_usuario.close()
