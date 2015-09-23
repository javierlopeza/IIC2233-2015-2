from random import choice
from jugador import Jugador
from mapa import Mapa
from vehiculos import BarcoPequeno, BuqueDeGuerra, Lancha, Puerto, AvionExplorador, KamikazeIXXI, AvionCaza


class Partida:
    def __init__(self):
        self.jugadores = {}
        self.cargar_jugadores()
        self.cargar_mapas()
        self.cargar_vehiculos()
        self.cargar_vehiculos_a_mapa()

    def cargar_jugadores(self):
        try:
            pc_persona = input('Desea jugar con otra PERSONA o '
                               'con la COMPUTADORA? [p/c]: ')

            if pc_persona != 'p' and pc_persona != 'c':
                raise TypeError('La opcion elegida no es valida')

            self.modo_oponente = pc_persona

            if self.modo_oponente == 'p':
                nombre1 = input('Ingrese nombre jugador 1: ')
                nombre2 = input('Ingrese nombre jugador 2: ')
                jugador1 = Jugador(nombre1, 1)
                jugador2 = Jugador(nombre2, 2)
                self.jugadores.update({'player1': jugador1, 'player2': jugador2})

                # ----------- else modo == c

        except TypeError as err:
            print('Error: {}'.format(err))
            self.cargar_jugadores()

    def cargar_mapas(self):
        try:
            if not self.jugadores:
                raise Exception('Los jugadores no estan cargados.')

            size_mapas = input('Ingrese la dimension n que desea para sus mapas (n x n): ')

            if not size_mapas.isdigit():
                raise TypeError('La dimension ingresada no es valida')

            size_mapas = int(size_mapas)

            if size_mapas == 0:
                raise Exception('La dimension ingresada no puede ser nula')

            self.size_mapas = size_mapas

            for jugador in self.jugadores.values():
                mapa_jugador = Mapa(self.size_mapas)
                jugador.mapa = mapa_jugador

            return True

        except (TypeError, Exception) as err:
            print('Error: {}'.format(err))
            self.cargar_mapas()

    def cargar_vehiculos(self):
        try:
            if not self.jugadores:
                raise Exception('Los jugadores no estan cargados.')

            for jugador in self.jugadores.values():
                if jugador.flota:
                    raise Exception('Un jugador ya tiene cargados '
                                    'sus vehiculos')
                vehiculos_jugador = [BarcoPequeno(), BuqueDeGuerra(),
                                     Lancha(), Puerto(), AvionExplorador(),
                                     KamikazeIXXI(), AvionCaza()]
                jugador.flota = vehiculos_jugador
                jugador.flota_activa = jugador.flota[:]

        except Exception as err:
            print('Error: {}'.format(err))

    def cargar_vehiculos_a_mapa(self):
        for jugador in self.jugadores.values():
            print('\nPLAYER {0}: {1}, proceda a '
                  'posicionar sus vehiculos en su mapa.'.format(
                jugador.id,
                jugador.nombre
            ))
            for vehiculo in jugador.flota:
                vehiculo.setear_orientacion()
                while not vehiculo.casillas_usadas:
                    jugador.mapa.agregar_vehiculo(vehiculo)

p = Partida()
print(p.jugadores['player1'].mapa)
print(p.jugadores['player2'].mapa)
