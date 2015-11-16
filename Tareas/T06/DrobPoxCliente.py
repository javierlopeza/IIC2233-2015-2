from PyQt4 import QtCore, QtGui, uic
from login_window import LoginWindow
import datetime


class DrobPoxCliente:
    def __init__(self, host, port):
        self.app = QtGui.QApplication([])
        self.ventana = LoginWindow(host, port)
        self.ventana.show()

    def run(self):
        self.app.exec_()
