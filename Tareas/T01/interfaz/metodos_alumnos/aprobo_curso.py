def aprobo_curso(menu_alumno, sigla_curso):
    if sigla_curso in menu_alumno.alumno_in.cursos_aprobados:
        return True
    else:
        return False
