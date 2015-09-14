from ListaLigada import ListaLigada


def cargar_padres(hacker):
    for p in range(len(hacker.red_bummer.puertos)):
        id_padre = hacker.red_bummer.puertos[p].ide
        for c in range(len(hacker.red_bummer.puertos[p].conexiones)):
            for d in range(len(hacker.red_bummer.puertos[p].conexiones[c].puertos_destino)):
                id_destino = hacker.red_bummer.puertos[p].conexiones[c].puertos_destino[d]
                par = ListaLigada()
                par.append(id_padre)
                par.append(id_destino)
                hacker.pares_padre_destino.append(par)
