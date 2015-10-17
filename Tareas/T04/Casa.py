# -*- encoding: utf-8 -*-
from random import randint


class Casa:
    def __init__(self, material, duracion_robo):
        self.material = material
        self.duracion_robo = randint(duracion_robo[0], duracion_robo[1])

    def __repr__(self):
        return 'Casa de {}'.format(self.material)

