from ListaLigada import ListaLigada


def trio_igual(trio1, trio2):
    a1 = trio1[0]
    a2 = trio1[1]
    a3 = trio1[2]
    b1 = trio2[0]
    b2 = trio2[1]
    b3 = trio2[2]
    if a1 == b3 and a2 == b1 and a3 == b2:
        return True
    if a1 == b2 and a2 == b3 and a3 == b1:
        return True
    return False


def ciclos_triangulares(pares_padre_destino):
    ciclos_tri = ListaLigada()
    for p1 in range(len(pares_padre_destino)):
        a1 = pares_padre_destino[p1][0]
        a2 = pares_padre_destino[p1][1]
        for p2 in range(len(pares_padre_destino)):
            b1 = pares_padre_destino[p2][0]
            b2 = pares_padre_destino[p2][1]
            for p3 in range(len(pares_padre_destino)):
                c1 = pares_padre_destino[p3][0]
                c2 = pares_padre_destino[p3][1]
                if a2 == b1 and b2 == c1 and c2 == a1:
                    nuevo_ciclo_tri = ListaLigada()
                    nuevo_ciclo_tri.append(a1)
                    nuevo_ciclo_tri.append(b1)
                    nuevo_ciclo_tri.append(c1)
                    ciclos_tri.append(nuevo_ciclo_tri)
    for c1 in range(len(ciclos_tri)):
        for c2 in range(len(ciclos_tri)):
            if c1 != c2:
                if ciclos_tri[c1] and ciclos_tri[c2]:
                    if trio_igual(ciclos_tri[c1], ciclos_tri[c2]):
                        ciclos_tri[c1] = None
    return ciclos_tri
