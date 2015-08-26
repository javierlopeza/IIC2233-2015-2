import datetime

def cargar_followers(lista_alumnos):
    print(datetime.datetime.now())
    for alumno_follower in lista_alumnos:
        for idolo in alumno_follower.idolos:
            for alumno_idolo in lista_alumnos:
                if alumno_idolo.nombre == idolo:
                    alumno_idolo.followers.append(alumno_follower)
    print(datetime.datetime.now())
    print(lista_alumnos[23].nombre)
    for follower in lista_alumnos[23].followers:
        print(follower.nombre)
    return lista_alumnos
