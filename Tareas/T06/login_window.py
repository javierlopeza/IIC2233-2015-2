from PyQt4 import QtCore, QtGui, uic
from usuario_window import UsuarioWindow
from hashear import hashear
import socket
import sys

ventana = uic.loadUiType("login_gui.ui")


class LoginWindow(ventana[0], ventana[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set titulo ventana a DropbPox.
        self.setWindowTitle('DrobPox')
        # Set icono ventana.
        pixmap = QtGui.QIcon(QtGui.QPixmap('assets/dropbox_icon_green.png'))
        self.setWindowIcon(pixmap)

        # Set socket Login.
        self.host = socket.gethostname()
        self.port = 4010
        self.socket_login = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket_login.connect((self.host, self.port))
        except socket.error:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       'No ha sido posible conectarse al servidor, '
                                       'vuelva a intentarlo mas tarde.',
                                       QtGui.QMessageBox.Ok)
            sys.exit()

        # Set connections buttons.
        self.IngresarButton.clicked.connect(self.ingresar_clicked)
        self.RegistrarseButton.clicked.connect(self.registrarse_clicked)

    def solicitar_verificacion_ingreso(self, usuario, clave):
        data_verificar = "INGRESO" + " " + usuario + " " + clave
        self.socket_login.send(data_verificar.encode('utf-8'))
        verificacion = self.socket_login.recv(1024).decode('utf-8')
        if verificacion == "True":
            return True
        else:
            return False

    def ingresar_clicked(self):
        usuario = self.usuarioTextEdit1.text()
        clave = self.claveTextEdit1.text()

        if usuario.isalnum() and clave.isalnum():
            respuesta_verificacion = self.solicitar_verificacion_ingreso(usuario, clave)
            if respuesta_verificacion:
                self.close()
                self.main_window = UsuarioWindow(usuario)
                self.main_window.show()

            else:
                QtGui.QMessageBox.critical(None, 'ERROR', 'Usuario y/o clave invalidos.', QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.critical(None, 'ERROR', 'Usuario y/o clave invalidos.', QtGui.QMessageBox.Ok)

    def solicitar_verificacion_registro(self, usuario, clave):
        data_verificar = "REGISTRO" + " " + usuario + " " + clave
        self.socket_login.send(data_verificar.encode('utf-8'))
        verificacion = self.socket_login.recv(1024).decode('utf-8')
        if verificacion == "True":
            return True
        else:
            return False

    def registrarse_clicked(self):
        usuario = self.usuarioTextEdit2.text()
        clave = self.claveTextEdit2.text()

        if usuario.isalnum() and clave.isalnum():
            respuesta_verificacion = self.solicitar_verificacion_registro(usuario, clave)
            if respuesta_verificacion:
                QtGui.QMessageBox.information(None, 'EXITO', 'Registro exitoso, se iniciara automaticamente su sesion.',
                                              QtGui.QMessageBox.Ok)
                self.close()
                self.main_window = UsuarioWindow(usuario)
                self.main_window.show()

            else:
                QtGui.QMessageBox.critical(None, 'ERROR', 'El usuario ya existe.', QtGui.QMessageBox.Ok)

        else:
            QtGui.QMessageBox.critical(None, 'ERROR', 'Usuario y/o clave invalido.', QtGui.QMessageBox.Ok)

    def closeEvent(self, QCloseEvent):
        data = "QUIT"
        self.socket_login.send(data.encode('utf-8'))
        verificacion = self.socket_login.recv(1024).decode('utf-8')
        if verificacion == "QUIT":
            self.socket_login.close()
