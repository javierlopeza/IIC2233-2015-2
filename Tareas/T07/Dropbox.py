# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from LoginWindow import LoginWindow


class Dropbox:
    def __init__(self):
        self.app = QtGui.QApplication([])
        self.ventana = LoginWindow()
        self.ventana.show()

    def run(self):
        self.app.exec_()
