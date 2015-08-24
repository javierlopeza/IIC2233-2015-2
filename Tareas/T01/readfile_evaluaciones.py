from clases import Evaluacion


def cargar_evaluaciones(lista_cursos):
    evaluaciones = []
    evaluaciones_file = open("evaluaciones.txt").readlines()
    for i in range(len(evaluaciones_file)):
        if evaluaciones_file[i] == "  {\n":
            sigla_eval = evaluaciones_file[i + 1][14:-3]
            tipo_eval = evaluaciones_file[i + 2][13:-3]
            seccion_eval = evaluaciones_file[i + 3][11:-2]
            fecha_eval = evaluaciones_file[i + 4][14:-2]
            dia_eval = fecha_eval.split(" - ")[0]
            hora_eval = fecha_eval.split(" - ")[1]
            if hora_eval[-1] == '"':
                hora_eval = hora_eval[:-1]
            nueva_evaluacion = Evaluacion(
                nombre=tipo_eval,
                hora=hora_eval,
                dia=dia_eval,
                curso=sigla_eval,
                seccion=seccion_eval
                )
            evaluaciones.append(nueva_evaluacion)

# --------------------- ESTA FALLANDO AGREGARLE LAS EVALUACIONES A LOS CURSOS
    '''
    for evaluacion in evaluaciones:
        sigla_eval = evaluacion.curso
        seccion_eval = evaluacion.seccion
        for c in lista_cursos:
            sigla_curso = c.sigla
            seccion_curso = c.seccion
            if (sigla_eval == sigla_curso) and (seccion_eval == seccion_curso):
                (c.evaluaciones).append(evaluacion)


    for c in lista_cursos:
        print(c.evaluaciones)
                '''
    return lista_cursos, len(evaluaciones)