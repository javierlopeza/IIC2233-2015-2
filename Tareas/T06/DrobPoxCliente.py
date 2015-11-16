from PyQt4 import QtGui
from login_window import LoginWindow


class DrobPoxCliente:
    def __init__(self, host, port):
        self.app = QtGui.QApplication([])
        self.ventana = LoginWindow(host, port)
        self.ventana.show()

    def run(self):
        self.app.exec_()
