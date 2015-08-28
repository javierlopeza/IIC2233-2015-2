def aprobo_curso(menu_alumno, sigla_curso):
    if sigla_curso[-2] == "c":
        for curso_tomado in menu_alumno.alumno_in.cursos_por_tomar:
            if sigla_curso[:-3] == curso_tomado.sigla:
                return True
        else:
            return False

    else:
        if sigla_curso in menu_alumno.alumno_in.cursos_aprobados:
            return True
        else:
            return False
