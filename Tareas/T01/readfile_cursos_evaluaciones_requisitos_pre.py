from clases import Curso, Evaluacion


def cargar_cursos():
    cursos_file = open("cursos.txt", "r", encoding="utf8").readlines()
    cursos = []
    for i in range(len(cursos_file)):
        if cursos_file[i] == '  {\n':
            retiro = "---"
            eng = "---"
            aprobacion_especial = "---"
            hora_cat = "---"
            sala_cat = "---"
            hora_ayud = "---"
            sala_ayud = "---"
            hora_lab = "---"
            sala_lab = "---"
            evaluaciones = []
            equivalencias = []
            pre_requisitos = []
            for j in range(i, len(cursos_file)):
                leido = cursos_file[j].split(":")[0][5:-1]
                if leido == "disp":
                    disponibles = cursos_file[j].split(":")[1][1:-2]
                elif leido == "ocu":
                    ocupados = cursos_file[j].split(":")[1][1:-2]
                elif leido == "ofr":
                    ofrecidos = cursos_file[j].split(":")[1][1:-2]
                elif leido == "curso":
                    nombre_curso = cursos_file[j].split(":")[1][2:-3]
                elif leido == "apr":
                    aprobacion_especial = cursos_file[j].split(":")[1][2:-3]
                elif leido == "eng":
                    eng = cursos_file[j].split(":")[1][2:-3]
                elif leido == "cred":
                    creditos = cursos_file[j].split(":")[1][1:-2]
                elif leido == "sec":
                    seccion = cursos_file[j].split(":")[1][1:-2]
                elif leido == "NRC":
                    nrc = cursos_file[j].split(":")[1][1:-2]
                elif leido == "hora_lab":
                    hora_lab = cursos_file[j].split(":")[1][2:-3]
                elif leido == "sala_lab":
                    sala_lab = cursos_file[j].split(":")[1][2:-3]
                elif leido == "hora_cat":
                    hora_cat = cursos_file[j].split(":")[1][2:-3]
                elif leido == "sala_cat":
                    sala_cat = cursos_file[j].split(":")[1][2:-3]
                elif leido == "hora_ayud":
                    hora_ayud = cursos_file[j].split(":")[1][2:-3]
                elif leido == "sala_ayud":
                    sala_ayud = cursos_file[j].split(":")[1][2:-3]
                elif leido == "campus":
                    campus = cursos_file[j].split(":")[1][2:-3]
                elif leido == "sigla":
                    sigla = cursos_file[j].split(":")[1][2:-3]
                elif leido == "retiro":
                    retiro = cursos_file[j].split(":")[1][2:-3]
                elif (leido == "profesor") and \
                        (cursos_file[j] != '    "profesor": [\n'):
                    profesores = []
                    nombre_profesor = cursos_file[j].split(":")[1][2:-2]
                    nombre = nombre_profesor.split(" ")[1]
                    apellido = nombre_profesor.split(" ")[0]
                    nombre_profesor = "{0} {1}".format(nombre, apellido)
                    profesores.append(nombre_profesor)
                elif cursos_file[j] == '    "profesor": [\n':
                    profesores = []
                    for k in range(j + 1, len(cursos_file)):
                        if cursos_file[k] == "    ]\n":
                            break
                        else:
                            nombre_profesor = cursos_file[k].split('"')[1]
                            nombre = nombre_profesor.split(" ")[1]
                            apellido = nombre_profesor.split(" ")[0]
                            nombre_profesor = nombre + " " + apellido
                            profesores.append(nombre_profesor)
                elif cursos_file[j] == "  },\n":
                    break

            evaluaciones_file = open("evaluaciones.txt").readlines()
            for i in range(len(evaluaciones_file)):
                if evaluaciones_file[i] == "  {\n":
                    sigla_eval = evaluaciones_file[i + 1][14:-3]
                    seccion_eval = evaluaciones_file[i + 3][11:-2]
                    if (sigla_eval == sigla) and (seccion_eval == seccion):
                        tipo_eval = evaluaciones_file[i + 2][13:-3]
                        fecha_eval = evaluaciones_file[i + 4][14:-2]
                        dia_eval = fecha_eval.split(" - ")[0]
                        hora_eval = fecha_eval.split(" - ")[1]
                        if hora_eval[-1] == '"':
                            hora_eval = hora_eval[:-1]
                        nueva_evaluacion = Evaluacion(
                            nombre=tipo_eval,
                            hora=hora_eval,
                            dia=dia_eval,
                            curso=sigla_eval,
                            seccion=seccion_eval
                        )
                        evaluaciones.append(nueva_evaluacion)
            requisitos_file = open("requisitos.txt").readlines()
            for i in range(len(requisitos_file)):
                if requisitos_file[i] == '  {\n':
                    sigla_curso = requisitos_file[i + 2][14:-3]
                    if sigla_curso == sigla:
                        equivalencias = requisitos_file[i + 1][15:-4]
                        pre_requisitos = requisitos_file[i + 3].split(": ")[1][1:-2]
                        if equivalencias == 'o tien':
                            equivalencias = ['No tiene']
                        else:
                            equivalencias = equivalencias.split(' o ')

            nuevo_curso = Curso(
                nombre=nombre_curso,
                sigla=sigla,
                nrc=nrc,
                retiro=retiro,
                eng=eng,
                aprobacion_especial=aprobacion_especial,
                profesor=profesores,
                seccion=seccion,
                campus=campus,
                creditos=creditos,
                evaluaciones=evaluaciones,
                pre_requisitos=pre_requisitos,
                equivalencias=equivalencias,
                ocupados=ocupados,
                disponibles=disponibles,
                ofrecidos=ofrecidos,
                hora_cat=hora_cat,
                sala_cat=sala_cat,
                hora_ayud=hora_ayud,
                sala_ayud=sala_ayud,
                hora_lab=hora_lab,
                sala_lab=sala_lab
            )
            cursos.append(nuevo_curso)
    return cursos
