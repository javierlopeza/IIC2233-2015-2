from ListaLigada import ListaLigada


def encontrar_caminos(arcos, inicio, final, camino=ListaLigada()):
    lista_inicio = ListaLigada()
    lista_inicio.append(inicio)
    camino = camino + lista_inicio

    if inicio == final:
        lista_camino = ListaLigada()
        lista_camino.append(camino)
        print("NUEVO CAMINO :)")
        return lista_camino

    contador = len(arcos)
    arcos_sig = None
    for n in range(len(arcos)):
        if arcos[n][0] != inicio:
            contador -= 1
        if arcos[n][0] == inicio:
            arcos_sig = arcos[n][1]
    if contador == 0:
        return []

    caminos = ListaLigada()
    for n in range(len(arcos_sig)):
        in_camino = False
        for p in range(len(camino)):
            if arcos_sig[n] == camino[p]:
                in_camino = True
                break
        if not in_camino:
            nuevos_caminos = encontrar_caminos(arcos,
                                               arcos_sig[n],
                                               final, camino)
            for c in range(len(nuevos_caminos)):
                caminos.append(nuevos_caminos[c])
    return caminos
