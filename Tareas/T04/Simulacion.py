# -*- encoding: utf-8 -*-

from Ciudad import Ciudad
from random import expovariate, choice
import itertools


class Evento:
    def __init__(self, instante_ocurrencia, tipo_evento, lugar):
        self.instante_ocurrencia = instante_ocurrencia
        self.tipo_evento = tipo_evento
        self.lugar = lugar


class Simulacion:
    def __init__(self, app, rows, cols):
        self.app = app
        self.rows = rows
        self.cols = cols
        self.tiempo_maximo = 200
        self.tiempo_simulacion = 0
        self.linea_de_tiempo = []

    def cargar_linea_de_tiempo(self):
        self.linea_de_tiempo = []

        def cargar_enfermos(self):
            reloj = 0
            while reloj < self.tiempo_maximo:
                tiempo_nuevo_enfermo = expovariate(30 * 60) + reloj
                lugar = choice(list(self.ciudad.casas.keys()))
                nuevo_evento = Evento(tiempo_nuevo_enfermo, 'enfermo', lugar)
                self.linea_de_tiempo.append(nuevo_evento)
                reloj += tiempo_nuevo_enfermo

        def cargar_robos(self):
            reloj = 0
            probs_robos_lugar = self.ciudad.lista_pesos_lugares_robos
            while reloj < self.tiempo_maximo:
                tiempo_nuevo_robo = expovariate(15 * 60) + reloj
                lugar = choice(probs_robos_lugar)
                nuevo_evento = Evento(tiempo_nuevo_robo, 'robo', lugar)
                self.linea_de_tiempo.append(nuevo_evento)
                reloj += tiempo_nuevo_robo

        cargar_enfermos(self)
        cargar_robos(self)

    def run_master(self):
        for permutacion in itertools.permutations(self.ciudad.terrenos_vacios):
            pos_policia = permutacion[0]
            pos_bomberos = permutacion[1]
            pos_hospital = permutacion[2]
            self.run(pos_policia, pos_bomberos, pos_hospital)

    def run(self, pos_policia, pos_bomberos, pos_hospital):
        self.ciudad = Ciudad(self.app, self.rows, self.cols, pos_policia, pos_bomberos, pos_hospital)
        self.cargar_linea_de_tiempo()
        while self.tiempo_simulacion < self.tiempo_maximo:
            self.tiempo_simulacion += 1
            # TODO: Si el tiempo de simulacion es multiplo de 20, todos los semaforos cambian de luz.
            if self.tiempo_simulacion % 20 == 0:
                self.ciudad.cambiar_semaforos()
            # TODO: Todos los vehiculos avanzan
            self.ciudad.avanzar_vehiculos()
