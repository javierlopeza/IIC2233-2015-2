import datetime
from Conexion_Puerto_Red import Red
from clasificar_conexiones import clasificar_conexiones
from writefile_red import writefile_red


def cargar_red(sistema):
    t1 = datetime.datetime.now()

    red_bummer = Red()
    red_bummer.agregar_puerto(
        0,
        sistema.posibles_conexiones(),
        sistema.get_capacidad()
    )
    while red_bummer.revisar_completitud():
        ide_puerto_actual = sistema.preguntar_puerto_actual()[0]
        posibles_conexiones_puerto_actual = sistema.posibles_conexiones()
        capacidad_puerto_actual = sistema.get_capacidad()
        red_bummer.agregar_puerto(
            ide_puerto_actual,
            posibles_conexiones_puerto_actual,
            capacidad_puerto_actual)
        red_bummer.puerto(ide_puerto_actual).conectar(sistema)

    t2 = datetime.datetime.now()
    print("---> TIEMPO EN CONSTRUIR LA RED DE BUMMER:", t2 - t1)

    print("---> CLASIFICANDO CONEXIONES")
    clasificar_conexiones(red_bummer)

    print("---> GENERANDO ARCHIVO red.txt")
    writefile_red(red_bummer)

    return red_bummer