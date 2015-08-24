from clases import Alumno, Profesor


def cargar_personas():
    personas_file = open("personas.txt").readlines()
    profesores = []
    alumnos = []
    for i in range(len(personas_file)):
        if personas_file[i] == '  {\n':
            if personas_file[i + 1] == '    "idolos": [],\n' and personas_file[i + 4] == '    "ramos_pre": [],\n':
                nombre = personas_file[i + 2][15:-3]
                clave = personas_file[i + 3][14:-3]
                alumno = personas_file[i + 5][15:-3]
                usuario = personas_file[i + 6][16:-2]
                if alumno == "NO":
                    nuevo_profesor = Profesor(nombre=nombre,
                                              usuario=usuario,
                                              clave=clave,
                                              idolos=[],
                                              cursos_aprobados=[]
                                              )
                    profesores.append(nuevo_profesor)
                else:
                    nuevo_alumno = Alumno(nombre=nombre,
                                          usuario=usuario,
                                          clave=clave,
                                          idolos=[],
                                          cursos_aprobados=[]
                                          )
                    alumnos.append(nuevo_alumno)

            else:
                for j in range(i, len(personas_file)):
                    if personas_file[j] == '    ],\n':
                        pre_idolos = personas_file[i + 2:j]
                        idolos = []
                        pre_idolos[-1] += ","
                        for idolo in pre_idolos:
                            idolos.append(idolo[7:-3])
                        break
                for k in range(i + 5 + len(idolos), len(personas_file)):
                    if personas_file[k] == '    ],\n':
                        pre_ramos_pre = personas_file[i + 6 + len(idolos):k]
                        ramos_pre = []
                        pre_ramos_pre[-1] += ","
                        for ramo in pre_ramos_pre:
                            ramos_pre.append(ramo[7:-3])
                        break
                nombre = personas_file[i + 3 + len(idolos)][15:-3]
                clave = personas_file[i + 4 + len(idolos)][14:-3]
                alumno = personas_file[i + 7 + len(idolos) + len(ramos_pre)][15:-3]
                usuario = personas_file[i + 8 + len(idolos) + len(ramos_pre)][16:-2]

                if alumno == "NO":
                    nuevo_profesor = Profesor(nombre=nombre,
                                              usuario=usuario,
                                              clave=clave
                                              )
                    profesores.append(nuevo_profesor)

                else:
                    nuevo_alumno = Alumno(nombre=nombre,
                                          usuario=usuario,
                                          clave=clave,
                                          idolos=idolos,
                                          cursos_aprobados=ramos_pre
                                          )
                    alumnos.append(nuevo_alumno)
                    
    return alumnos, profesores
