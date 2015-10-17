# -*- encoding: utf-8 -*-

from Ciudad import Ciudad


class Simulacion:
    def __init__(self, app):
        self.ciudad = Ciudad(app)
        self.tiempo_maximo = 50
        self.tiempo_simulacion = 0

    def run(self):
        while self.tiempo_simulacion < self.tiempo_maximo:
            self.tiempo_simulacion += 1
            # TODO: Si el tiempo de simulacion es multiplo de 20, todos los semaforos cambian de luz.
            if self.tiempo_simulacion % 20 == 0:
                self.ciudad.cambiar_semaforos()

            # TODO: Todos los vehiculos avanzan
            self.ciudad.avanzar_vehiculos()