from PyQt4 import QtCore, QtGui, uic
from MainWindow import MainWindow
from ZombieDeliver import ZombieDeliver
from Reloj import Reloj
from Helicoptero import Helicoptero
import datetime


class ControlJuego:
    def __init__(self):
        # MainWindow
        self.app = QtGui.QApplication([])
        self.ventana = MainWindow(control_juego=self)
        self.ventana.show()

        # Zombie Deliver Thread
        self.zombie_deliver = ZombieDeliver(control_juego=self)
        self.zombie_deliver.start()

        # Reloj Thread
        self.reloj = Reloj(control_juego=self)
        self.reloj.start()

        # Helicoptero Thread
        self.helicoptero = Helicoptero(control_juego=self)
        self.helicoptero.start()

        # Estado Juego (ACTIVO = 1 | PAUSADO = 0))
        self.estado = 1

        # Tiempo de Juego (en segundos)
        self.tiempo_inicial = datetime.datetime.now()

    @property
    def tiempo_total(self):
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
        lista_int_reloj = [round(float(num)) for num in lista_str_reloj[-2::]]
        segundos = str(lista_int_reloj[1]).zfill(2)
        minutos = str(lista_int_reloj[0]).zfill(2)
        reloj_text = "{0}:{1}".format(minutos, segundos)

        return reloj_text

    def run(self):
        self.app.exec_()
