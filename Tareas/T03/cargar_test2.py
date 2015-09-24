from jugador import Jugador
from computadora import Computadora
from mapa import Mapa
from cargar import cargar_vehiculos

def cargar_test2(partida):
    j1 = Jugador('Javier', 1)
    computadora = Computadora()
    jugadores = {'player1': j1, 'computadora': computadora}
    partida.jugadores = jugadores

    mapa = Mapa(10)
    radar = Mapa(10)
    partida.jugadores['player1'].mapa = mapa
    partida.jugadores['player1'].radar = radar

    mapa2 = Mapa(10, 'c')
    radar2 = Mapa(10, 'c')
    partida.jugadores['computadora'].mapa = mapa2
    partida.jugadores['computadora'].radar = radar2

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

    partida.cargado = True
    partida.modo_oponente = 'c'

    partida.jugadores['computadora'].posicionar_vehiculos()