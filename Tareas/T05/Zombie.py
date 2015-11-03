from PyQt4 import QtGui
from PyQt4 import QtCore
from random import randint
from time import sleep
from vector_unitario import vector_unitario


class MoveZombieEvent:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y


class Zombie(QtCore.QThread):
    trigger = QtCore.pyqtSignal(MoveZombieEvent)

    def __init__(self, parent, x, y):
        super().__init__()
        # Set de la imagen inicial del Zombie
        self.parent = parent
        self.image = QtGui.QLabel(parent)
        self.image.setPixmap(QtGui.QPixmap('assets/movs_zombie/pie_neutro42T.png'))
        self.image.show()
        self.image.setVisible(True)
        self.trigger.connect(parent.moveZombie)
        self.__position = (parent.x0, parent.y0)
        self.position = (x, y)

        # Atributo del vector unitario que apunta en direccion de la vista del zombie.
        self.vector_vista = [0, 1]

        # TODO: Factor para variar la velocidad del zombie.
        self.velocidad = randint(10, 20)

    def rotar(self, angulo):
        # Rota el QPixmap de ZombieLabel en angulo grados sentido horario.
        nuevo_pixmap = QtGui.QPixmap('assets/movs_zombie/pie_neutro42T.png')
        self.image.setPixmap(nuevo_pixmap.transformed(QtGui.QTransform().rotate(angulo)))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        self.trigger.emit(MoveZombieEvent(self.image,
                                          self.position[0],
                                          self.position[1]))

    def actualizar_vector_vista(self):
        militar_x = self.parent.MilitarLabel.x() - self.image.x() + 10
        militar_y = self.parent.MilitarLabel.y() - self.image.y() + 130
        self.vector_vista = vector_unitario([0, 0], [militar_x, -militar_y])

    def run(self):
        while True:
            # Avanza en direccion hacia el militar.
            sleep(1 / self.velocidad)
            dx = self.vector_vista[0]
            dy = self.vector_vista[1]
            x = self.image.x()
            y = self.image.y()
            new_x = x + 2 * dx
            new_y = y - 2 * dy
            self.position = (new_x, new_y)
            self.actualizar_vector_vista()

            # TODO: Verifica si toca al militar, en ese caso, le quita vida.
