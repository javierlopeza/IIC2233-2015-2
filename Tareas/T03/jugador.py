class Jugador:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.mapa = None
        self.radar = None
        self.flota = None
        self.flota_activa = None
        self.flota_muerta = []

