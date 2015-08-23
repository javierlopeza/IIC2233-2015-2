from clases import Persona, Alumno, Profesor, Horario, Curso, Evaluacion


def cargar_cursos():
    cursos_file = open("cursos.txt", "r", encoding="utf8").readlines()
    cursos = []
    for i in range(len(cursos_file)):
        if cursos_file[i] == '  {\n':
            for j in range(i, len(cursos_file)):
            	leido = cursos_file[j].split(":")[0][5:-1]
            	if leido == "disp":
            		disponibles = cursos_file[j].split(":")[1][1:-2]
            	elif leido == "ocu":
            		ocupados = cursos_file[j].split(":")[1][1:-2]
            	elif leido == "ofr":
            		ofrecidos = cursos_file[j].split(":")[1][1:-2]
            	elif leido == "curso":
            		nombre = cursos_file[j].split(":")[1][2:-3]
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

            	elif cursos_file[j] == "  },\n":
            		print("fin curso")

            		break

            print(sigla, retiro)


cargar_cursos()
