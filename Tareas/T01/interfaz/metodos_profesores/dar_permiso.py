def dar_permiso(menu_profesor):
    alumno_autorizado = input("\nIngrese el usuario del alumno \
que quiere darle un permiso especial: ")
    alumno_existe = False
    nrc_existe = False
    dicta_ramo = False

    for a in menu_profesor.sistema.lista_alumnos:
        if a.usuario == alumno_autorizado:
            alumno_existe = True
            nrc_autorizacion = input('Ingrese el NRC del curso \
que quiere otorgar la autorizacion especial: ')
            for curso in menu_profesor.sistema.lista_cursos:
                if curso.nrc == nrc_autorizacion:
                    nrc_existe = True
                    for p in curso.lista_profesor:
                        if menu_profesor.profesor_in.nombre == p.nombre:
                            dicta_ramo = True
                            if not(curso in a.permisos_especiales):
                                a.permisos_especiales.append(
                                curso)
                                print('\n--- Le ha otorgado un permiso \
especial al alumno(a) {0} para tomar el ramo {1} ---'.format(
                                a.nombre,
                                curso.curso))
                            else:
                                print("\n--- El alumno ya tiene un permiso \
especial para tomar el ramo ---")

                    break
            break

    if not alumno_existe:
        print("\n--- El usuario {0} no existe. ---".format(
            alumno_autorizado))
    elif not nrc_existe:
        print("\n--- El NRC: {0} no existe. ---".format(
            nrc_autorizacion))
    elif not dicta_ramo:
        print("\n--- Usted no dicta el ramo, \
por lo tanto no tiene autorizacion para dar permisos especiales. ---")