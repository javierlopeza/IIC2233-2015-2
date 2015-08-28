def tiene_permiso_especial(menu_alumno, curso):
    if curso in menu_alumno.alumno_in.permisos_especiales:
        return True
    else:
        return False
