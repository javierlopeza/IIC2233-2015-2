from cargar import \
    cargar_jugadores, \
    cargar_mapas, \
    cargar_vehiculos, \
    cargar_vehiculos_a_mapa


class Partida:
    def __init__(self):
        self.jugadores = {}
        cargar_jugadores(self)
        cargar_mapas(self)
        cargar_vehiculos(self)
        cargar_vehiculos_a_mapa(self)


p = Partida()
print(p.jugadores['player1'].mapa)
print(p.jugadores['player2'].mapa)
