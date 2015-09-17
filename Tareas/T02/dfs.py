from ListaLigada import ListaLigada
from copy import deepcopy


def dfs(arcos, start):
    grafo = deepcopy(arcos)
    visitados = ListaLigada()
    pila = ListaLigada()
    pila.append(start)
    while len(pila) != 0:
        vertice = pila.pop()
        if not visitados.contiene(vertice):
            visitados.append(vertice)
            for g in range(len(grafo)):
                if grafo[g][0] == vertice:
                    extender = grafo[g][1]
                    break
            borrar = ListaLigada()
            for e in range(len(extender)):
                for v in range(len(visitados)):
                    if extender[e] == visitados[v]:
                        borrar.append(extender[e])
            for b in range(len(borrar)):
                extender.remove(borrar[b])
            pila.extend(extender)
    return visitados
