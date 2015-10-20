# -*- encoding: utf-8 -*-

from Ciudad import Ciudad
from random import expovariate, choice, randint
import itertools


class Evento:
    def __init__(self, instante_ocurrencia, tipo_evento, lugar):
        self.instante_ocurrencia = instante_ocurrencia
        self.tipo = tipo_evento
        self.lugar = lugar

    def __repr__(self):
        return 'EVENTO: {} | INSTANTE: {} | LUGAR: {}'.format(self.tipo, self.instante_ocurrencia, self.lugar)


class Simulacion:
    def __init__(self, app, rows, cols):
        self.ciudad = None
        self.app = app
        self.rows = rows
        self.cols = cols
        self.tiempo_maximo = 24 * 60 * 60
        self.tiempo_simulacion = 0
        self.linea_de_tiempo = []
        self.terrenos_vacios = []
        print('[SIMULACION] Se simulara durante un periodo de {} segundos.'.format(self.tiempo_maximo))

    def cargar_terrenos_vacios(self):
        mapa_file = open('mapa fix.txt', 'r')
        lineas = mapa_file.readlines()
        for l in range(1, len(lineas)):
            x = int(lineas[l].split(' ')[0].split(',')[0])
            y = int(lineas[l].split(' ')[0].split(',')[1])
            entidad = lineas[l].split(' ')[1]
            if entidad.lower() == 'vacio\n':
                self.terrenos_vacios.append('{},{}'.format(x + 1, y + 1))

    def cargar_linea_de_tiempo(self):
        self.linea_de_tiempo = []

        def cargar_enfermos(self):
            reloj = 0
            while reloj < self.tiempo_maximo:
                tiempo_nuevo_enfermo = round(expovariate(1 / (2 * 60 * 60)) + reloj)
                if tiempo_nuevo_enfermo <= self.tiempo_maximo:
                    lugar = choice(list(self.ciudad.casas.keys()))
                    nuevo_evento = Evento(tiempo_nuevo_enfermo, 'enfermo', lugar)
                    self.linea_de_tiempo.append(nuevo_evento)
                reloj += tiempo_nuevo_enfermo

        def cargar_robos(self):
            reloj = 0
            probs_robos_lugar = self.ciudad.lista_pesos_lugares_robos
            while reloj < self.tiempo_maximo:
                tiempo_nuevo_robo = round(expovariate(1 / (4 * 60 * 60)) + reloj)
                if tiempo_nuevo_robo <= self.tiempo_maximo:
                    lugar = choice(probs_robos_lugar)
                    nuevo_evento = Evento(tiempo_nuevo_robo, 'robo', lugar)
                    self.linea_de_tiempo.append(nuevo_evento)
                reloj += tiempo_nuevo_robo

        def cargar_incendios(self):
            reloj = 0
            probs_incendios_lugar = self.ciudad.lista_pesos_lugares_incendios
            while reloj < self.tiempo_maximo:
                tiempo_nuevo_incendio = round(expovariate(1 / (10 * 60 * 60)) + reloj)
                if tiempo_nuevo_incendio <= self.tiempo_maximo:
                    lugar = choice(probs_incendios_lugar)
                    nuevo_evento = Evento(tiempo_nuevo_incendio, 'incendio', lugar)
                    self.linea_de_tiempo.append(nuevo_evento)
                reloj += tiempo_nuevo_incendio

        def ordenar_linea_de_tiempo(self):
            self.linea_de_tiempo.sort(key=lambda x: x.instante_ocurrencia)

        cargar_enfermos(self)
        cargar_robos(self)
        cargar_incendios(self)

        ordenar_linea_de_tiempo(self)

        print('[SIMULACION] Los eventos que ocurriran en el periodo son: ')
        for evento in self.linea_de_tiempo:
            print('\t{}'.format(evento))

    def run_master(self):
        self.cargar_terrenos_vacios()
        for permutacion in itertools.permutations(self.terrenos_vacios):
            pos_policia = permutacion[0]
            pos_bomberos = permutacion[1]
            pos_hospital = permutacion[2]
            self.run(pos_policia, pos_bomberos, pos_hospital)

    def run(self, pos_policia, pos_bomberos, pos_hospital):
        self.ciudad = Ciudad(self.app, self.rows, self.cols, pos_policia, pos_bomberos, pos_hospital)
        self.cargar_linea_de_tiempo()
        self.tiempo_simulacion = 0
        while self.tiempo_simulacion < self.tiempo_maximo:
            # Si es que quedan eventos:
            if self.linea_de_tiempo:
                siguiente_evento = self.linea_de_tiempo.pop(0)

                # Se revisa si cada taxi recoge un pasajero en este tiempo antes del siguiente evento.
                taxis_utiles_vacios = [taxi for taxi in self.ciudad.taxis.values()
                                         if taxi.instante_nuevo_pasajero <= siguiente_evento.instante_ocurrencia
                                       and not taxi.pasajero]
                while taxis_utiles_vacios:
                    taxis_utiles_vacios.sort(key=lambda x: x.instante_nuevo_pasajero)
                    taxi = taxis_utiles_vacios[0]

                    # Los vehiculos avanzan hasta que el taxi encuentra el pasajero.
                    delta_mini = round(taxi.instante_nuevo_pasajero - self.tiempo_simulacion)
                    self.ciudad.avanzar_vehiculos_periodo(delta_mini)

                    # El taxi toma al pasajero
                    taxi.recoger_pasajero(self.ciudad.calles)
                    self.tiempo_simulacion = taxi.instante_nuevo_pasajero
                    print('[SIMULACION] Un taxi recoge un pasajero en el '
                          'instante {} con destino a {}'.format(round(self.tiempo_simulacion,2),
                                                                taxi.destino))

                    taxis_utiles_vacios = [taxi for taxi in self.ciudad.taxis.values()
                                             if taxi.instante_nuevo_pasajero <= siguiente_evento.instante_ocurrencia
                                           and not taxi.pasajero]

                # Los vehiculos avanzan durante un periodo de tiempo igual a delta_tiempo antes del siguiente evento.
                delta_tiempo = round(siguiente_evento.instante_ocurrencia - self.tiempo_simulacion)
                print('[SIMULACION] Moviendo vehiculos comunes por {} segundos...'.format(delta_tiempo))
                self.ciudad.avanzar_vehiculos_periodo(delta_tiempo)

                # Ocurre el siguiente evento.
                self.tiempo_simulacion = siguiente_evento.instante_ocurrencia
                if siguiente_evento.tipo == 'enfermo':
                    # TODO: sale ambulancia al lugar del enfermo y vuelve al hospital.
                    print('EVENTO ENFERMO')
                elif siguiente_evento.tipo == 'robo':
                    # TODO: sale una patrulla al lugar del robo y vuelve a la comisaria.
                    print('EVENTO ROBO')
                elif siguiente_evento.tipo == 'incendio':
                    # TODO: sale un carro de bomberos al lugar del incendio, apaga el incendio y vuelve al cuartel.
                    print('EVENTO INCENDIO')

            # Si no quedan eventos:
            else:
                delta_tiempo_final = self.tiempo_maximo - self.tiempo_simulacion
                self.ciudad.avanzar_vehiculos_periodo(delta_tiempo_final)

                self.tiempo_simulacion = self.tiempo_maximo
