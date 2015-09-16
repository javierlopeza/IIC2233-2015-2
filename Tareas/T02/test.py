# Ir conexion a conexion, y viendo si al eliminar dicha conexion deja de ser fuertemente conexo.
# Si no deja de serlo, borro la conexion.

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

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            extender = graph[vertex]
            for e in extender:
                for v in visited:
                    if e == v:
                        extender.remove(e)
            stack.extend(extender)
    return visited

from ListaLigada import ListaLigada


def dfs2(graph, start):
    visited = ListaLigada()
    stack = ListaLigada()
    stack.append(start)
    while len(stack) != 0:
        vertex = stack.pop()
        if not visited.contiene(vertex):
            visited.append(vertex)
            for g in range(len(graph)):
                if graph[g][0] == vertex:
                    extender = graph[g][1]
                    break
            borrar = ListaLigada()
            for e in range(len(extender)):
                for v in range(len(visited)):
                    if extender[e] == visited[v]:
                        borrar.append(extender[e])
            for b in range(len(borrar)):
                extender.remove(borrar[b])
            stack.extend(extender)
    return visited

graph2 = [['A', ['B', 'C']],
         ['B', ['A', 'D', 'E']],
         ['C', ['A', 'F']],
         ['D', ['B']],
         ['E', ['B', 'F']],
         ['F', ['C', 'E']]]

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

print(dfs(graph, 'B'))
print(len(dfs2(graph2, 'B')))