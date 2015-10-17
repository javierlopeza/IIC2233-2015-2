# -*- encoding: utf-8 -*-
from random import uniform


class VehiculoComun:
    def __init__(self):
        self.tipo = 'normal'
        self.velocidad = uniform(0.5, 1)

    def __repr__(self):
        return 'Vehículo común con velocidad {}'.format(round(self.velocidad, 2))


class Taxi(VehiculoComun):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Taxi con velocidad {}'.format(round(self.velocidad, 2))


class VehiculoEmergencia:
    def __init__(self, tipo):
        self.tipo = tipo
        self.sirena_activada = False

    def __repr__(self):
        add = ''
        if not self.sirena_activada:
            add = 'no '
        return 'Vehículo de emergencia tipo {} ' \
               'con velocidad {} y sirena {}activada'.format(self.tipo,
                                                             self.velocidad,
                                                             add)

    @property
    def velocidad(self):
        if self.sirena_activada:
            return 1
        return 0.5
