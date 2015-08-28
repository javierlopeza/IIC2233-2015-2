def cargar_apuestas_a_cursos(lista_cursos, lista_alumnos):
    for alumno in lista_alumnos:
        for curso_apuesta in alumno.cursos_con_puntajes:
            curso_apostado = curso_apuesta[0]
            apuesta = curso_apuesta[1]
            for curso in lista_cursos:
                if curso_apostado.nrc == curso.nrc:
                    curso.lista_apuestas.append([alumno, apuesta])
