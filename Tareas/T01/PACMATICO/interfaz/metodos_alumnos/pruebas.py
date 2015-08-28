puntaje_variado = "-230"

if puntaje_variado[0].isdigit() or ord(puntaje_variado[0]) == 45:
    if puntaje_variado[1:].isdigit():
        puntaje_variado = int(puntaje_variado)
        print(puntaje_variado)