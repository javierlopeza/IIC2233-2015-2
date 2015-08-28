def readfile_bacanosidad(lista_alumnos):
    bacanosidad_file = open('bacanosidad.txt').readlines()
    for linea in bacanosidad_file:
        linea = linea.split('\t\t\t')
        nombre_alumno = linea[0]
        bacanosidad_relativa = linea[1][:-1]
        for alumno in lista_alumnos:
            if alumno.nombre == nombre_alumno:
                alumno.bacanosidad_relativa = bacanosidad_relativa
    lista_alumnos_ordenada = sorted(lista_alumnos, key=lambda x: x.bacanosidad_relativa, reverse=True)

    return lista_alumnos_ordenada