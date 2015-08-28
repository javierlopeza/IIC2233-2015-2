def cargar_followers(lista_alumnos):
    print("\nCargando la bacanosidad de los alumnos...\n")
    total_alumnos = len(lista_alumnos)
    for alumno_follower in range(total_alumnos):
        lista_alumnos[alumno_follower].idolos_instanciados = True
        for idolo in range(len(lista_alumnos[alumno_follower].idolos)):
            for alumno_idolo in lista_alumnos:
                if alumno_idolo.nombre == lista_alumnos[alumno_follower].idolos[idolo]:
                    alumno_idolo.followers.append(lista_alumnos[alumno_follower])
                    lista_alumnos[alumno_follower].idolos[idolo] = alumno_idolo
    return lista_alumnos
