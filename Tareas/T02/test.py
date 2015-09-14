class Nodo:
    """ Clase que construye una estructura simulando un nodo
    para ser agregado a una lista ligada.
    """

    def __init__(self, valor=None):
        self.siguiente = None
        self.valor = valor


class ListaLigada:
    """ Clase que construye una estructura simulando una lista ligada.
    """

    def __init__(self):
        """ Se inicializa sin cabeza y sin cola.
        """
        self.cola = None
        self.cabeza = None
        self.largo = 0

    def append(self, valor):
        """ Agrega el valor en un nuevo nodo despues
        de la cola de la lista ligada (o en la cabeza
        si esta recien instanciada).
        """
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            self.cola.siguiente = Nodo(valor)
            self.cola = self.cola.siguiente
        self.largo += 1

    def __getitem__(self, item):
        """ Retorna el elemento de indice item.
        Se usa igual que las listas de Python,
        indicando el indice entre corchetes: self[i]
        """
        nodo = self.cabeza
        for n in range(item):
            if nodo:
                nodo = nodo.siguiente
        if not nodo:
            return "posicion no encontrada"
        else:
            return nodo.valor

    def __setitem__(self, key, value):
        """ Permite realizar item assignment en la lista.
        """
        nodo = self.cabeza
        for n in range(key):
            if nodo:
                nodo = nodo.siguiente
        nodo.valor = value

    def __len__(self):
        """ Retorna la cantidad de nodos existentes.
        """
        return self.largo

    def has(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == valor:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def __repr__(self):
        """ Imprime la lista ligada de manera simple y comprensible.
        """
        rep = ''
        nodo_actual = self.cabeza
        while nodo_actual:
            rep += '{0} >>> '.format(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        rep = rep[:-5]
        return rep


class Perro:
    def __init__(self, nombre):
        self.nombre = nombre


'''
lista = ListaLigada()
chubi = Perro("Chubiii")
for n in range(6):
    lista.append(1)
    lista.append(0)

print('Lista:', lista)
print('Largo:', len(lista))

lista = [1,1,0,1,1]
print(lista.index(min(lista)))

for i in range(1):
    print(True)

import sys

print(sys.getsizeof(lista))

print("hola {}".format(2))

graph = [['A', ['B', 'C']],
         ['B', ['C', 'D']],
         ['C', ['D']],
         ['D', ['C']],
         ['E', ['F']],
         ['F', ['C']]]

def find_path(graph, start, end, path=[]):
    path.append(start)
    if start == end:
        return path
    contador = len(graph)
    graph_start = None
    for n in range(len(graph)):
        if not start == graph[n][0]:
            contador -= 1
        if graph[n][0] == start:
            graph_start = graph[n][1]
    if contador == 0:
        return None
    for node in graph_start:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

print(find_path(graph, 'A', 'D'))


graph = [['A', ['B', 'C']],
         ['B', ['C', 'D']],
         ['C', ['D']],
         ['D', ['C']],
         ['E', ['F']],
         ['F', ['C']]]

arcos = ListaLigada()

a = ListaLigada()
a.append(1)
aa = ListaLigada()
aa.append(2)
aa.append(3)
a.append(aa)

arcos.append(a)

a = ListaLigada()
a.append(2)
aa = ListaLigada()
aa.append(3)
aa.append(4)
a.append(aa)

arcos.append(a)

a = ListaLigada()
a.append(3)
aa = ListaLigada()
aa.append(4)
a.append(aa)

arcos.append(a)

a = ListaLigada()
a.append(4)
aa = ListaLigada()
aa.append(3)
a.append(aa)

arcos.append(a)

a = ListaLigada()
a.append(5)
aa = ListaLigada()
aa.append(6)
a.append(aa)

arcos.append(a)

a = ListaLigada()
a.append(6)
aa = ListaLigada()
aa.append(3)
a.append(aa)

arcos.append(a)

print(encontrar_camino(arcos, , 4))
'''