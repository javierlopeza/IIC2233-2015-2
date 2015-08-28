def asignar_grupos(lista_alumnos):
    # GRUPO 1
    for i in range(0, 435):
        lista_alumnos[i].grupo_bummer = 1
        lista_alumnos[i].horario_inscripcion = ['08:30', '10:30']
    # GRUPO 2
    for i in range(435, 435 * 2):
        lista_alumnos[i].grupo_bummer = 2
        lista_alumnos[i].horario_inscripcion = ['09:30', '11:30']
    # GRUPO 3
    for i in range(435 * 2, 435 * 3):
        lista_alumnos[i].grupo_bummer = 3
        lista_alumnos[i].horario_inscripcion = ['10:30', '12:30']
    # GRUPO 4
    for i in range(435 * 3, 435 * 4):
        lista_alumnos[i].grupo_bummer = 4
        lista_alumnos[i].horario_inscripcion = ['11:30', '13:30']
    # GRUPO 5
    for i in range(435 * 4, 435 * 5):
        lista_alumnos[i].grupo_bummer = 5
        lista_alumnos[i].horario_inscripcion = ['12:30', '14:30']
    # GRUPO 6
    for i in range(435 * 5, 435 * 6):
        lista_alumnos[i].grupo_bummer = 6
        lista_alumnos[i].horario_inscripcion = ['13:30', '15:30']
    # GRUPO 7
    for i in range(435 * 6, 435 * 7):
        lista_alumnos[i].grupo_bummer = 7
        lista_alumnos[i].horario_inscripcion = ['14:30', '16:30']
    # GRUPO 8
    for i in range(435 * 7, 435 * 8):
        lista_alumnos[i].grupo_bummer = 8
        lista_alumnos[i].horario_inscripcion = ['15:30', '17:30']
    # GRUPO 9
    for i in range(435 * 8, 435 * 9):
        lista_alumnos[i].grupo_bummer = 9
        lista_alumnos[i].horario_inscripcion = ['16:30', '18:30']
    # GRUPO 10
    for i in range(435 * 9, len(lista_alumnos)):
        lista_alumnos[i].grupo_bummer = 10
        lista_alumnos[i].horario_inscripcion = ['17:30', '19:30']

    for alumno in lista_alumnos:
        alumno.maximo_creditos_permitidos = \
            ((55 + 2 * (6 - alumno.grupo_bummer)) // 5) * 5

    return lista_alumnos
