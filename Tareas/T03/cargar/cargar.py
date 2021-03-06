from copy import deepcopy
from clases.jugador import Jugador
from clases.computadora import Computadora
from clases.mapa import Mapa
from clases.vehiculos import BarcoPequeno, BuqueDeGuerra, Lancha, Puerto, AvionExplorador, KamikazeIXXI, AvionCaza


def cargar_jugadores(partida):
    try:
        pc_persona = input('Desea jugar contra otra PERSONA o '
                           'contra la COMPUTADORA? [p/c]: ')

        if pc_persona != 'p' and pc_persona != 'c':
            raise TypeError('La opcion elegida no es valida')

        partida.modo_oponente = pc_persona

        if partida.modo_oponente == 'p':
            nombre1 = input('Ingrese nombre jugador 1: ')
            nombre2 = input('Ingrese nombre jugador 2: ')
            jugador1 = Jugador(nombre1, 1)
            jugador2 = Jugador(nombre2, 2)
            partida.jugadores.update({'player1': jugador1, 'player2': jugador2})

        if partida.modo_oponente == 'c':
            nombre = input('Ingrese su nombre: ')
            jugador = Jugador(nombre, 1)
            computadora = Computadora()
            partida.jugadores.update({'player1': jugador, 'computadora': computadora})

    except TypeError as err:
        print('Error: {}'.format(err))
        partida.cargar_jugadores()


def cargar_mapas(partida):
    try:
        if not partida.jugadores:
            raise AttributeError('Los jugadores no estan cargados.')

        size_mapas = input('Ingrese la dimension n que desea para los mapas (n x n): ')

        if not size_mapas.isdigit():
            raise TypeError('La dimension ingresada no es valida')

        size_mapas = int(size_mapas)

        if size_mapas == 0:
            raise ValueError('La dimension ingresada no puede ser nula')

        partida.size_mapas = size_mapas

        if partida.modo_oponente == 'p':
            for jugador in partida.jugadores.values():
                mapa_jugador = Mapa(partida.size_mapas)
                jugador.mapa = deepcopy(mapa_jugador)
                jugador.radar = deepcopy(mapa_jugador)

        elif partida.modo_oponente == 'c':
            mapa_jugador = Mapa(partida.size_mapas)
            partida.jugadores['player1'].mapa = deepcopy(mapa_jugador)
            partida.jugadores['player1'].radar = deepcopy(mapa_jugador)
            mapa_computadora = Mapa(partida.size_mapas, 'c')
            partida.jugadores['computadora'].mapa = deepcopy(mapa_computadora)
            partida.jugadores['computadora'].radar = deepcopy(mapa_computadora)

        return True

    except (TypeError, AttributeError, ValueError) as err:
        print('Error: {}'.format(err))
        partida.cargar_mapas()


def cargar_vehiculos(partida):
    try:
        if not partida.jugadores:
            raise AttributeError('Los jugadores no estan cargados.')

        for jugador in partida.jugadores.values():
            if jugador.flota:
                raise AttributeError('Un jugador ya tiene cargados '
                                     'sus vehiculos')
            vehiculos_jugador = [BarcoPequeno(), BuqueDeGuerra(),
                                 Lancha(), Puerto(), AvionExplorador(),
                                 KamikazeIXXI(), AvionCaza()]
            jugador.flota = vehiculos_jugador
            jugador.flota_activa = jugador.flota[:]

    except AttributeError as err:
        print('Error: {}'.format(err))


def cargar_vehiculos_a_mapa(self):
    try:
        if not self.jugadores:
            raise AttributeError('Los jugadores no estan cargados.')

        for jugador in self.jugadores.values():
            if jugador.nombre != 'Computadora':
                print('\nPLAYER {0}: {1}, proceda a '
                      'posicionar sus vehiculos en su mapa.'.
                      format(jugador.id, jugador.nombre))
                for vehiculo in jugador.flota:
                    vehiculo.setear_orientacion()
                    while not vehiculo.casillas_usadas:
                        jugador.mapa.agregar_vehiculo(vehiculo)

            elif jugador.nombre == 'Computadora':
                jugador.posicionar_vehiculos()

        self.cargado = True

    except AttributeError as err:
        print('Error: {}'.format(err))
