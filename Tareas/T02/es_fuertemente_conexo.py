from dfs import dfs


def es_fuertemente_conexo(arcos):
    total_puertos = len(arcos)
    for g in range(len(arcos)):
        visitados = len(dfs(arcos, arcos[g][0]))
        if total_puertos != visitados:
            return False
    return True


grafo = [
    [0, [2, 3]],
    [1, [0, 6]],
    [2, [1, 5]],
    [3, [5, 10]],
    [4, [1, 2, 7]],
    [5, [0, 4]],
    [6, [8, 9]],
    [7, [1, 6]],
    [8, [3, 5]],
    [9, [7, 10]],
    [10, [5, 8]]
]

print(es_fuertemente_conexo(grafo))