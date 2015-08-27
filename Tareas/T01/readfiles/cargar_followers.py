def cargar_followers(lista_alumnos):
    print("\nCargando la bacanosidad de los alumnos...\n")
    total_alumnos = len(lista_alumnos)
    porcentajes = []
    for alumno_follower in range(total_alumnos):

        '''
        #MOSTRAR PORCENTAJE DE AVANCE
        p_avance = int(str((alumno_follower / len(lista_alumnos)) * 100).split('.')[0])
        if p_avance//11 == 9 and not p_avance in porcentajes:
            porcentajes.append(p_avance)
            print(p_avance, end='%\n')
        elif p_avance % 10 == 0:
            if not p_avance in porcentajes:
                porcentajes.append(p_avance)
                print(p_avance, end='% -> ')
        '''

        for idolo in lista_alumnos[alumno_follower].idolos:
            for alumno_idolo in lista_alumnos:
                if alumno_idolo.nombre == idolo:
                    alumno_idolo.followers.append(lista_alumnos[alumno_follower])
    # print(lista_alumnos[23].nombre)
    # for follower in lista_alumnos[23].followers:
    #    print(follower.nombre)
    print("\n--- Archivo 'bacanosidad_alumnos.txt' creado en el directorio de main.py'")
    return lista_alumnos
