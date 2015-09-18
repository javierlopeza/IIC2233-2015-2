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

    def __iter__(self):
        for i in range(self.largo):
            yield getattr(self, "e{0}".format(i))

    def __len__(self):
        """ Retorna la cantidad de elementos existentes.
        """
        return self.largo

    def __add__(self, other):
        lista_retorno = ListaLigada()
        for e1 in range(len(self)):
            lista_retorno.append(self[e1])
        for e2 in range(len(other)):
            lista_retorno.append(other[e2])
        return lista_retorno

    def pop(self):
        valor_popeado = getattr(self, "e{0}".format(self.largo - 1))
        delattr(self, "e{0}".format(self.largo - 1))
        self.largo -= 1
        return valor_popeado

    def remove(self, value):
        i_remover = None
        for n in range(self.largo):
            if getattr(self, "e{0}".format(n)) == value:
                i_remover = n
                break
        if i_remover is not None:
            for i in range(i_remover, self.largo - 1):
                setattr(self, "e{0}".format(i), getattr(self,
                                                        "e{0}".format(i + 1)))
            delattr(self, "e{0}".format(self.largo - 1))
            self.largo -= 1

    def extend(self, other):
        for e in range(len(other)):
            self.append(other[e])

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
        if self.largo == 0:
            return "[]"
        rep = '['
        for a in range(self.largo):
            rep += '{0}, '.format(getattr(self, 'e{0}'.format(a)))
        rep = rep[:-2]
        rep += ']'
        return rep