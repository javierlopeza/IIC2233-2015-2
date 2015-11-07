from PyQt4 import QtCore
from time import sleep
from random import expovariate
from math import log
from Zombie import Zombie


class CreateZombieEvent:
    def __init__(self, nombre_zombie):
        self.nombre_zombie = nombre_zombie


class ZombieDeliver(QtCore.QThread):
    trigger_createzombie = QtCore.pyqtSignal(CreateZombieEvent)

    def __init__(self, control_juego=None):
        super().__init__()

        self.control_juego = control_juego
        self.trigger_createzombie.connect(self.control_juego.ventana.addZombie)
        self.__Dzombie = None
        self.Dzombie = 'zombie 0'

    @property
    def Dzombie(self):
        return self.__Dzombie

    @Dzombie.setter
    def Dzombie(self, zombie):
        self.__Dzombie = zombie
        self.trigger_createzombie.emit(CreateZombieEvent(self.Dzombie))

    def run(self):
        sleep(1)  # Tiempo de espera para empezar a soltar Zombies nuevos.
        while True:
            lambda_exp = 1 / log(self.control_juego.tiempo_total + 1, 10)  # Funcion lambda(t)
            t_prox_zombie = expovariate(1 / lambda_exp) + 0.1
            sleep(t_prox_zombie)

            total_zombies = len(self.control_juego.ventana.lista_zombies)
            if total_zombies < 25:  # Mantiene un maximo de 25 Zombies en la ZonaJuego.
                self.control_juego.ventana.zombie_id += 1
                nombre_zombie = 'zombie {}'.format(self.control_juego.ventana.zombie_id)
                self.Dzombie = nombre_zombie
