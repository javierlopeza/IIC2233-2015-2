import unittest
from mapa import Mapa
from vehiculo import Vehiculo
from ataque import Ataque
from vehiculos import BarcoPequeno, BuqueDeGuerra, AvionCaza, AvionExplorador, KamikazeIXXI, Lancha, Puerto
from ataques import Trident, Tomahawk, Napalm, Minuteman, Kamikaze, Kit

map = Mapa(5)
barco = BarcoPequeno()
lancha = Lancha()
avion = AvionCaza()
kam = KamikazeIXXI()

barco.setear_orientacion()
avion.setear_orientacion()
kam.setear_orientacion()

map.agregar_vehiculo(barco)
map.agregar_vehiculo(avion)
map.agregar_vehiculo(kam)
map.mover_vehiculo(avion)
map.mover_vehiculo(kam)
map.mover_vehiculo(barco)
print(map)