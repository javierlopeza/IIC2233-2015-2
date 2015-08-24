def agregar_evaluaciones_a_cursos(lista_cursos, lista_evaluaciones):
	for i in range(len(lista_evaluaciones)):
		sigla_eval = lista_evaluaciones[i].curso
		seccion_eval = lista_evaluaciones[i].seccion
		for j in range(len(lista_cursos)):
			sigla_curso = lista_cursos[j].sigla
			seccion_curso = lista_cursos[j].seccion
			if (sigla_eval == sigla_curso) and (seccion_eval == seccion_curso):
				lista_cursos[j].evaluaciones.append(lista_evaluaciones[i])
				break
	return lista_cursos