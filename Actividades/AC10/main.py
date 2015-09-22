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
    instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instancias:
            cls.instancias[cls] = super().__call__(*args, **kwargs)
        return cls.instancias[cls]

class A(metaclass = Singleton):
    def __init__(self, value):
        self.val = value
a = A(10) # Se crea una instancia de A
b = A(20) # Se retorna la instancia que ya estaba creada
print (a.val, b.val)
## 10 10
print (b is a)