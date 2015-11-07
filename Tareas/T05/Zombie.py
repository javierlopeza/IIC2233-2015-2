from PyQt4 import QtGui
from PyQt4 import QtCore
from random import randint, uniform
from time import sleep
from SSClass import SSZombie
from vector_unitario import vector_unitario


class MoveZombieEvent:
    def __init__(self, image, x, y, nuevo_pixmap):
        self.nuevo = nuevo_pixmap
        self.image = image
        self.x = x
        self.y = y


class Zombie(QtCore.QThread):
    trigger_moveZombie = QtCore.pyqtSignal(MoveZombieEvent)

    def __init__(self, parent, x, y, name):
        super().__init__()
        self.name = name
        self.SSZombie = SSZombie()

        # Set de la imagen inicial del Zombie
        self.parent = parent
        self.image = QtGui.QLabel(parent)
        self.image.setPixmap(QtGui.QPixmap('assets/movs_zombie/pie_neutro42T.png'))
        self.image.show()
        self.image.setVisible(True)
        self.trigger_moveZombie.connect(parent.moveZombie)
        self.__position = (parent.x0, parent.y0)
        self.position = (x, y)

        # Atributo del vector unitario que apunta en direccion de la vista del zombie.
        self.vector_vista = [0, 1]

        # Factor para variar la velocidad del zombie.
        self.velocidad = randint(10, 20)

        # Factor para variar el damage que provoca el zombie
        self.damage = randint(1, 3)

        self.jugando = True

    def rotar(self, angulo):
        # Rota el QPixmap de ZombieLabel en angulo grados sentido horario.
        nuevo_pixmap = self.SSZombie.en_uso
        self.image.setPixmap(nuevo_pixmap.transformed(QtGui.QTransform().rotate(angulo)))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        nuevo_pixmap = self.SSZombie.actualizar_ss
        self.trigger_moveZombie.emit(MoveZombieEvent(self.image,
                                                     self.position[0],
                                                     self.position[1],
                                                     nuevo_pixmap))

    def actualizar_vector_vista(self):
        militar_x = self.parent.MilitarLabel.x() - self.image.x() + 10
        militar_y = self.parent.MilitarLabel.y() - self.image.y() + 130
        self.vector_vista = vector_unitario([0, 0], [militar_x, -militar_y])

    def run(self):
        while self.jugando:
            # Avanza en direccion hacia el militar.
            sleep(1 / self.velocidad)
            dx = self.vector_vista[0]
            dy = self.vector_vista[1]
            x = self.image.x()
            y = self.image.y()
            new_x = x + 2 * dx
            new_y = y - 2 * dy

            # Se verifica que en la proxima posicion no se encuentre otro zombie o el militar.
            zombie_x = new_x - 10
            zombie_y = new_y - 130
            puede_avanzar = True
            toca_militar = False
            for obj in self.parent.pos_dict:
                if obj != self.name:
                    pos_ocupada = self.parent.pos_dict[obj]
                    pos_ocup_x = pos_ocupada[0]
                    pos_ocup_y = pos_ocupada[1]
                    if (- 6 < pos_ocup_x - zombie_x < 6) and (-6 < pos_ocup_y - zombie_y < 6):
                        puede_avanzar = False
                        if obj == "militar":
                            toca_militar = True
                            break

            if puede_avanzar:  # Si no tiene obstaculos, el zombie avanza.
                self.position = (new_x, new_y)
                self.parent.pos_dict.update({self.name: (zombie_x, zombie_y)})
                self.actualizar_vector_vista()

            if toca_militar:  # Si toca al militar le provoca un damage aleatorio entre 1 y 3.
                sleep(uniform(0.4, 0.1))
                self.parent.vida_militar -= self.damage
                if self.parent.vida_militar < 0:
                    self.parent.vida_militar = 0
                self.parent.setSalud()
