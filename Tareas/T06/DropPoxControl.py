from PyQt4 import QtCore, QtGui, uic
from main_window import MainWindow
from login_window import LoginWindow
import datetime


class DropPoxControl:
    def __init__(self):
        # TODO: Cargar Servidor.

        # LoginWindow
        self.app = QtGui.QApplication([])
        self.ventana = LoginWindow()
        self.ventana.show()

    def run(self):
        self.app.exec_()
