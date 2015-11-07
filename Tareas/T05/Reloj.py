from PyQt4 import QtCore
from time import sleep


class ChangeTimeEvent:
    def __init__(self, tiempo):
        self.tiempo = tiempo


class SumarPuntajeEvent:
    def __init__(self, dpuntaje):
        self.dpuntaje = dpuntaje


class Reloj(QtCore.QThread):
    trigger_changetime = QtCore.pyqtSignal(ChangeTimeEvent)
    trigger_sumarpuntaje = QtCore.pyqtSignal(SumarPuntajeEvent)

    def __init__(self, control_juego=None):
        super().__init__()

        self.control_juego = control_juego

        self.trigger_changetime.connect(self.control_juego.ventana.setReloj)
        self.__Treloj = None
        self.Treloj = "00:00"

        self.trigger_sumarpuntaje.connect(self.control_juego.ventana.setPuntaje)
        self.__Dpuntaje = 0
        self.Dpuntaje = 0

    @property
    def Treloj(self):
        return self.__Treloj

    @Treloj.setter
    def Treloj(self, tiempo):
        self.__Treloj = tiempo
        self.trigger_changetime.emit(ChangeTimeEvent(tiempo))

    @property
    def Dpuntaje(self):
        return self.__Dpuntaje

    @Dpuntaje.setter
    def Dpuntaje(self, dpunt):
        self.__Dpuntaje = dpunt
        self.trigger_sumarpuntaje.emit(SumarPuntajeEvent(dpunt))

    def run(self):
        sleep(1)
        while True:
            nuevo_tiempo = self.control_juego.reloj_text
            self.Treloj = nuevo_tiempo
            self.Dpuntaje = 12
            sleep(1)
