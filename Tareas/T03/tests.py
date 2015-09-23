import unittest
from mapa import Mapa
from vehiculo import Vehiculo
from ataque import Ataque
from vehiculos import BarcoPequeno, BuqueDeGuerra, AvionCaza, AvionExplorador, KamikazeIXXI, Lancha, Puerto
from ataques import Trident, Tomahawk, Napalm, Minuteman, Kamikaze, Kit

map = Mapa(5)
barco = BarcoPequeno()

barco.setear_orientacion()

map.agregar_vehiculo(barco)
map.mover_vehiculo(barco)

print(map)