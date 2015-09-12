import datetime
import sistema
from Conexion_Puerto_Red import Red
from writefile_red import writefile_red

t1 = datetime.datetime.now()
print("INICIO:", t1)

red_bummer = Red()
red_bummer.agregar_puerto(0, sistema.posibles_conexiones())


while red_bummer.revisar_completitud():
#for w in range(1000):
    ide_puerto_actual = sistema.preguntar_puerto_actual()[0]
    posibles_conexiones_puerto_actual = sistema.posibles_conexiones()
    red_bummer.agregar_puerto(ide_puerto_actual, posibles_conexiones_puerto_actual)
    red_bummer.puerto(ide_puerto_actual).conectar(sistema)

t2 = datetime.datetime.now()
print("FIN RECORRER:", t2)
print("TOTAL:", t2 - t1)


# ------------------------------------
writefile_red(red_bummer)
# -----------------------------------

print(40 * "-")
for k in range(len(red_bummer.puertos)):
    print("PUERTO:", red_bummer.puertos[k].ide)
    for j in range(len(red_bummer.puertos[k].conexiones)):
        print("C({0}):".format(j), red_bummer.puertos[k].conexiones[j].puertos_destino)
