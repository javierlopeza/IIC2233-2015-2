
from mapa import Mapa
from vehiculos import BarcoPequeno, Lancha, AvionCaza, KamikazeIXXI

map = Mapa(5)
barco = BarcoPequeno()
lancha = Lancha()
avion = AvionCaza()
avion2 = AvionCaza()
kam = KamikazeIXXI()

barco.setear_orientacion('v')
lancha.setear_orientacion('h')
avion.setear_orientacion('v')
avion2.setear_orientacion('v')
kam.setear_orientacion('v')

map.agregar_vehiculo(2,2, barco)
map.agregar_vehiculo(3,3, avion)
map.agregar_vehiculo(4,4, kam)

kam.mover(3,4, map)
kam.mover(3,3, map)
print(map)