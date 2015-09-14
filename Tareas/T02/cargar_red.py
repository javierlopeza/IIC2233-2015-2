import datetime
from Conexion_Puerto_Red import Red
from clasificar_conexiones import clasificar_conexiones
from writefile_red import writefile_red
from ListaLigada import ListaLigada


def cargar_red(sistema):
    t1 = datetime.datetime.now()

    red_bummer = Red()
    red_bummer.agregar_puerto(0, sistema.posibles_conexiones())
    camino = ListaLigada()
    camino.append(0)
    while red_bummer.revisar_completitud():
        ide_puerto_actual = sistema.preguntar_puerto_actual()[0]
        posibles_conexiones_puerto_actual = sistema.posibles_conexiones()
        red_bummer.agregar_puerto(ide_puerto_actual, posibles_conexiones_puerto_actual)
        red_bummer.puerto(ide_puerto_actual).conectar(sistema)
        if sistema.preguntar_puerto_actual()[0] == sistema.puerto_final():
            camino.append(sistema.puerto_final())
            red_bummer.caminos.append(camino)
            camino = ListaLigada()
        elif not sistema.preguntar_puerto_actual()[1]:
            camino.append(sistema.preguntar_puerto_actual()[0])
        elif sistema.preguntar_puerto_actual()[1]:
            camino = ListaLigada()
            camino.append(0)


        # print("Porcentaje progreso: {}%".format(round((100 * w)/iteraciones)), end="\r")

    t2 = datetime.datetime.now()
    print("---> TIEMPO EN CONSTRUIR LA RED DE BUMMER:", t2 - t1)

    print("---> CLASIFICANDO CONEXIONES")
    clasificar_conexiones(red_bummer)

    print("---> GENERANDO ARCHIVO red.txt")
    writefile_red(red_bummer)

    return red_bummer