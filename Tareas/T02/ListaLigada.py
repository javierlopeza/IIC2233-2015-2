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

    def __len__(self):
        """ Retorna la cantidad de nodos existentes.
        """
        nodo = self.cabeza
        largo = 0
        while nodo:
            largo += 1
            nodo = nodo.siguiente
        return largo

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

'''
l = ListaLigada()
for n in range(10):
    l.append(n)
print('Lista l:', l)
print('Largo:', len(l))
print('Elemento en el indice 3:', l[3])
'''
