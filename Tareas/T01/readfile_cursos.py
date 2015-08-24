from clases import Curso


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
