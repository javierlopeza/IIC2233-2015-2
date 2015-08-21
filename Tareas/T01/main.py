from clases import Persona, Alumno, Profesor, Horario, Curso, Evaluacion

javier = Alumno(nombre_apellido="Javier Lopez", usuario="jilopez8", clave="jla123", alumno="SI", idolos=["Juan Perez","Jose Gonzalez"], cursos_aprobados=["IIC1103","MAT1620"])
print(javier.alumno)
progra = Curso(sigla="IIC1103", profesor="Bellido Jesus", lista_de_alumnos=["a1","a2"], seccion=2, campus="San Joaquin", evaluaciones=[], pre_requisitos=[123], capacidad_maxima=100, hora_cat="L-W-V:3", sala_cat="CS-101", hora_ayud="", sala_ayud="", hora_lab="", sala_lab="") 
print(progra.profesor.apellido)
