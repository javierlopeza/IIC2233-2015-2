from clases.ListaLigada import ListaLigada


def cargar_padres(hacker):
    for p in range(len(hacker.red_bummer.puertos)):
        id_padre = hacker.red_bummer.puertos[p].ide
        ya_esta = False
        for a in range(len(hacker.red_bummer.arcos)):
            if hacker.red_bummer.arcos[a][0] == id_padre:
                ya_esta = True
        if not ya_esta:
            arcos_s = ListaLigada()
            destinos = ListaLigada()
            arcos_s.append(id_padre)
        for c in range(len(hacker.red_bummer.puertos[p].conexiones)):
            for d in range(len(
                    hacker.red_bummer.
                            puertos[p].
                            conexiones[c].
                            puertos_destino)):
                id_destino = \
                    hacker.red_bummer.puertos[p].conexiones[c].puertos_destino[d]
                par = ListaLigada()
                par.append(id_padre)
                par.append(id_destino)
                hacker.pares_padre_destino.append(par)
                if not ya_esta:
                    destinos.append(id_destino)
        if not ya_esta:
            arcos_s.append(destinos)
            hacker.red_bummer.arcos.append(arcos_s)
