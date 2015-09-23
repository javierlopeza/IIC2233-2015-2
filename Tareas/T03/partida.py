from jugador import Jugador
from mapa import Mapa


class Partida:
    def __init__(self):
        self.jugadores = {}
        self.cargar_jugadores()
        self.cargar_mapas()

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
                jugador1 = Jugador(nombre1)
                jugador2 = Jugador(nombre2)
                self.jugadores.update({'player1': jugador1, 'player2': jugador2})

            # ----------- else modo == c

        except TypeError as err:
            print('Error: {}'.format(err))
            self.cargar_jugadores()

    def cargar_mapas(self):
        try:
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


p = Partida()