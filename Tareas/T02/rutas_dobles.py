from ListaLigada import ListaLigada


def son_iguales(lista1, lista2):
    if lista1 and lista2:
        if len(lista1) == len(lista2):
            contador = len(lista1)
            for l in range(len(lista1)):
                if lista1[l] == lista2[l]:
                    contador -= 1
            if contador == 0:
                return True
            return False


def es_sublista(lista_sub, lista_big):
    if lista_big:
        for m in range(len(lista_big)):
            if lista_sub[0] == lista_big[m]:
                if (len(lista_sub) - 1) <= (len(lista_big) - m - 1):
                    contador = len(lista_sub)
                    for n in range(len(lista_sub)):
                        if lista_sub[n] == lista_big[m + n]:
                            contador -= 1
                    if contador == 0:
                        if len(lista_big) == len(lista_sub):
                            return False
                        return True
    return False


def rutas_doble_sentido(pares_bi):
    rutas_bi = ListaLigada()
    for p0 in range(len(pares_bi)):
        a = pares_bi[p0][0]
        b = pares_bi[p0][1]
        ruta_par = ListaLigada()
        ruta_par.append(a)
        ruta_par.append(b)
        rutas_bi.append(ruta_par)

    for p1 in range(len(pares_bi)):
        a = pares_bi[p1][0]
        b1 = pares_bi[p1][1]
        for r in range(len(rutas_bi)):
            b2 = rutas_bi[r][0]
            c = rutas_bi[r][len(rutas_bi[r]) - 1]
            if b1 == b2:
                nueva_ruta_bi = ListaLigada()
                nueva_ruta_bi.append(a)
                for p in range(len(rutas_bi[r])):
                    nueva_ruta_bi.append(rutas_bi[r][p])
                rutas_bi.append(nueva_ruta_bi)
            elif a == c:
                nueva_ruta_bi = ListaLigada()
                for p in range(len(rutas_bi[r])):
                    nueva_ruta_bi.append(rutas_bi[r][p])
                nueva_ruta_bi.append(b1)
                rutas_bi.append(nueva_ruta_bi)

    for r1 in range(len(rutas_bi)):
        ruta1 = rutas_bi[r1]
        for r2 in range(len(rutas_bi)):
            ruta2 = rutas_bi[r2]
            if es_sublista(ruta1, ruta2):
                rutas_bi[r1] = None

    for r1 in range(len(rutas_bi)):
        ruta1 = rutas_bi[r1]
        for r2 in range(len(rutas_bi)):
            ruta2 = rutas_bi[r2]
            if son_iguales(ruta1, ruta2) and r1 != r2:
                rutas_bi[r1] = None
                break

    return rutas_bi
