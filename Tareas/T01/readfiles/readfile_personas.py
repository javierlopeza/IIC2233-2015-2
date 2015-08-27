from clases import Alumno, Profesor
from readfiles.cargar_followers import cargar_followers


def cargar_personas():
    personas_file = open("./readfiles/personas.txt").readlines()
    profesores = []
    alumnos = []
    for i in range(len(personas_file)):
        if personas_file[i] == '  {\n':
            idolos = []
            nombre = ""
            clave = ""
            ramos_pre = []
            alumno = ""
            usuario = ""
            for j in range(i, len(personas_file)):
                leido = personas_file[j].split(':')[0][5:-1]
                if leido == "nombre":
                    nombre = personas_file[j].split('"')[3]
                elif leido == "clave":
                    clave = personas_file[j].split('"')[3]
                elif leido == "usuario":
                    usuario = personas_file[j].split('"')[3]
                elif leido == "alumno":
                    alumno = personas_file[j].split('"')[3]
                elif personas_file[j] == '    "idolos": [\n':
                    for k in range(j + 1, len(personas_file)):
                        if personas_file[k] == "    ],\n":
                            break
                        else:
                            n_idolo = personas_file[k].split('"')[1]
                            idolos.append(n_idolo)
                elif personas_file[j] == '    "ramos_pre": [\n':
                    for h in range(j + 1, len(personas_file)):
                        if personas_file[h] == "    ],\n":
                            break
                        else:
                            n_ramo_pre = personas_file[h].split('"')[1]
                            ramos_pre.append(n_ramo_pre)
                elif personas_file[j] == "  },\n":
                    break

            if alumno == "NO" and nombre != "Profesores) (Sin" and nombre != "Fijar Por":
                nuevo_profesor = Profesor(nombre=nombre,
                                          usuario=usuario,
                                          clave=clave,
                                          idolos=[],
                                          cursos_aprobados=[],
                                          followers=[]
                                          )
                profesores.append(nuevo_profesor)

            else:
                nuevo_alumno = Alumno(nombre=nombre,
                                      usuario=usuario,
                                      clave=clave,
                                      idolos=idolos,
                                      cursos_aprobados=ramos_pre,
                                      followers=[]
                                      )
                alumnos.append(nuevo_alumno)

    return alumnos, profesores
