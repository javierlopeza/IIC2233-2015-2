from PyQt4 import QtCore, QtGui, uic
from main_window import MainWindow
import datetime


class DropPoxControl:
    def __init__(self):
        # MainWindow
        self.app = QtGui.QApplication([])
        self.ventana = MainWindow()
        self.ventana.show()

    def run(self):
        self.app.exec_()
