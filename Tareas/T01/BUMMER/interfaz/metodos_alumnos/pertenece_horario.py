def pertenece_horario(tiempo_actual, horario_inscripcion):
    tiempo_actual = tiempo_actual.split(':')
    hora_actual = int(tiempo_actual[0])
    minutos_actual = int(tiempo_actual[1])

    tiempo_min = horario_inscripcion[0].split(':')
    hora_min = int(tiempo_min[0])

    tiempo_max = horario_inscripcion[1].split(':')
    hora_max = int(tiempo_max[0])

    if hora_min < hora_actual < hora_max:
        return True
    elif hora_min == hora_actual:
        if minutos_actual >= 30:
            return True
    elif hora_max == hora_actual:
        if minutos_actual <= 30:
            return True
    return False
