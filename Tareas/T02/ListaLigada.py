class ListaLigada:
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
        if str(item).isdigit():
            if int(item) < self.largo:
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

    def contiene(self, valor):
        """ Retorna True si la lista contiene valor.
        """
        for a in range(self.largo):
            if getattr(self, 'e{0}'.format(a)) == valor:
                return True
        return False

    def __repr__(self):
        """ Imprime la lista ligada de manera simple y comprensible.
        """
        rep = ''
        for a in range(self.largo):
            rep += '{0} >>> '.format(getattr(self, 'e{0}'.format(a)))
        rep = rep[:-5]
        return rep
