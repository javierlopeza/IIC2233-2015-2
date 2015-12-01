# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic
import dropbox
import dropbox.files
import threading
import os

ventana = uic.loadUiType("main.ui")


class MainWindow(ventana[0], ventana[1]):
    def __init__(self, dbx):
        super().__init__()
        self.setupUi(self)
        self.dbx = dbx

        # Se actualiza arbol de archivos.
        self.crear_thread(self.update_files_tree, (self.ArbolArchivos,), "thread_actualizar_arbol")

        # Mostrar historial button
        self.VerHistorialButton.clicked.connect(self.mostrar_historial)

        # Actualizar Button
        self.ActualizarButton.clicked.connect(self.actualizar_pressed)

        # Descargar Button y Thread Descargas
        self.DescargarArchivoButton.clicked.connect(self.descargar_pressed)
        self.thread_descarga_archivo = threading.Thread()

        # Subir Button y Thread Subidas
        self.SubirArchivoButton.clicked.connect(self.subir_pressed)
        self.thread_subir_archivo = threading.Thread()

        # Crear carpeta button y thread
        self.CrearCarpetaButton.clicked.connect(self.crear_carpeta_pressed)
        self.thread_crear_carpeta = threading.Thread()

        # Descargar carpeta button
        self.DescargarCarpetaButton.clicked.connect(self.descargar_carpeta_pressed)

    def crear_thread(self, funcion, argumentos, nombre):
        t = threading.Thread(name=nombre, target=funcion, args=argumentos)
        t.setDaemon(True)
        t.start()
        setattr(self, nombre, t)

    def update_files_tree(self, parent, folder=''):
        for entry in self.dbx.files_list_folder(folder).entries:
            # print(entry.name)
            if isinstance(entry, dropbox.files.FolderMetadata):
                new_carpeta = QtGui.QTreeWidgetItem(parent)
                new_carpeta.setText(0, entry.name)
                self.update_files_tree(new_carpeta, entry.path_lower)
            else:
                new_file = QtGui.QTreeWidgetItem(parent)
                new_file.setText(0, entry.name)

    def mostrar_historial(self):
        archivo_seleccionado = self.ArbolArchivos.currentItem()
        item = archivo_seleccionado
        if archivo_seleccionado:

            path = []
            while item is not None:
                path.append(str(item.text(0)))
                item = item.parent()
            path = '/' + '/'.join(reversed(path))

            try:
                revisiones = self.dbx.files_list_revisions(path, limit=99)
                num_rows = self.HistorialTable.rowCount()

                # Se limpia la HistorialTable.
                for r in range(num_rows):
                    self.HistorialTable.removeRow(0)

                # Se muestra el nombre archivo del que se obtuvo el historial.
                self.HistorialLabel.setText("Historial de Modificaciones del Archivo: {}".
                                            format(archivo_seleccionado.text(0)))

                # Se agregan las revisiones obtenidas a la HistorialTable.
                for rev in revisiones.entries:
                    n_row = self.HistorialTable.rowCount()
                    self.HistorialTable.insertRow(n_row)
                    self.HistorialTable.setVerticalHeaderItem(n_row, QtGui.QTableWidgetItem(rev.name))
                    fecha = "-".join(reversed(str(rev.client_modified).split(" ")[0].split("-")))
                    hora = str(rev.client_modified).split(" ")[1]
                    size = rev.size
                    self.HistorialTable.setItem(n_row, 0, QtGui.QTableWidgetItem(str(fecha)))
                    self.HistorialTable.setItem(n_row, 1, QtGui.QTableWidgetItem(str(hora)))
                    self.HistorialTable.setItem(n_row, 2, QtGui.QTableWidgetItem(str(size)))

            except:
                QtGui.QMessageBox.critical(None, 'ERROR', "Debe seleccionar un archivo.", QtGui.QMessageBox.Ok)

        else:
            QtGui.QMessageBox.critical(None, 'ERROR', "Debe seleccionar un archivo.", QtGui.QMessageBox.Ok)

    def actualizar_pressed(self):
        if not self.thread_actualizar_arbol.isAlive():
            self.ArbolArchivos.clear()
            self.crear_thread(self.update_files_tree, (self.ArbolArchivos,), "thread_actualizar_arbol")

    def descargar_pressed(self):
        if not self.thread_descarga_archivo.isAlive():
            archivo_seleccionado = self.ArbolArchivos.currentItem()
            if archivo_seleccionado:
                nombre_archivo = archivo_seleccionado.text(0)

                if nombre_archivo.count(".") > 0:
                    item = archivo_seleccionado

                    path = []
                    while item is not None:
                        path.append(str(item.text(0)))
                        item = item.parent()
                    path_archivo = '/' + '/'.join(reversed(path))

                    path_destino_descarga = QtGui.QFileDialog.getExistingDirectory(self)
                    if path_destino_descarga:
                        path_destino_descarga = os.path.join(path_destino_descarga, nombre_archivo)
                        self.crear_thread(self.descargar_archivo,
                                          (path_destino_descarga, path_archivo),
                                          "thread_descarga_archivo")

                else:
                    QtGui.QMessageBox.critical(None, 'ERROR', "Debe seleccionar un archivo.",
                                               QtGui.QMessageBox.Ok)
            else:
                QtGui.QMessageBox.critical(None, 'ERROR', "Debe seleccionar un archivo.",
                                           QtGui.QMessageBox.Ok)

        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "Actualmente se esta descargando "
                                       "un archivo, por favor espere.",
                                       QtGui.QMessageBox.Ok)

    def descargar_archivo(self, path_destino_descarga, path_archivo):
        try:
            self.dbx.files_download_to_file(path_destino_descarga, path_archivo, rev=None)
        except:
            pass

    def descargar_carpeta_pressed(self):
        if not self.thread_descarga_archivo.isAlive():
            carpeta_seleccionada = self.ArbolArchivos.currentItem()
            if carpeta_seleccionada:
                nombre_carpeta = carpeta_seleccionada.text(0)

                if nombre_carpeta.count(".") == 0 or nombre_carpeta.count(".") > 1:
                    item = carpeta_seleccionada

                    path = []
                    while item is not None:
                        path.append(str(item.text(0)))
                        item = item.parent()
                    path_carpeta = '/' + '/'.join(reversed(path))

                    path_destino_descarga = QtGui.QFileDialog.getExistingDirectory(self)
                    if path_destino_descarga:
                        path_destino_descarga = os.path.join(path_destino_descarga, nombre_carpeta)
                        self.crear_thread(self.descargar_carpeta,
                                          (path_destino_descarga, path_carpeta),
                                          "thread_descarga_archivo")

                else:
                    QtGui.QMessageBox.critical(None, 'ERROR', "Debe seleccionar una carpeta.",
                                               QtGui.QMessageBox.Ok)
            else:
                QtGui.QMessageBox.critical(None, 'ERROR', "Debe seleccionar una carpeta.",
                                           QtGui.QMessageBox.Ok)

        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "Actualmente se esta descargando "
                                       "un archivo, por favor espere.",
                                       QtGui.QMessageBox.Ok)

    def descargar_carpeta(self, path_destino_descarga, path_carpeta):
        nombre_carpeta = os.path.split(path_carpeta)[1]
        dir_carpeta = os.path.join(path_destino_descarga, nombre_carpeta)
        if not os.path.exists(dir_carpeta):
            os.makedirs(dir_carpeta)

    def subir_pressed(self):
        if not self.thread_subir_archivo.isAlive():
            dir_seleccionado = self.ArbolArchivos.currentItem()
            if dir_seleccionado:
                item = dir_seleccionado

                path = []
                while item is not None:
                    path.append(str(item.text(0)))
                    item = item.parent()
                path.reverse()
                path = path[:-1]
                path_dir = '/' + '/'.join(path)


                path_origen_subida = QtGui.QFileDialog.getOpenFileName(self)
                if path_origen_subida:
                    nombre_archivo = os.path.split(path_origen_subida)[1]
                    path_subida = path_dir + '/' + nombre_archivo
                    path_subida = path_subida.replace("//", "/")
                    self.crear_thread(self.subir_archivo,
                                      (path_origen_subida, path_subida),
                                      "thread_subir_archivo")

            else:
                QtGui.QMessageBox.critical(None, 'ERROR', "Debe seleccionar un directorio.",
                                           QtGui.QMessageBox.Ok)

        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "Actualmente esta subiendo un archivo, por favor espere.",
                                       QtGui.QMessageBox.Ok)

    def subir_archivo(self, path_origen_subida, path_subida):
        try:
            with open(path_origen_subida, 'rb') as archivo:
                self.dbx.files_upload(archivo, path_subida)
            self.actualizar_pressed()
        except:
            pass

    def crear_carpeta_pressed(self):
        if not self.thread_crear_carpeta.isAlive():
            ubicacion_seleccionada = self.ArbolArchivos.currentItem()
            if ubicacion_seleccionada:
                nombre_carpeta = self.NombreCarpetaLineEdit.text()

                if nombre_carpeta:
                    item = ubicacion_seleccionada

                    path = []
                    while item is not None:
                        path.append(str(item.text(0)))
                        item = item.parent()
                    path.reverse()
                    path = path[:-1]
                    path_creacion = '/' + '/'.join(path) + '/' + nombre_carpeta
                    path_creacion = path_creacion.replace("//", "/")

                    self.crear_thread(self.crear_carpeta,
                                      (path_creacion,),
                                      "thread_crear_carpeta")

                else:
                    QtGui.QMessageBox.critical(None, 'ERROR', "Debe ingresar un nombre para la carpeta nueva.",
                                               QtGui.QMessageBox.Ok)

            else:
                QtGui.QMessageBox.critical(None, 'ERROR', "Debe seleccionar una ubicacion de creacion.",
                                           QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       "Actualmente se esta creando una carpeta, por favor espere.",
                                       QtGui.QMessageBox.Ok)

    def crear_carpeta(self, path_creacion):
        try:
            self.dbx.files_create_folder(path_creacion)
        except:
            pass
