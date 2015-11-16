from PyQt4 import QtGui, uic
import socket
import sys
import json
import threading
from time import sleep

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
        self.ActualizarTodoButton.clicked.connect(self.actualizar_todo)
        self.ConversarButton.clicked.connect(self.conversar_pressed)

        item = QtGui.QTreeWidgetItem(self.ArchivosTree)
        item.setText(0, "Carpeta")

        # Cargar lista de amigos.
        self.actualizar_lista_amigos()

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
        sleep(0.5)
        while self.conectado:
            data = self.socket_usuario.recv(1024)
            data_dec = data.decode('utf-8')
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

    def actualizar_todo(self):
        self.stop_escuchar()

        self.actualizar_lista_amigos()

        # TODO actualizar arbol archivos.

        self.start_escuchar()

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

    def closeEvent(self, QCloseEvent):
        self.stop_escuchar()

        data = "QUIT" + " " + self.usuario
        self.socket_usuario.send(data.encode('utf-8'))
        verificacion = self.socket_usuario.recv(1024).decode('utf-8')
        if verificacion == "QUIT":
            self.conectado = False
            self.socket_usuario.close()
