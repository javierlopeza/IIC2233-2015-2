# -*- encoding: utf-8 -*-
from random import randint, uniform


class Casa:
    def __init__(self, material, duracion_robo):
        self.material = material
        self.duracion_robo = randint(duracion_robo[0], duracion_robo[1])
        if material == 'madera':
            self.rango_demorar_apagar_incendio = [30, 120]
        elif material == 'ladrillos':
            self.rango_demorar_apagar_incendio = [40, 100]
        elif material == 'hormigon':
            self.rango_demorar_apagar_incendio = [60, 80]
        elif material == 'metal':
            self.rango_demorar_apagar_incendio = [30, 40]
        self.peso_distancia_comisaria = None

    @property
    def demora_apagar_incendio(self):
        a = self.rango_demorar_apagar_incendio[0]*60
        b = self.rango_demorar_apagar_incendio[1]*60
        return uniform(a, b)

    def __repr__(self):
        return 'Casa de {}'.format(self.material)
