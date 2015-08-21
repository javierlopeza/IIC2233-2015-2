from clases import Persona, Alumno, Profesor, Horario, Curso, Evaluacion




javier = Alumno(nombre_apellido="Javier Lopez", usuario="jilopez8", clave="jla123", alumno="SI", idolos=["Juan Perez","Jose Gonzalez"], cursos_aprobados=["IIC1103","MAT1620"])
print(javier.alumno)
progra = Curso(sigla="IIC1103", profesor="Bellido Jesus", lista_de_alumnos=["a1","a2"], seccion=2, campus="San Joaquin", evaluaciones=[], pre_requisitos=[123], capacidad_maxima=100, hora_cat="L-W-V:3", sala_cat="CS-101", hora_ayud="", sala_ayud="", hora_lab="", sala_lab="") 
print(progra.profesor.apellido)

algebra = Curso(nombre="", sigla="", nrc=0, retiro="", eng="", aprobacion_especial="", profesor="Wolfgang Rivera", lista_de_alumnos=[], seccion=0, campus="", creditos=0, evaluaciones=[], pre_requisitos=[], equivalencias=[], ocupados=0, disponibles=50, ofrecidos=50)
javier.inscribir_ramo(algebra)
print(javier.cursos_por_tomar[0].profesor.apellido)
print(algebra.disponibles)
print(algebra.ofrecidos)
print(algebra.ocupados)
