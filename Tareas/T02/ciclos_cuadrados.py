from ListaLigada import ListaLigada


def cuad_falso(cuad):
    a1 = cuad[0]
    a2 = cuad[1]
    a3 = cuad[2]
    a4 = cuad[3]
    if a1 == a2 \
            or a1 == a3 \
            or a1 == a4 \
            or a2 == a3 \
            or a2 == a4 \
            or a3 == a4:
        return True


def cuad_igual(cuad1, cuad2):
    a1 = cuad1[0]
    a2 = cuad1[1]
    a3 = cuad1[2]
    a4 = cuad1[3]
    b1 = cuad2[0]
    b2 = cuad2[1]
    b3 = cuad2[2]
    b4 = cuad2[3]
    if a1 == b4 and a2 == b1 and a3 == b2 and a4 == b3:
        return True
    if a1 == b3 and a2 == b4 and a3 == b1 and a4 == b2:
        return True
    if a1 == b2 and a2 == b3 and a3 == b4 and a4 == b1:
        return True
    if a1 == b2 and a2 == b3 and a3 == b4 and a4 == b1:
        return True
    return False


def ciclos_cuadrados(pares_padre_destino):
    ciclos_cuad = ListaLigada()
    for p1 in range(len(pares_padre_destino)):
        a1 = pares_padre_destino[p1][0]
        a2 = pares_padre_destino[p1][1]
        for p2 in range(len(pares_padre_destino)):
            b1 = pares_padre_destino[p2][0]
            b2 = pares_padre_destino[p2][1]
            for p3 in range(len(pares_padre_destino)):
                c1 = pares_padre_destino[p3][0]
                c2 = pares_padre_destino[p3][1]
                for p4 in range(len(pares_padre_destino)):
                    d1 = pares_padre_destino[p4][0]
                    d2 = pares_padre_destino[p4][1]
                    if a2 == b1 and b2 == c1 and c2 == d1 and d2 == a1:
                        nuevo_ciclo_cuad = ListaLigada()
                        nuevo_ciclo_cuad.append(a1)
                        nuevo_ciclo_cuad.append(b1)
                        nuevo_ciclo_cuad.append(c1)
                        nuevo_ciclo_cuad.append(d1)
                        ciclos_cuad.append(nuevo_ciclo_cuad)

    for c1 in range(len(ciclos_cuad)):
        for c2 in range(len(ciclos_cuad)):
            if c1 != c2:
                if ciclos_cuad[c1] and ciclos_cuad[c2]:
                    if cuad_igual(ciclos_cuad[c1], ciclos_cuad[c2]):
                        ciclos_cuad[c1] = None

    for c in range(len(ciclos_cuad)):
        if ciclos_cuad[c]:
            if cuad_falso(ciclos_cuad[c]):
                ciclos_cuad[c] = None

    return ciclos_cuad
