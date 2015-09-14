from ListaLigada import ListaLigada


def encontrar_camino(arcos, puerto_inicio, puerto_bummer, camino = ListaLigada()):
    camino.append(puerto_inicio)

    if puerto_inicio == puerto_bummer:
        return camino

    contador = len(arcos)
    inicio_arcos = None
    for n in range(len(arcos)):
        if not puerto_inicio == arcos[n][0]:
            contador -= 1
        if arcos[n][0] == puerto_inicio:
            inicio_arcos = arcos[n][1]
    if contador == 0:
        return None

    in_camino = False
    for p1 in range(len(inicio_arcos)):
        for p2 in range(len(camino)):
            if inicio_arcos[p1] == camino[p2]:
                in_camino = True
                break
        if not in_camino:
            nuevocamino = encontrar_camino(arcos, inicio_arcos[p1], puerto_bummer, camino)
            if nuevocamino: return nuevocamino
    return None

