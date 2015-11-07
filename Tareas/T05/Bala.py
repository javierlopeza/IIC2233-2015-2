from PyQt4 import QtGui
from PyQt4 import QtCore
from time import sleep


class MoveBalaEvent:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image


class EliminarZombieEvent:
    def __init__(self, zombie):
        self.zombie = zombie


class EliminarBalaEvent:
    def __init__(self, bala):
        self.bala = bala


class Bala(QtCore.QThread):
    trigger_moveBala = QtCore.pyqtSignal(MoveBalaEvent)
    trigger_eliminarZombie = QtCore.pyqtSignal(EliminarZombieEvent)
    trigger_eliminarBala = QtCore.pyqtSignal(EliminarBalaEvent)

    def __init__(self, parent, x, y, vector_direccion):
        super().__init__()

        # Set de la imagen inicial de la Bala
        self.parent = parent
        self.image = QtGui.QLabel(parent)
        self.image.setFixedWidth(7)
        self.image.setFixedHeight(7)
        self.image.setPixmap(QtGui.QPixmap('assets/bala/bala.png'))
        self.image.setScaledContents(True)
        self.image.show()
        self.image.setVisible(True)

        # Trigger Mover Bala
        self.trigger_moveBala.connect(parent.moveBala)
        self.__position = (parent.x0, parent.y0)
        self.position = (x, y)

        # Trigger Eliminar Zombie
        self.trigger_eliminarZombie.connect(parent.eliminarZombie)
        self.__delZ = None
        self.delZ = None

        # Trigger Eliminar Bala
        self.trigger_eliminarBala.connect(parent.eliminarBala)
        self.__delB = 0
        self.delB = 0

        # Atributo del vector unitario que apunta en direccion de movimiento de la Bala.
        self.vector_direccion = vector_direccion

        # Factor para variar la velocidad de la Bala.
        self.velocidad = 50

        # Factor para variar el alcance de las Balas.
        self.alcance = 20

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        self.trigger_moveBala.emit(MoveBalaEvent(self.position[0],
                                                 self.position[1],
                                                 self.image))

    @property
    def delZ(self):
        return self.__delZ

    @delZ.setter
    def delZ(self, zombie):
        self.__delZ = zombie
        self.trigger_eliminarZombie.emit(EliminarZombieEvent(self.delZ))

    @property
    def delB(self):
        return self.__delB

    @delB.setter
    def delB(self, bala):
        self.__delB = bala
        self.trigger_eliminarBala.emit(EliminarBalaEvent(self.delB))

    def verificar_disparo(self, new_x, new_y):
        for zombie in self.parent.lista_zombies:
            zombie_x = zombie.image.x()
            zombie_y = zombie.image.y()
            if (-30 < new_x - zombie_x < 30) and (-30 < new_y - zombie_y < 30):
                self.delZ = zombie
                self.delB = self
                return True
        return False

    def run(self):
        for i in range(self.alcance):
            sleep(1 / self.velocidad)
            dx = self.vector_direccion[0]
            dy = self.vector_direccion[1]
            x = self.image.x()
            y = self.image.y()
            new_x = x + 10 * dx
            new_y = y - 10 * dy
            if new_y <= 131 or new_x <= 10:
                break
            self.position = (new_x, new_y)
            achunto = self.verificar_disparo(new_x, new_y)
            if achunto:
                return
        self.delB = self
