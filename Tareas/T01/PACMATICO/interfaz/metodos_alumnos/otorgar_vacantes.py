def otorgar_vacantes(sistema):
    puntos_efectivos_totales = 0
    for curso in sistema.lista_cursos:
        # Ordenamos las apuestas de mayor a menor puntaje.
        lista_apuestas_ordenada = sorted(curso.lista_apuestas, key=lambda x: x[1], reverse=True)
        while int(curso.disponibles) > 0:
            for apuesta in lista_apuestas_ordenada:
                apuesta[0].cursos_por_tomar.append(curso)
                apuesta[0].puntos_efectivos += int(apuesta[1])
                curso.lista_de_alumnos.append(apuesta[0])
                curso.ocupados = str(int(curso.ocupados) + 1)
                curso.disponibles = str(int(curso.disponibles) - 1)
            break
    for alumno in sistema.lista_alumnos:
        print(alumno.puntos_efectivos)
        #puntos_efectivos_totales += alumno.puntos_efectivos
    return puntos_efectivos_totales
