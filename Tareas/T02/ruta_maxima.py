oo = float("infinity")


def ruta_maxima(puertos, rutas):
    indice_ruta_max = -1
    capacidad_ruta_max = -1
    for r in range(len(rutas)):
        capacidad_ruta = oo
        for p in range(len(rutas[r])):
            ide_puerto_ruta = rutas[r][p]
            for x in range(len(puertos)):
                if puertos[x].ide == ide_puerto_ruta:
                    capacidad_puerto = puertos[x].capacidad
                    if capacidad_puerto < capacidad_ruta:
                        capacidad_ruta = capacidad_puerto
        if capacidad_ruta > capacidad_ruta_max:
            capacidad_ruta_max = capacidad_ruta
            indice_ruta_max = r
        if capacidad_ruta == capacidad_ruta_max:
            if len(rutas[r]) < len(rutas[indice_ruta_max]):
                capacidad_ruta_max = capacidad_ruta
                indice_ruta_max = r
    return rutas[indice_ruta_max], capacidad_ruta_max
