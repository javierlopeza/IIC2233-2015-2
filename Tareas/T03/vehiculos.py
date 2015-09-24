from vehiculo import Vehiculo
from ataques import \
    Trident, \
    Tomahawk, \
    Napalm, \
    Minuteman, \
    Kamikaze, \
    Kit, \
    Paralizer


class BarcoPequeno(Vehiculo):
    def __init__(self):
        super().__init__()
        self.nombre = 'Barco Pequeno'
        self.tipo = 'maritimo'
        self.resistencia = 30
        self.vida = 30
        self.size = (3, 1)
        self.ataques = [Trident(), Minuteman(), Paralizer()]
        self.simbolo = 'B'


class BuqueDeGuerra(Vehiculo):
    def __init__(self):
        super().__init__()
        self.nombre = 'Buque de Guerra'
        self.tipo = 'maritimo'
        self.resistencia = 60
        self.vida = 60
        self.size = (2, 3)
        self.ataques = [Trident(), Tomahawk(), Paralizer()]
        self.simbolo = 'G'


class Lancha(Vehiculo):
    def __init__(self):
        super().__init__()
        self.nombre = 'Lancha'
        self.tipo = 'maritimo'
        self.resistencia = 1
        self.vida = 1
        self.size = (2, 1)
        self.ataques = []
        self.movilidad = float('infinity')
        self.simbolo = 'L'


class Puerto(Vehiculo):
    def __init__(self):
        super().__init__()
        self.nombre = 'Puerto'
        self.tipo = 'maritimo'
        self.resistencia = 80
        self.vida = 80
        self.size = (4, 2)
        self.ataques = [Trident(), Kit(), Paralizer()]
        self.movilidad = 0
        self.simbolo = 'P'


class AvionExplorador(Vehiculo):
    def __init__(self):
        super().__init__()
        self.nombre = 'Avion Explorador'
        self.tipo = 'aereo'
        self.size = (2, 2)
        self.ataques = [Trident()]
        self.movilidad = float('infinity')
        self.turnos_paralizado = 0
        self.simbolo = 'E'
        self.vida = '-'
        self.resistencia = '-'

    def paralizar(self):
        self.turnos_paralizado = 5


class KamikazeIXXI(Vehiculo):
    def __init__(self):
        super().__init__()
        self.nombre = 'Kamikaze IXXI'
        self.tipo = 'aereo'
        self.size = (1, 1)
        self.ataques = [Trident(), Kamikaze()]
        self.movilidad = float('infinity')
        self.simbolo = 'K'
        self.vida = '-'
        self.resistencia = '-'


class AvionCaza(Vehiculo):
    def __init__(self):
        super().__init__()
        self.nombre = 'Avion Caza'
        self.tipo = 'aereo'
        self.size = (1, 1)
        self.ataques = [Trident(), Napalm()]
        self.movilidad = float('infinity')
        self.simbolo = 'C'
        self.vida = '-'
        self.resistencia = '-'