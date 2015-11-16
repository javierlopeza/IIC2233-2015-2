from PyQt4 import QtCore, QtGui, uic
import socket
from random import randint, choice
from time import sleep
import sys

ventana = uic.loadUiType("main_gui.ui")


class UsuarioWindow(ventana[0], ventana[1]):
    def __init__(self, usuario, host, port):
        super().__init__()
        self.setupUi(self)

        self.usuario = usuario
        self.setup_base()

        self.host = host
        self.port = port
        self.setup_networking()

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

        self.EnviarButton.clicked.connect(self.enviar_pressed)
        self.AgregarAmigoButton.clicked.connect(self.agregar_amigo_pressed)

        item = QtGui.QTreeWidgetItem(self.ArchivosTree)
        item.setText(0, "Carpeta 1")

        f = QtGui.QTreeWidgetItem(item)
        f.setText(0, "Archivo 1")

    def setup_networking(self):
        self.socket_usuario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_usuario.connect((self.host, self.port))

    def solicitar_agregar_amigo(self, amigo):
        data_solicitar = "AGREGAR_AMIGO" + " " + self.usuario + " " + amigo
        self.socket_usuario.send(data_solicitar.encode('utf-8'))
        verificacion = self.socket_usuario.recv(1024).decode('utf-8')
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
        if mensaje:
            mensaje_final = "{0}: {1}".format(self.usuario,
                                              mensaje)
            item_mensaje = QtGui.QListWidgetItem(mensaje_final)
            self.ChatList.addItem(item_mensaje)
            self.ChatList.scrollToItem(item_mensaje)
        self.ChatTextField.clear()

    def closeEvent(self, QCloseEvent):
        data = "QUIT"
        self.socket_usuario.send(data.encode('utf-8'))
        verificacion = self.socket_usuario.recv(1024).decode('utf-8')
        if verificacion == "QUIT":
            self.socket_usuario.close()
