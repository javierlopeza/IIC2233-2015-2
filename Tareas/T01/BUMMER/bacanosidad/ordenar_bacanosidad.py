def ordenar_bacanosidad(lista_alumnos):
    archivo_bacanosidades = open("bacanosidad.txt","w")
    lista_alumnos_ordenada = sorted(lista_alumnos, key=lambda x: x.puntos_recibidos, reverse=True)
    mas_bacan = lista_alumnos_ordenada[0].puntos_recibidos
    for alumno in lista_alumnos_ordenada:
        alumno.bacanosidad_relativa = alumno.puntos_recibidos/mas_bacan
        escribir = alumno.nombre + '\t\t\t' + str(alumno.bacanosidad_relativa) + '\n'
        archivo_bacanosidades.write(escribir)
    return lista_alumnos_ordenada