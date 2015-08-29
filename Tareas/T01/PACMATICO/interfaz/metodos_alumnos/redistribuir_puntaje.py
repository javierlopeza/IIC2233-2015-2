def redistribuir_puntaje(cursos_pedidos, puntos_pucmatico_alumno):
    n_cursos_pedidos = len(cursos_pedidos)
    puntos_redistribuidos = 0
    creditos_redistribuidos = 0
    if n_cursos_pedidos > 1:
        puntos_por_curso = puntos_pucmatico_alumno / n_cursos_pedidos

        cursos_con_puntajes = []

        for curso_pedido in cursos_pedidos:
            cursos_con_puntajes.append([curso_pedido, puntos_por_curso])

        redistribucion_finalizada = False

        while not redistribucion_finalizada:
            display_cursos_con_puntos = '\n    N#    CURSO-SECCION        PUNTOS ASIGNADOS\n'
            for c in range(len(cursos_con_puntajes)):
                display_cursos_con_puntos += '   ({0}):   {1}-{2}    ->   {3} puntos\n'.format(
                    c + 1,
                    cursos_con_puntajes[c][0].sigla,
                    cursos_con_puntajes[c][0].seccion,
                    cursos_con_puntajes[c][1])
            print(display_cursos_con_puntos)

            curso_redistribucion = input("Ingrese el N# de ramo al que quiere redistribuirle puntaje \
[ingrese 0 para finalizar redistribucion]: ")
            if curso_redistribucion == '0':
                redistribucion_finalizada = True
            es_numero = (curso_redistribucion.split("0"))[-1].isdigit()
            if es_numero:
                n_opcion = int((curso_redistribucion.split("0"))[-1])
                if 1 <= n_opcion <= n_cursos_pedidos:
                    puntaje_variado = input("Ingrese cuantos puntos quiere redistribuirle al curso \
[ej: 300, -450]: ")
                    if puntaje_variado:
                        if puntaje_variado[0].isdigit() or ord(puntaje_variado[0]) == 45:
                            if puntaje_variado[1:].isdigit():
                                puntaje_variado = int(puntaje_variado)
                                x_puntos = puntaje_variado / (n_cursos_pedidos - 1)
                                negatividad = False
                                if cursos_con_puntajes[n_opcion - 1][1] + puntaje_variado < 0:
                                    negatividad = True
                                for k in range(len(cursos_con_puntajes)):
                                    if k != (n_opcion - 1):
                                        if (cursos_con_puntajes[k][1] - x_puntos) < 0:
                                            negatividad = True

                                if not negatividad:
                                    if (abs(puntaje_variado) + puntos_redistribuidos) <= 1000:
                                        if int(cursos_con_puntajes[n_opcion - 1][0].creditos) + \
                                                creditos_redistribuidos <= 45:
                                            creditos_redistribuidos += int(cursos_con_puntajes[n_opcion - 1][0].creditos)
                                            puntos_redistribuidos += abs(puntaje_variado)
                                            cursos_con_puntajes[n_opcion - 1][1] += puntaje_variado
                                            for j in range(len(cursos_con_puntajes)):
                                                if j != (n_opcion - 1):
                                                    cursos_con_puntajes[j][1] -= x_puntos
                                        else:
                                            print("\n --- ERROR: Solo puede redistribuir puntos a \
    maximo 45 creditos ---\n")

                                    else:
                                        print("\n --- ERROR: Excede el maximo de 1000 puntos de redistribucion ---\n")
                                else:
                                    print("\n --- ERROR: La distribucion de puntos de los cursos \
    quedaria negativa ---\n")

        print("\n--- FIN REDISTRIBUCION DE PUNTOS DE LOS RAMOS PEDIDOS ---\n")
        print("\n--- Si desea hacer cambios debe volver a empezar la solicitud de ramos ---\n")

        return cursos_con_puntajes


    else:
        print("\n--- ERROR: Debe tener mas de un curso pedido para redistribuir puntajes y \
acceder a pedir sus ramos ---\n")
