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
        # Set titulo ventana a DropbPox.
        self.setWindowTitle('DrobPox')
        # Set icono ventana.
        pixmap = QtGui.QIcon(QtGui.QPixmap('assets/dropbox_icon_green.png'))
        self.setWindowIcon(pixmap)

        # Al hacer click en Enviar se borrar el ChatTextField y se agrega el mensaje a la conversacion.
        self.EnviarButton.clicked.connect(self.enviar_pressed)

        item = QtGui.QTreeWidgetItem(self.ArchivosTree)
        item.setText(0, "Carpeta 1")

        f = QtGui.QTreeWidgetItem(item)
        f.setText(0, "Archivo 1")

    def enviar_pressed(self):
        mensaje = self.ChatTextField.toPlainText().strip()
        if mensaje:  # Si el mensaje no eran puros espacios o un string vacio
            item_mensaje = QtGui.QListWidgetItem(mensaje)
            self.ChatList.addItem(item_mensaje)
            self.ChatList.scrollToItem(item_mensaje)

        self.ChatTextField.clear()