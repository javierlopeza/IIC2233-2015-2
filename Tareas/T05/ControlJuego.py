from PyQt4 import QtCore, QtGui, uic
from gui_class import MainWindow
from ZombieDeliver import ZombieDeliver


class ControlJuego:
    def __init__(self):
        self.app = QtGui.QApplication([])
        self.ventana = MainWindow()
        self.ventana.show()

        self.zombie_deliver = ZombieDeliver(control_juego=self)

        self.zombie_deliver.deliver()

    def run(self):
        self.app.exec_()
