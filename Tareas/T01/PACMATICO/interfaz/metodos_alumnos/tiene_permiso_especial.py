def tiene_permiso_especial(alumno, curso):
    if curso in alumno.permisos_especiales:
        return True
    else:
        return False
