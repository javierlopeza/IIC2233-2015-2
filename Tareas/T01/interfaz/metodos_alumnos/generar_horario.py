def generar_horario(cursos_por_tomar):
    horario_base = """
    ___________________________________________________________________________________________________
   |    HORARIO    |    LUNES    |    MARTES   |  MIERCOLES  |    JUEVES   |   VIERNES   |    SABADO   |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
   | 08:30 - 09:50 |             |             |             |             |             |             |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
   | 10:00 - 11:20 |             |             |             |             |             |             |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
   | 11:30 - 12:50 |             |             |             |             |             |             |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
   | 14:00 - 15:20 |             |             |             |             |             |             |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
   | 15:30 - 16:50 |             |             |             |             |             |             |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
   | 17:00 - 18:20 |             |             |             |             |             |             |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
   | 18:30 - 19:50 |             |             |             |             |             |             |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
   | 20:00 - 21:20 |             |             |             |             |             |             |
   |_______________|_____________|_____________|_____________|_____________|_____________|_____________|
                       """

    horario_listado = [[[], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], []]]

    extra_tope_horario = "|\n   |               |             |             \
|             |             |             |             |"

    repeticiones_dia = [[0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]]

    repeticiones_individuales = [[0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0]]

    for curso in cursos_por_tomar:
        if curso.hora_cat != ("(Por Asignar)" and "---"):
            dias = curso.hora_cat.split(":")[0].split("-")
            modulos = curso.hora_cat.split(":")[1].split(",")
            for dia in dias:
                for modulo in modulos:
                    if dia == "L":
                        d = 0
                    if dia == "M":
                        d = 1
                    if dia == "W":
                        d = 2
                    if dia == "J":
                        d = 3
                    if dia == "V":
                        d = 4
                    if dia == "S":
                        d = 5
                    if modulo == "1":
                        m = 0
                    if modulo == "2":
                        m = 1
                    if modulo == "3":
                        m = 2
                    if modulo == "4":
                        m = 3
                    if modulo == "5":
                        m = 4
                    if modulo == "6":
                        m = 5
                    if modulo == "7":
                        m = 6
                    if modulo == "8":
                        m = 7

                    h = 337 + (210 * m) + (14 * d)
                    hh = 418 + (210 * m)

                    horario_listado[d][m].append(curso)

                    repeticiones_in = repeticiones_individuales[d][m]

                    extra_repeticiones_in = 105 * repeticiones_in

                    repeticiones_maximas = 0
                    es_max = True
                    for i in range(len(repeticiones_dia)):
                        repeticiones_dia_n = 0
                        for j in range(len(repeticiones_dia[i])):
                            if j < m:
                                repeticiones_dia_n += repeticiones_dia[i][j]
                            if j == m:
                                if (repeticiones_dia[d][m] <
                                        repeticiones_dia[i][j]):
                                    if d != i:
                                        es_max = False
                        if repeticiones_dia_n > repeticiones_maximas:
                            repeticiones_maximas = repeticiones_dia_n

                    extra_modulos_anteriores_dias = \
                        (repeticiones_maximas * 105)

                    if repeticiones_individuales[d][m] == 0:
                        extra = extra_modulos_anteriores_dias
                        h += extra
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_individuales[d][m] += 1

                    elif not es_max:
                        extra = (extra_repeticiones_in
                                 + extra_modulos_anteriores_dias)
                        h += extra
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_individuales[d][m] += 1
                        repeticiones_dia[d][m] += 1

                    elif es_max:
                        hh += (extra_repeticiones_in
                               + extra_modulos_anteriores_dias
                               - 105)
                        horario_base = "{0}{1}{2}".format(
                            horario_base[:hh],
                            extra_tope_horario,
                            horario_base[(hh + 1):])
                        h += (extra_repeticiones_in
                              + extra_modulos_anteriores_dias)
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_dia[d][m] += 1
                        repeticiones_individuales[d][m] += 1

        if curso.hora_ayud != ("(Por Asignar)" and "---"):
            dias = curso.hora_ayud.split(":")[0].split("-")
            modulos = curso.hora_ayud.split(":")[1].split(",")
            for dia in dias:
                for modulo in modulos:
                    if dia == "L":
                        d = 0
                    if dia == "M":
                        d = 1
                    if dia == "W":
                        d = 2
                    if dia == "J":
                        d = 3
                    if dia == "V":
                        d = 4
                    if dia == "S":
                        d = 5
                    if modulo == "1":
                        m = 0
                    if modulo == "2":
                        m = 1
                    if modulo == "3":
                        m = 2
                    if modulo == "4":
                        m = 3
                    if modulo == "5":
                        m = 4
                    if modulo == "6":
                        m = 5
                    if modulo == "7":
                        m = 6
                    if modulo == "8":
                        m = 7

                    h = 337 + (210 * m) + (14 * d)
                    hh = 418 + (210 * m)

                    horario_listado[d][m].append(curso)

                    repeticiones_in = repeticiones_individuales[d][m]

                    extra_repeticiones_in = 105 * repeticiones_in

                    repeticiones_maximas = 0
                    es_max = True
                    for i in range(len(repeticiones_dia)):
                        repeticiones_dia_n = 0
                        for j in range(len(repeticiones_dia[i])):
                            if j < m:
                                repeticiones_dia_n += repeticiones_dia[i][j]
                            if j == m:
                                if repeticiones_dia[d][m] \
                                        < repeticiones_dia[i][j]:
                                    if d != i:
                                        es_max = False
                        if repeticiones_dia_n > repeticiones_maximas:
                            repeticiones_maximas = repeticiones_dia_n

                    extra_modulos_anteriores_dias = \
                        (repeticiones_maximas * 105)

                    if repeticiones_individuales[d][m] == 0:
                        extra = extra_modulos_anteriores_dias
                        h += extra
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_individuales[d][m] += 1

                    elif not es_max:
                        extra = (extra_repeticiones_in
                                 + extra_modulos_anteriores_dias)
                        h += extra
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_individuales[d][m] += 1
                        repeticiones_dia[d][m] += 1

                    elif es_max:
                        hh += (extra_repeticiones_in
                               + extra_modulos_anteriores_dias - 105)
                        horario_base = "{0}{1}{2}".format(
                            horario_base[:hh],
                            extra_tope_horario,
                            horario_base[(hh + 1):])
                        h += (extra_repeticiones_in
                              + extra_modulos_anteriores_dias)
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_dia[d][m] += 1
                        repeticiones_individuales[d][m] += 1

        if curso.hora_lab != ("(Por Asignar)" and "---"):
            dias = curso.hora_lab.split(":")[0].split("-")
            modulos = curso.hora_lab.split(":")[1].split(",")
            for dia in dias:
                for modulo in modulos:
                    if dia == "L":
                        d = 0
                    if dia == "M":
                        d = 1
                    if dia == "W":
                        d = 2
                    if dia == "J":
                        d = 3
                    if dia == "V":
                        d = 4
                    if dia == "S":
                        d = 5
                    if modulo == "1":
                        m = 0
                    if modulo == "2":
                        m = 1
                    if modulo == "3":
                        m = 2
                    if modulo == "4":
                        m = 3
                    if modulo == "5":
                        m = 4
                    if modulo == "6":
                        m = 5
                    if modulo == "7":
                        m = 6
                    if modulo == "8":
                        m = 7

                    h = 337 + (210 * m) + (14 * d)
                    hh = 418 + (210 * m)

                    horario_listado[d][m].append(curso)

                    repeticiones_in = repeticiones_individuales[d][m]

                    extra_repeticiones_in = 105 * repeticiones_in

                    repeticiones_maximas = 0
                    es_max = True
                    for i in range(len(repeticiones_dia)):
                        repeticiones_dia_n = 0
                        for j in range(len(repeticiones_dia[i])):
                            if j < m:
                                repeticiones_dia_n += repeticiones_dia[i][j]
                            if j == m:
                                if repeticiones_dia[d][m] \
                                        < repeticiones_dia[i][j]:
                                    if d != i:
                                        es_max = False
                        if repeticiones_dia_n > repeticiones_maximas:
                            repeticiones_maximas = repeticiones_dia_n

                    extra_modulos_anteriores_dias = \
                        (repeticiones_maximas * 105)

                    if repeticiones_individuales[d][m] == 0:
                        extra = extra_modulos_anteriores_dias
                        h += extra
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_individuales[d][m] += 1

                    elif not es_max:
                        extra = (extra_repeticiones_in
                                 + extra_modulos_anteriores_dias)
                        h += extra
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_individuales[d][m] += 1
                        repeticiones_dia[d][m] += 1

                    elif es_max:
                        hh += (extra_repeticiones_in
                               + extra_modulos_anteriores_dias - 105)
                        horario_base = "{0}{1}{2}".format(
                            horario_base[:hh],
                            extra_tope_horario,
                            horario_base[(hh + 1):])
                        h += (extra_repeticiones_in
                              + extra_modulos_anteriores_dias)
                        horario_base = "{0}{1}-{2}{3}".format(
                            horario_base[:h],
                            str(curso.sigla),
                            str(curso.seccion),
                            horario_base[(h + 9):])
                        repeticiones_dia[d][m] += 1
                        repeticiones_individuales[d][m] += 1

    file_horario = open("horario.txt", "w")
    file_horario.write(horario_base)

    return horario_base, horario_listado
