import datetime
import sistema
from Conexion_Puerto_RedATT import Red
from writefile_redATT import writefile_red

t1 = datetime.datetime.now()

red_bummer = Red()
red_bummer.agregar_puerto(0, sistema.posibles_conexiones())

while red_bummer.revisar_completitud():
#iteraciones = 10000
#for w in range(iteraciones):
    ide_puerto_actual = sistema.preguntar_puerto_actual()[0]
    posibles_conexiones_puerto_actual = sistema.posibles_conexiones()
    red_bummer.agregar_puerto(ide_puerto_actual, posibles_conexiones_puerto_actual)
    red_bummer.puerto(ide_puerto_actual).conectar(sistema)
    #print("Porcentaje progreso: {}%".format(round((100 * w)/iteraciones)), end="\r")

t2 = datetime.datetime.now()
print("TIEMPO DE RECORRIDO TOTAL:", t2 - t1)


# ------------------------------------
writefile_red(red_bummer)
# -----------------------------------

print(40 * "-")
print("TOTAL PUERTOS:", len(red_bummer.puertos))

total_pasadas = 0
for k in range(len(red_bummer.puertos)):
    #print("PUERTO:", red_bummer.puertos[k].ide)
    for j in range(len(red_bummer.puertos[k].conexiones)):
        total_pasadas += red_bummer.puertos[k].conexiones[j].pasadas
        #print("C({0}):".format(j), red_bummer.puertos[k].conexiones[j].puertos_destino)
print("TOTAL PASADAS:", total_pasadas)