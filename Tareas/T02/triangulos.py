from ListaLigada import ListaLigada


def ciclos_triangulares(arcos):
    ids_visitados = ListaLigada()
    arcos_totales = len(arcos)
    for a in range(len(arcos)):
        porcentaje = round((a / arcos_totales) * 100, 2)
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
                esta = False
                for aa in range(len(arcos_nodo_c)):
                    if arcos_nodo_c[aa] == id_nodo_a:
                        esta = True
                if esta:
                    mant = ListaLigada()
                    mant.append(id_nodo_a)
                    mant.append(id_nodo_b)
                    mant.append(id_nodo_c)
                    yield mant
        ids_visitados.append(id_nodo_a)
