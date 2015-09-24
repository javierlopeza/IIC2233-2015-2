from cargar import \
    cargar_jugadores, \
    cargar_mapas, \
    cargar_vehiculos, \
    cargar_vehiculos_a_mapa
import sys
from random import choice

from cargar_test import cargar_test


class Partida:
    def __init__(self):
        self.cargado = False
        self.jugadores = {}
        # Para testeo solamente
        cargar_test(self)
        '''
        cargar_jugadores(self)
        cargar_mapas(self)
        cargar_vehiculos(self)
        cargar_vehiculos_a_mapa(self)
        '''
        self.run()

    def run(self):
        try:
            if not self.cargado:
                raise AttributeError('El juego no se ha cargado todavia')
            turno_jugador = choice(['player1', 'player2'])

            print('\n---> Por sorteo comienza jugando Player {0}: {1} <---\n'.
                  format(self.jugadores[turno_jugador].id,
                         self.jugadores[turno_jugador].nombre))

            while not self.jugadores[turno_jugador].verificar_fracaso():
                jugador_actual = self.jugadores[turno_jugador]
                if jugador_actual.id == 1:
                    oponente = self.jugadores['player2']
                    prox_turno = 'player2'
                else:
                    oponente = self.jugadores['player1']
                    prox_turno = 'player1'

                jugador_actual.jugar(oponente)

                turno_jugador = prox_turno

            for jugador in self.jugadores.values():
                if jugador.loser == False:
                    ganador = jugador
                    break

            self.terminar_juego(ganador)

        except AttributeError as err:
            print('Error: {}'.format(err))

    def estadisticas(self):
        print('\n     === ESTADISTICAS DE LA PARTIDA ===')
        print('\n=== ESTADISTICAS PLAYER 1: {0} ==='.
              format(self.jugadores['player1'].nombre))
        self.jugadores['player1'].mostrar_estadisticas(
            self.jugadores['player2'])
        print('\n=== ESTADISTICAS PLAYER 2: {0} ==='.
              format(self.jugadores['player2'].nombre))
        self.jugadores['player2'].mostrar_estadisticas(
            self.jugadores['player1'])

    def terminar_juego(self, ganador):
        print('\n\n   === JUEGO FINALIZADO  ->  '
              'GANADOR: {} ===\n'.format(ganador.nombre))
        self.estadisticas()
        sys.exit()


p = Partida()
