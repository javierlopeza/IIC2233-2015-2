def pedir_curso(menu_alumno):
    existe_nrc = False
    cumple_requisito = False
    curso_posible = None
    curso_pedido_exito = False
    ya_tiene_curso = False

    curso_a_pedir = input("\nIngrese el NRC del curso que desea inscribir: ")

    for curso in menu_alumno.alumno_in.cursos_por_tomar:
        if curso_a_pedir == curso.nrc:
            ya_tiene_curso = True

    if not ya_tiene_curso:
        for curso in menu_alumno.sistema.lista_cursos:

            if curso.nrc == curso_a_pedir:
                curso_posible = curso
                existe_nrc = True

                if existe_nrc:

                    if int(curso_posible.disponibles) > 0:
                        if menu_alumno.alumno_in.tiene_permiso_especial(
                                menu_alumno,
                                curso_posible):
                            cumple_requisito = True
                        elif curso_posible.pre_requisitos:
                            for opcion_req in curso_posible.pre_requisitos:
                                n_cursos_requisitos = len(opcion_req)
                                for sigla_curso_req in opcion_req:
                                    if menu_alumno.alumno_in.aprobo_curso(menu_alumno, sigla_curso_req):
                                        n_cursos_requisitos -= 1
                                    if n_cursos_requisitos == 0:
                                        cumple_requisito = True
                        elif not curso_posible.pre_requisitos:
                            cumple_requisito = True

                        if cumple_requisito:
                            menu_alumno.alumno_in.cursos_pedidos.append(curso_posible)
                            curso_pedido_exito = True

    if ya_tiene_curso:
        print("\n--- El curso que desea pedir ya lo ha solicitado. ---\n")

    elif not existe_nrc:
        print("\n--- ERROR: El NRC:{0} ingresado no existe. ---\n".format(
            curso_a_pedir))

    elif not int(curso_posible.disponibles) > 0:
        print("\n--- ERROR: El curso {0}-{1} no posee \
vacantes disponibles. ---\n".format(
            curso_posible.sigla,
            curso_posible.seccion
        ))

    elif not cumple_requisito:
        print("\n--- ERROR: No cumple con alguno de los \
prerrequisitos del curso. ---\n")

    elif curso_pedido_exito:
        print("\n--- PETICION EXITOSA: El curso {0}-{1} fue pedido exitosamente. ---\n".format(
            curso_posible.sigla,
            curso_posible.seccion
        ))