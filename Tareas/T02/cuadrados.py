from ListaLigada import ListaLigada


def ciclos_cuadrados(arcos):
    ids_visitados = ListaLigada()
    arcos_totales = len(arcos)
    for a in range(len(arcos)):
        porcentaje = round((a/arcos_totales)*100, 2)
        print(" ---> Porcentaje Revisado: {0}%".format(porcentaje), end="\r")
        id_nodo_a = arcos[a][0]
        for b in range(len(arcos[a][1])):
            id_nodo_b = arcos[a][1][b]
            continuar = False
            for bb in range(len(ids_visitados)):
                if ids_visitados[bb] == id_nodo_b:
                    continuar = True
            if continuar:
                continue
            for nb in range(len(arcos)):
                if arcos[nb][0] == id_nodo_b:
                    arcos_nodo_b = arcos[nb][1]
                    break
            for c in range(len(arcos_nodo_b)):
                id_nodo_c = arcos_nodo_b[c]
                continuar1 = False
                for cc in range(len(ids_visitados)):
                    if ids_visitados[cc] == id_nodo_c:
                        continuar1 = True
                if continuar1:
                    continue
                for nc in range(len(arcos)):
                    if arcos[nc][0] == id_nodo_c:
                        arcos_nodo_c = arcos[nc][1]
                        break
                for d in range(len(arcos_nodo_c)):
                    id_nodo_d = arcos_nodo_c[d]
                    for nd in range(len(arcos)):
                        if arcos[nd][0] == id_nodo_d:
                            arcos_nodo_d = arcos[nd][1]
                            break
                    esta = False
                    for aa in range(len(arcos_nodo_d)):
                        if arcos_nodo_d[aa] == id_nodo_a:
                            esta = True
                    if esta:
                        mant = ListaLigada()
                        mant.append(id_nodo_a)
                        mant.append(id_nodo_b)
                        mant.append(id_nodo_c)
                        mant.append(id_nodo_d)
                        yield mant
        ids_visitados.append(id_nodo_a)


def eliminar_equivalentes(lista_ciclos):
    for c1 in range(len(lista_ciclos)):
        ciclo1 = lista_ciclos[c1]
        for c2 in range(len(lista_ciclos)):
            ciclo2 = lista_ciclos[c2]
            if ciclo1 and ciclo2:
                if len(ciclo1) == len(ciclo2) and c1 != c2:
                    contador = len(ciclo1)
                    for p1 in range(len(ciclo1)):
                        puerto1 = ciclo1[p1]
                        for p2 in range(len(ciclo2)):
                            puerto2 = ciclo2[p2]
                            if puerto1 == puerto2:
                                contador -= 1
                    if contador == 0:
                        # Eran equivalentes:
                        lista_ciclos[c1] = None
    return lista_ciclos


def eliminar_none(lista_ciclos):
    lista_limpia = ListaLigada()
    for c in range(len(lista_ciclos)):
        if lista_ciclos[c]:
            lista_limpia.append(lista_ciclos[c])
    return lista_limpia


def cuadrados_limpios(arcos):
    ciclos = ciclos_cuadrados(arcos)
    lista_ciclos = ListaLigada()
    for c in ciclos:
        lista_ciclos.append(c)
    # Procedo a eliminar los ciclos equivalentes.
    lista_ciclos = eliminar_equivalentes(lista_ciclos)
    # Procedo a limpiar los None elements.
    lista_ciclos = eliminar_none(lista_ciclos)
    return lista_ciclos
