from PyQt4 import QtCore, QtGui, uic
from random import randint, choice
from time import sleep
import sys

ventana = uic.loadUiType("gui.ui")

class MainWindow(ventana[0], ventana[1]):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setup_base()

    def setup_base(self):
        # Set titulo ventana a Age of Zombies
        self.setWindowTitle('DropPox')
        # Set icono ventana.
        pixmap = QtGui.QIcon(QtGui.QPixmap('assets/dropbox_icon_green.png'))
        self.setWindowIcon(pixmap)

        item = QtGui.QTreeWidgetItem(self.ArchivosTree)
        item.setText(0, "Hola123")

        n = QtGui.QTreeWidgetItem(item)
        n.setText(0, "Alo")