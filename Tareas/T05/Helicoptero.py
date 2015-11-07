from PyQt4 import QtCore
from time import sleep
from random import choice, uniform

class DeliverBoxEvent:
    def __init__(self, contenido):
        self.contenido = contenido


class Helicoptero(QtCore.QThread):
    trigger_deliverbox = QtCore.pyqtSignal(DeliverBoxEvent)

    def __init__(self, control_juego=None):
        super().__init__()

        self.control_juego = control_juego
        self.trigger_deliverbox.connect(self.control_juego.ventana.addBox)
        self.__Box = None
        self.Box = 'nada'

    @property
    def Box(self):
        return self.__Box

    @Box.setter
    def Box(self, contenido):
        self.__Box = contenido
        self.trigger_deliverbox.emit(DeliverBoxEvent(contenido))

    def run(self):
        sleep(10)  # El helicoptero se activa a los 10 segundos de juego.
        while True:
            t_prox_box = uniform(5,15)  # Las entregas del helicoptero se hacen con una frecuencia Uniforme(10,20)
            sleep(t_prox_box)

            self.Box = choice(["vida", "balas"])

