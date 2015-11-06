from PyQt4 import QtCore, QtGui, uic
from MainWindowClass import MainWindow
from ZombieDeliver import ZombieDeliver
import datetime


class ControlJuego:
    def __init__(self):
        # MainWindow
        self.app = QtGui.QApplication([])
        self.ventana = MainWindow()
        self.ventana.show()

        # Zombie Deliver Thread
        self.zombie_deliver = ZombieDeliver(control_juego=self)
        self.zombie_deliver.start()

        # Estado Juego (ACTIVO = 1 | PAUSADO = 0))
        self.estado = 1

        # Tiempo de Juego (en segundos)
        self.tiempo_inicial = datetime.datetime.now()
        a = self.tiempo_actual

    @property
    def tiempo_actual(self):
        lista_str_reloj = str(datetime.datetime.now() - self.tiempo_inicial).split(":")
        lista_int_reloj = [round(float(num)) for num in lista_str_reloj]
        lista_int_reloj.reverse()
        segundos_totales = 0
        for i in range(len(lista_int_reloj)):
            segundos_totales += (60 ** i) * lista_int_reloj[i]

        return segundos_totales

    @property
    def reloj_text(self):
        lista_str_reloj = str(datetime.datetime.now() - self.tiempo_inicial).split(":")
        lista_int_reloj = [round(float(num)) for num in lista_str_reloj]
        lista_reloj = [num for num in lista_int_reloj if num]
        reloj_text = ""
        for num in lista_reloj:
            reloj_text += str(num) + ":"
        reloj_text = reloj_text[:-1]

        return reloj_text

    def run(self):
        self.app.exec_()
