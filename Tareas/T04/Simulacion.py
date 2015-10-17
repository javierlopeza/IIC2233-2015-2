# -*- encoding: utf-8 -*-

from Ciudad import Ciudad


class Simulacion:
    def __init__(self, app):
        self.ciudad = Ciudad(app)
        self.tiempo_maximo = 50
        self.tiempo_simulacion = 0

    def run(self):
        while self.tiempo_simulacion < self.tiempo_maximo:
            