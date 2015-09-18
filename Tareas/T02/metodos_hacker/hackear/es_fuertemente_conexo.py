from metodos_hacker.hackear.dfs import dfs


def es_fuertemente_conexo(arcos):
    total_puertos = len(arcos)
    for g in range(len(arcos)):
        visitados = len(dfs(arcos, arcos[g][0]))
        if total_puertos != visitados:
            return False
    return True

