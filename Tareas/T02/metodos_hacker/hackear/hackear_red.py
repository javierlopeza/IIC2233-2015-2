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
