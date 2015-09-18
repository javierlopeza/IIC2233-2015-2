from clases.ListaLigada import ListaLigada


def pares_doble_sentido(pares_padre_destino):
    pares_bi = ListaLigada()
    pares_totales = len(pares_padre_destino)
    for i in range(len(pares_padre_destino)):
        porcentaje = round((i/pares_totales)*100, 2)
        print(" ---> Porcentaje Revisado: {0}%".format(porcentaje), end="\r")
        a1 = pares_padre_destino[i][0]
        a2 = pares_padre_destino[i][1]
        for j in range(len(pares_padre_destino)):
            b1 = pares_padre_destino[j][0]
            b2 = pares_padre_destino[j][1]
            if a1 == b2 and a2 == b1:
                continuar = True
                for pb in range(len(pares_bi)):
                    if pares_bi[pb][0] == a2 and pares_bi[pb][1] == a1:
                        continuar = False
                        break
                    elif pares_bi[pb][0] == a1 and pares_bi[pb][1] == a2:
                        continuar = False
                        break
                if continuar:
                    nuevo_par_bi = ListaLigada()
                    nuevo_par_bi.append(a1)
                    nuevo_par_bi.append(a2)
                    pares_bi.append(nuevo_par_bi)
    return pares_bi
