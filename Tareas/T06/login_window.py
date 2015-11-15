from PyQt4 import QtCore, QtGui, uic
from main_window import MainWindow


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

        self.IngresarButton.clicked.connect(self.ingresar_clicked)
        self.RegistrarseButton.clicked.connect(self.registrarse_clicked)

    def ingresar_clicked(self):
        # TODO: revisar base de datos servidor.
        usuario = self.usuarioTextEdit1.text()
        clave = self.claveTextEdit1.text()

        if usuario.strip() and clave.strip():
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QtGui.QMessageBox.question(None, 'ERROR', 'Usuario y/o clave invalido.', QtGui.QMessageBox.Ok)

    def registrarse_clicked(self):
        # TODO: revisar base de datos servidor y registrar.
        usuario = self.usuarioTextEdit2.text()
        clave = self.claveTextEdit2.text()

        if usuario.strip() and clave.strip():
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QtGui.QMessageBox.question(None, 'ERROR', 'Usuario y/o clave invalido.', QtGui.QMessageBox.Ok)