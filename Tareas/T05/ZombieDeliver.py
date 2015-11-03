from time import sleep
from Zombie import Zombie
from PyQt4 import QtCore


class CreateZombieEvent:
    def __init__(self):
        pass


class ZombieDeliver(QtCore.QThread):
    trigger = QtCore.pyqtSignal(CreateZombieEvent)

    def __init__(self, control_juego=None):
        super().__init__()

        self.control_juego = control_juego
        # self.trigger.connect(self.control_juego.ventana.addZombie)

    def deliver(self):
        for i in range(10):
            nombre_zombie = 'zombie {}'.format(self.control_juego.ventana.zombie_id)
            self.control_juego.ventana.zombie_id += 1

            start_position = self.control_juego.ventana.new_zombie_start_position(nombre_zombie)
            nuevo_zombie = Zombie(parent=self.control_juego.ventana,
                                  x=start_position[0],
                                  y=start_position[1])

            self.control_juego.ventana.lista_zombies.append(nuevo_zombie)

            nuevo_zombie.start()

            self.control_juego.ventana.rotarZombies()
