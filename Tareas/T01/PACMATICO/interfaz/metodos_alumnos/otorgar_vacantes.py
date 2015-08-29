def otorgar_vacantes(sistema):
    puntos_efectivos_totales = 0
    for curso in sistema.lista_cursos:
        # Ordenamos las apuestas de mayor a menor puntaje.
        lista_apuestas_ordenada = sorted(curso.lista_apuestas, key=lambda x: x[1], reverse=True)
        while int(curso.disponibles) > 0:
            for apuesta in lista_apuestas_ordenada:
                cumple_requisito = False

                if  apuesta[0].tiene_permiso_especial(
                        apuesta[0],
                        curso):
                    cumple_requisito = True
                elif curso.pre_requisitos:
                    for opcion_req in curso.pre_requisitos:
                        n_cursos_requisitos = len(opcion_req)
                        for sigla_curso_req in opcion_req:
                            if  apuesta[0].aprobo_curso(apuesta[0], sigla_curso_req):
                                n_cursos_requisitos -= 1
                            if n_cursos_requisitos == 0:
                                cumple_requisito = True
                elif not curso.pre_requisitos:
                    cumple_requisito = True

                if cumple_requisito:
                    apuesta[0].cursos_por_tomar.append(curso)
                    apuesta[0].puntos_efectivos += int(apuesta[1])
                    curso.lista_de_alumnos.append(apuesta[0])
                    curso.ocupados = str(int(curso.ocupados) + 1)
                    curso.disponibles = str(int(curso.disponibles) - 1)
            break
    for alumno in sistema.lista_alumnos:
        puntos_efectivos_totales += alumno.puntos_efectivos
    print("\n---  Se han otorgado las vacantes a los alumnos con mayores apuestas en los cursos.  ---")
    print("---  Se ha logrado un maximo total de {0} Puntos Efectivos ---\n".format(puntos_efectivos_totales))
    return puntos_efectivos_totales
