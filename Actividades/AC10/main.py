class RestrictedAccess(type):
    def __new__(meta, nombre, base_clases, diccionario):

        atributos = diccionario.pop('attributes')

        def __init__(self, *args):
            for i in range(len(args)):
                setattr(self, "_" + atributos[i], args[i])

        def create_property(arg):
            def get_arg(self):
                return getattr(self, "_" + arg)

            return property(get_arg)

        diccionario.update({'__init__': __init__})

        for a in atributos:
            diccionario.update({a: create_property(a)})

        return super().__new__(meta, nombre, base_clases, diccionario)


class Singleton(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instancias[cls]
