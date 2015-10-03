from clases.jugador import Jugador
from clases.mapa import Mapa
from cargar.cargar import cargar_vehiculos


def cargar_test(partida):
    j1 = Jugador('Javier', 1)
    j2 = Jugador('Marlo', 2)
    jugadores = {'player1': j1, 'player2': j2}
    partida.jugadores = jugadores

    for jugador in partida.jugadores.values():
        mapa = Mapa(10)
        radar = Mapa(10)
        jugador.mapa = mapa
        jugador.radar = radar

    cargar_vehiculos(partida)

    jugadores['player1'].flota_activa[0].setear_orientacion('v')
    jugadores['player1'].flota_activa[1].setear_orientacion('h')
    jugadores['player1'].flota_activa[2].setear_orientacion('v')
    jugadores['player1'].flota_activa[3].setear_orientacion('h')
    jugadores['player1'].flota_activa[4].setear_orientacion('v')
    jugadores['player1'].flota_activa[5].setear_orientacion('h')
    jugadores['player1'].flota_activa[6].setear_orientacion('v')

    jugadores['player1'].mapa.agregar_vehiculo(jugadores['player1'].flota_activa[0], '1,1')
    jugadores['player1'].mapa.agregar_vehiculo(jugadores['player1'].flota_activa[1], '8,3')
    jugadores['player1'].mapa.agregar_vehiculo(jugadores['player1'].flota_activa[2], '7,1')
    jugadores['player1'].mapa.agregar_vehiculo(jugadores['player1'].flota_activa[3], '5,6')
    jugadores['player1'].mapa.agregar_vehiculo(jugadores['player1'].flota_activa[4], '1,5')
    jugadores['player1'].mapa.agregar_vehiculo(jugadores['player1'].flota_activa[5], '5,6')
    jugadores['player1'].mapa.agregar_vehiculo(jugadores['player1'].flota_activa[6], '9,1')

    jugadores['player2'].flota_activa[0].setear_orientacion('v')
    jugadores['player2'].flota_activa[1].setear_orientacion('v')
    jugadores['player2'].flota_activa[2].setear_orientacion('h')
    jugadores['player2'].flota_activa[4].setear_orientacion('h')
    jugadores['player2'].flota_activa[6].setear_orientacion('v')
    jugadores['player2'].flota_activa[3].setear_orientacion('v')
    jugadores['player2'].flota_activa[5].setear_orientacion('v')

    jugadores['player2'].mapa.agregar_vehiculo(jugadores['player2'].flota_activa[0], '0,1')
    jugadores['player2'].mapa.agregar_vehiculo(jugadores['player2'].flota_activa[1], '0,3')
    jugadores['player2'].mapa.agregar_vehiculo(jugadores['player2'].flota_activa[2], '5,4')
    jugadores['player2'].mapa.agregar_vehiculo(jugadores['player2'].flota_activa[3], '5,0')
    jugadores['player2'].mapa.agregar_vehiculo(jugadores['player2'].flota_activa[4], '3,5')
    jugadores['player2'].mapa.agregar_vehiculo(jugadores['player2'].flota_activa[5], '9,2')
    jugadores['player2'].mapa.agregar_vehiculo(jugadores['player2'].flota_activa[6], '4,7')

    partida.cargado = True
    partida.modo_oponente = 'p'