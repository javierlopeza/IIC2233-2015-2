# -*- encoding: utf-8 -*-


class Calle:
    def __init__(self, direccion):
        self.direccion = direccion
        self.vehiculo_encima = None
        self.semaforo = None
        self.cruce = False
        self.continuaciones = {}

    @property
    def pos_vehiculos(self):
        theta = 0
        mirror = False
        if self.direccion == 'arriba':
            theta = -90
        elif self.direccion == 'abajo':
            theta = 90
        elif self.direccion == 'derecha':
            theta = 0
        elif self.direccion == 'izquierda':
            theta = 0
            mirror = True
        return theta, mirror

    def cambiar_semaforo(self, grilla, x, y):
        if self.semaforo == ['arriba', 'abajo']:
            self.semaforo = ['derecha', 'izquierda']
            grilla.agregar_semaforo_horizontal(x, y)
        else:
            self.semaforo = ['arriba', 'abajo']
            grilla.agregar_semaforo_vertical(x, y)

    def __repr__(self):
        return 'Calle con Direccion: {} -> Vehiculo Encima: {}'.format(self.direccion,
                                                                     self.vehiculo_encima)
