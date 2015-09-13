class ListaLigadaATT:
    """ Clase que construye una estructura simulando una lista ligada.
    """

    def __init__(self):
        """ Se inicializa sin elementos.
        """
        self.e0 = None
        self.largo = 0

    def append(self, valor):
        """ Agrega el valor en un nuevo atributo de la lista.
        """
        setattr(self, 'e{0}'.format(self.largo), valor)
        self.largo += 1

    def __getitem__(self, item):
        """ Retorna el elemento de indice item.
        Se usa igual que las listas de Python,
        indicando el indice entre corchetes: self[i]
        """
        valor_item = getattr(self, 'e{0}'.format(item))
        return valor_item

    def __setitem__(self, key, value):
        """ Permite realizar item assignment en la lista.
        """
        setattr(self, 'e{0}'.format(key), value)

    def __len__(self):
        """ Retorna la cantidad de elementos existentes.
        """
        return self.largo

    def indice_min(self):
        """ Retorna el indice donde se encuentra el elemento de menor valor.
        """
        indice_menor = 0
        menor = getattr(self, 'e0')
        for a in range(self.largo):
            elemento_actual = getattr(self, 'e{0}'.format(a))
            if elemento_actual < menor:
                indice_menor = a
                menor = elemento_actual
        return indice_menor

    def __repr__(self):
        """ Imprime la lista ligada de manera simple y comprensible.
        """
        rep = ''
        for a in range(self.largo):
            rep += '{0} >>> '.format(getattr(self, 'e{0}'.format(a)))
        rep = rep[:-5]
        return rep