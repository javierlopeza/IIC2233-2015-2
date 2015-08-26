def quitar_permiso(menu_profesor):
    alumno_desautorizado = input("\nIngrese el usuario del alumno \
que quiere quitarle su permiso especial: ")
    alumno_existe = False
    nrc_existe = False
    dicta_ramo = False

    for a in menu_profesor.sistema.lista_alumnos:
        if a.usuario == alumno_desautorizado:
            alumno_existe = True
            nrc_desautorizacion = input('Ingrese el NRC del curso \
que quiere quitar la autorizacion especial: ')
            for curso in menu_profesor.sistema.lista_cursos:
                if curso.nrc == nrc_desautorizacion:
                    nrc_existe = True
                    for p in curso.lista_profesor:
                        if menu_profesor.profesor_in.nombre == p.nombre:
                            dicta_ramo = True
                            if curso in a.permisos_especiales:
                                a.permisos_especiales.remove(
                                curso)
                                if curso in a.cursos_por_tomar:
                                    a.cursos_por_tomar.remove(curso)
                                print('\n--- Le ha quitado el permiso \
especial al alumno(a) {0} para tomar el ramo {1} ---'.format(
                                a.nombre,
                                curso.curso))
                            else:
                                print("\n--- El alumno no tenia un permiso \
especial para tomar el ramo ---")

                    break
            break

    if not alumno_existe:
        print("\n--- El usuario {0} no existe. ---".format(
            alumno_desautorizado))
    elif not nrc_existe:
        print("\n--- El NRC: {0} no existe. ---".format(
            nrc_desautorizacion))
    elif not dicta_ramo:
        print("\n--- Usted no dicta el ramo, \
por lo tanto no tiene autorizacion para quitar permisos especiales. ---")