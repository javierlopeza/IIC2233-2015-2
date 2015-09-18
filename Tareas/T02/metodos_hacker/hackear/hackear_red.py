from metodos_hacker.hackear.es_fuertemente_conexo import es_fuertemente_conexo


def hackear_red(arcos):
    """
    Voy a ir conexion a conexion en la red,
    intentando ver si al quitar la conexion
    queda igual fuertemente conexo.
    Si queda fuertemente conexo luego de quitarla,
    la quito definitivamente.
    """
    total_arcos = len(arcos)
    for a in range(total_arcos):
        porcentaje = round((a / total_arcos) * 100, 2)
        print('Porcentaje Hackeado: {0}%'.format(porcentaje), end='\r')
        for conexion in arcos[a][1]:
            arcos[a][1].remove(conexion)
            if not es_fuertemente_conexo(arcos):
                arcos[a][1].append(conexion)
    return arcos


grafo = [
    [0, [2, 3]],
    [1, [0, 6]],
    [2, [1, 5]],
    [3, [5, 10]],
    [4, [1, 2, 7]],
    [5, [0, 4]],
    [6, [8, 9]],
    [7, [1, 6]],
    [8, [3, 5]],
    [9, [7, 10]],
    [10, [5, 8]]
]

print(hackear_red(grafo))

mini_red = [
    [0, [3]],
    [1, [6]],
    [2, [5]],
    [3, [10]],
    [4, [2, 7]],
    [5, [4, 0]],
    [6, [9]],
    [7, [6, 1]],
    [8, [5]],
    [9, [10]],
    [10, [8]]
]
