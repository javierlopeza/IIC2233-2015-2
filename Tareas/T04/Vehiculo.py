# -*- encoding: utf-8 -*-
from random import uniform, randint, expovariate, choice


class VehiculoComun:
    def __init__(self):
        self.tipo = 'normal'
        self.velocidad = uniform(0.5, 1)

    def __repr__(self):
        return 'Vehículo común con velocidad {}'.format(round(self.velocidad, 2))


class Taxi(VehiculoComun):
    def __init__(self):
        super().__init__()
        self.instante_nuevo_pasajero = expovariate(1/40)
        self.pasajero = False
        self.destino = None
        self.tiempo_paralizado = 0

    def recoger_pasajero(self, calles):
        self.pasajero = True
        self.destino = choice(list(calles.keys()))
        self.tiempo_paralizado = randint(5, 15)


    def dejar_pasajero(self, tiempo_simulacion):
        self.pasajero = False
        self.destino = None
        self.instante_nuevo_pasajero = expovariate(1/40) + tiempo_simulacion
        self.tiempo_paralizado = randint(10,20)

    def __repr__(self):
        return 'Taxi con velocidad {}'.format(round(self.velocidad, 2))


class VehiculoEmergencia:
    def __init__(self):
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


class Ambulancia(VehiculoEmergencia):
    def __init__(self):
        super().__init__()


class CarroBomberos(VehiculoEmergencia):
    def __init__(self):
        super().__init__()

class Patrulla(VehiculoEmergencia):
    def __init__(self):
        super().__init__()

