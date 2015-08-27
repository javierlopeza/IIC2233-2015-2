from interfaz.metodos_alumnos.generar_horario import generar_horario


def inscribir_curso(menu_alumno):
    hora = input("\nIngrese la hora actual [HH:MM]:")

    hora_valida = False
    if len(hora) == 5 and hora[2] == ":":
        if 48 <= ord(hora[0]) <= 50:
            if 48 <= ord(hora[1]) <= 57:
                if 48 <= ord(hora[3]) <= 53:
                    if 48 <= ord(hora[4]) <= 57:
                        hora_valida = True

    #FALTA VERIFICAR QUE LA HORA CORRESPONDE A SU GRUPO

    existe_nrc = False
    tope_horario = False
    tope_campus = False
    cumple_requisito = False
    cursos_topados = None
    foto_horario_tope = None
    cursos_tope_campus = None
    curso_posible = None
    tope_evaluaciones = False
    cursos_tope_evaluaciones = None
    exceso_creditos = False
    curso_inscrito_exito = False
    curso_a_inscribir = None
    ya_tiene_curso = False

    if hora_valida:
        curso_a_inscribir = input("\nIngrese el NRC del curso que desea inscribir: ")

        for curso in menu_alumno.alumno_in.cursos_por_tomar:
            if curso.nrc == curso_a_inscribir:
                ya_tiene_curso = True

        if not ya_tiene_curso:
            for curso in menu_alumno.sistema.lista_cursos:

                if curso.nrc == curso_a_inscribir:
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
                                cursos_por_tomar_posible = menu_alumno.alumno_in.cursos_por_tomar[:]
                                cursos_por_tomar_posible.append(curso_posible)
                                horario_posible = generar_horario(cursos_por_tomar_posible)[1]
                                for d in range(len(horario_posible)):
                                    for m in range(len(horario_posible[d])):
                                        if horario_posible[d][m - 1]:
                                            if horario_posible[d][m - 1][0].campus != curso_posible.campus:
                                                tope_campus = True
                                                cursos_tope_campus = [
                                                    horario_posible[d][m - 1][0],
                                                    horario_posible[d][m][0]]
                                        if m != 7:
                                            if horario_posible[d][m + 1]:
                                                if horario_posible[d][m + 1][0].campus != curso_posible.campus:
                                                    tope_campus = True
                                                    cursos_tope_campus = [
                                                        horario_posible[d][m + 1][0],
                                                        horario_posible[d][m][0]]
                                        if len(horario_posible[d][m]) > 1:
                                            tope_horario = True
                                            cursos_topados = horario_posible[d][m][:]
                                            foto_horario_tope = generar_horario(cursos_por_tomar_posible)[0]

                                if not (tope_horario or tope_campus):
                                    for curso_tomado in menu_alumno.alumno_in.cursos_por_tomar:
                                        if curso_tomado.evaluaciones:
                                            for evaluacion in curso_tomado.evaluaciones:
                                                for evaluacion_posible in curso_posible.evaluaciones:
                                                    if evaluacion.hora == evaluacion_posible.hora:
                                                        if evaluacion.dia == evaluacion_posible.dia:
                                                            cursos_tope_evaluaciones = [
                                                                curso_posible,
                                                                curso_tomado]
                                                            tope_evaluaciones = True

                                    if not tope_evaluaciones:
                                        creditos_por_tomar = 0
                                        for curso_tomado in menu_alumno.alumno_in.cursos_por_tomar:
                                            creditos_por_tomar += int(curso_tomado.creditos)
                                        creditos_hipoteticos = \
                                            int(curso_posible.creditos) + \
                                            creditos_por_tomar
                                        if creditos_hipoteticos > menu_alumno.alumno_in.maximo_creditos_permitidos:
                                            exceso_creditos = True

                                        if not exceso_creditos:
                                            curso_posible.disponibles = str(int(curso_posible.disponibles) - 1)
                                            curso_posible.ocupados = str(int(curso_posible.ocupados) + 1)
                                            curso_posible.lista_de_alumnos.append(menu_alumno.alumno_in)
                                            menu_alumno.alumno_in.cursos_por_tomar.append(curso_posible)
                                            curso_inscrito_exito = True

    if not hora_valida:
        print("\n--- La hora ingresada no respeta el formato valido. ---\n")

    elif ya_tiene_curso:
        print("\n--- El curso que desea inscribir ya lo tiene inscrito. ---\n")

    elif not existe_nrc:
        print("\n--- ERROR: El NRC:{0} ingresado no existe. ---\n".format(
            curso_a_inscribir))

    elif not int(curso_posible.disponibles) > 0:
        print("\n--- ERROR: El curso {0}-{1} no posee \
vacantes disponibles. ---\n".format(
            curso_posible.sigla,
            curso_posible.seccion
        ))

    elif not cumple_requisito:
        print("\n--- ERROR: No cumple con alguno de los \
prerrequisitos del curso. ---\n")

    elif tope_horario:
        print("\n--- ERROR: Los cursos {0}-{1} y {2}-{3} \
tienen tope de horario como se muestra en el horario impreso abajo. \
---\n".format(
            cursos_topados[0].sigla,
            cursos_topados[0].seccion,
            cursos_topados[1].sigla,
            cursos_topados[1].seccion))
        print(foto_horario_tope)

    elif tope_campus:
        print("\n--- ERROR: Los cursos {0}-{1} y {2}-{3} \
se dictan de forma consecutiva en campus diferentes. ---\n".format(
            cursos_tope_campus[0].sigla,
            cursos_tope_campus[0].seccion,
            cursos_tope_campus[1].sigla,
            cursos_tope_campus[1].seccion))

    elif tope_evaluaciones:
        print("\n--- ERROR: Los cursos {0}-{1} y {2}-{3} \
presentan tope de fechas en sus evaluaciones. ---\n".format(
            cursos_tope_evaluaciones[0].sigla,
            cursos_tope_evaluaciones[0].seccion,
            cursos_tope_evaluaciones[1].sigla,
            cursos_tope_evaluaciones[1].seccion))

    elif exceso_creditos:
        print("\n--- ERROR: Al tomar este curso excede su maximo de \
creditos permitidos que corresponde a {0} creditos. ---\n".format(
            menu_alumno.alumno_in.maximo_creditos_permitidos
        ))

    elif curso_inscrito_exito:
        print("\n--- INSCRIPCION EXITOSA: El curso {0}-{1} fue inscrito exitosamente. ---\n".format(
            curso_posible.sigla,
            curso_posible.seccion
        ))
