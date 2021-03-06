from clases import Curso, Evaluacion
from readfiles.readfile_personas import cargar_personas


def cargar_cursos():
    profesores_sistema = cargar_personas()[1]
    cursos_file = open("./readfiles/cursos.txt", "r", encoding="utf8").readlines()
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
            ofrecidos = 0
            disponibles = 0
            ocupados = 0
            equivalencias_show = ""
            nombre_curso = ""
            nrc = None
            profesores = []
            campus = ""
            creditos = 0
            pre_requisitos_show = ""
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
                    hora_lab = cursos_file[j].split('"')[3]
                elif leido == "sala_lab":
                    sala_lab = cursos_file[j].split(":")[1][2:-3]
                elif leido == "hora_cat":
                    hora_cat = cursos_file[j].split('"')[3]
                elif leido == "sala_cat":
                    sala_cat = cursos_file[j].split(":")[1][2:-3]
                elif leido == "hora_ayud":
                    hora_ayud = cursos_file[j].split('"')[3]
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
                    for profe in profesores_sistema:
                        if profe.nombre == nombre_profesor:
                            profesores.append(profe)
                elif cursos_file[j] == '    "profesor": [\n':
                    profesores = []
                    for k in range(j + 1, len(cursos_file)):
                        if cursos_file[k] == "    ]\n":
                            break
                        else:
                            nombre_profesor = cursos_file[k].split('"')[1]
                            nombre = nombre_profesor.split(" ")[1]
                            apellido = nombre_profesor.split(" ")[0]
                            nombre_profesor = "{0} {1}".format(nombre, apellido)
                            for profe in profesores_sistema:
                                if profe.nombre == nombre_profesor:
                                    profesores.append(profe)

                elif cursos_file[j] == "  },\n":
                    break

            evaluaciones_file = open("./readfiles/evaluaciones.txt").readlines()
            for e in range(len(evaluaciones_file)):
                if evaluaciones_file[e] == "  {\n":
                    sigla_eval = evaluaciones_file[e + 1][14:-3]
                    seccion_eval = evaluaciones_file[e + 3][11:-2]
                    if (sigla_eval == sigla) and (seccion_eval == seccion):
                        tipo_eval = evaluaciones_file[e + 2][13:-3]
                        fecha_eval = evaluaciones_file[e + 4][14:-2]
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
            requisitos_file = open("./readfiles/requisitos.txt").readlines()
            for q in range(len(requisitos_file)):
                if requisitos_file[q] == '  {\n':
                    sigla_curso = requisitos_file[q + 2][14:-3]
                    if sigla_curso == sigla:
                        equivalencias = requisitos_file[q + 1][15:-4]
                        pre_requisitos = requisitos_file[q + 3].split(": ")[1]
                        pre_requisitos = pre_requisitos[1:-2]
                        pre_requisitos_show = pre_requisitos
                        pre_requisitos = pre_requisitos.split(" o ")
                        for w in range(len(pre_requisitos)):
                            if pre_requisitos[w][0] == "(":
                                pre_requisitos[w] = pre_requisitos[w][1:-1]
                            pre_requisitos[w] = pre_requisitos[w].split(" y ")
                        if pre_requisitos[0][0] == 'No tiene':
                            pre_requisitos = []
                        if equivalencias == 'o tien':
                            equivalencias = []
                            equivalencias_show = "No tiene"
                        else:
                            equivalencias_show = equivalencias
                            equivalencias = equivalencias.split(' o ')

            for a in range(len(pre_requisitos)):
                for b in range(len(pre_requisitos[a])):
                    if pre_requisitos[a][b][0] == "(":
                        pre_requisitos[a][b] = pre_requisitos[a][b][1:]
                    if pre_requisitos[a][b][-1] == ")":
                        if pre_requisitos[a][b][-2] != "c":
                            pre_requisitos[a][b] = pre_requisitos[a][b][:-1]

            nuevo_curso = Curso(
                nombre=nombre_curso,
                sigla=sigla,
                nrc=nrc,
                retiro=retiro,
                eng=eng,
                aprobacion_especial=aprobacion_especial,
                lista_profesor=profesores,
                seccion=seccion,
                campus=campus,
                creditos=creditos,
                evaluaciones=evaluaciones,
                pre_requisitos_show=pre_requisitos_show,
                pre_requisitos=pre_requisitos,
                equivalencias_show=equivalencias_show,
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
