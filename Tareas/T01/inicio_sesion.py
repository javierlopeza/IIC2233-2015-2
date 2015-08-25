

def iniciar_sesion(usuario, clave, lista_alumnos, lista_profesores, es_alumno):
    if es_alumno == "SI":
        for alumno in lista_alumnos:
            if alumno.usuario == usuario and alumno.clave == clave:
                print("\nSesion iniciada exitosamente, bienvenido(a)", alumno.nombre, "\n")
                return alumno


    if es_alumno == "NO":
        for profesor in lista_profesores:
            if profesor.usuario == usuario and profesor.clave == clave:
                print("\nSesion iniciada exitosamente, bienvenido(a)", profesor.nombre, "\n")
                return alumno
    else:
        print('--- Usuario o clave incorrectos ---')
        return False
