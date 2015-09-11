import sistema
from ListaLigada import ListaLigada
from Puerto_Red import Conexion, Puerto, Red

print("PUERTO MI PC:", sistema.puerto_inicio())
print("PUERTO BUMMER:", sistema.puerto_final())

print()

red_bummer = Red()
red_bummer.agregar_puerto(0, sistema.posibles_conexiones())

for i in range(1000):
    ide_puerto_actual = sistema.preguntar_puerto_actual()[0]
    posibles_conexiones_puerto_actual = sistema.posibles_conexiones()
    nuevo_puerto = red_bummer.agregar_puerto(ide_puerto_actual, posibles_conexiones_puerto_actual)
    red_bummer.puerto(ide_puerto_actual).conectar(sistema)

for n in range(len(red_bummer.puertos)):
    print(red_bummer.puertos[n].ide)
