def hora_valida(hora):
    if len(hora) == 5 and hora[2] == ":":
        if 48 <= ord(hora[0]) <= 50:
            if 48 <= ord(hora[1]) <= 57:
                if 48 <= ord(hora[3]) <= 53:
                    if 48 <= ord(hora[4]) <= 57:
                        return True
    return False