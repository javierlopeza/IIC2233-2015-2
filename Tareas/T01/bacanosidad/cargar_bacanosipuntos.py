def cargar_bacanosipuntos(lista_alumnos):
    for alumno in lista_alumnos:
        n_followers = len(alumno.followers)
        alumno.bacanosipuntos = n_followers

    for alumno in lista_alumnos:
        n_encuentra_bacanes = len(alumno.idolos)
        if n_encuentra_bacanes != 0:
            puntos_a_repartir = alumno.bacanosipuntos / n_encuentra_bacanes
            for idolo in alumno.idolos:
                idolo.puntos_recibidos += puntos_a_repartir

    # ESTA PARTE DEL CODIGO CALCULA LA EFICIENCIA PORCENTUAL DE MI ALGORITMO DE ASIGNACION DE BACANOSIDAD
    # EL ALGORITMO PERFECTO SEGUN EL ENUNCIADO TENDRIA EFICIENCIA DEL 100%,
    # PERO ESTE TIENE CERCA DE UN 92,7113% POR LO CALCULADO CON EL ARCHIVO DADO DE PERSONAS.
    d = 0
    bp = 0
    pr = 0
    for alumno in lista_alumnos:
        diferencia = alumno.bacanosipuntos - alumno.puntos_recibidos
        d += abs(diferencia)
        bp += alumno.bacanosipuntos
        pr += alumno.puntos_recibidos

    total_alumnos = len(lista_alumnos)
    promedio_diferencias = d / total_alumnos
    promedio_bacanosipuntos = bp / total_alumnos
    promedio_puntosrepartidos = pr / total_alumnos
    promedio_bp_pr = (promedio_bacanosipuntos + promedio_puntosrepartidos) / 2
    eficiencia_porcentual = 100 - (promedio_diferencias / promedio_bp_pr) * 100
    # print("EFICIENCIA ======", eficiencia_porcentual)
    print("\n        --- Archivo 'bacanosidad.txt' creado en el directorio de main.py' ---")
    print("--- Se cargaran las bacanosidades guardadas en dicho archivo la proxima vez que inicie main.py' ---\n")

    return lista_alumnos
