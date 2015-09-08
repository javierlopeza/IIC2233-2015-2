# coding=utf-8


#ESTE DECORADOR FUNCIONA, PERO LA PARTE 2 ME FALLA :(
def tipar(*tipos):
    def revisar(funcion):
        def revisar_args(*args, **kwargs):
            cantidad_revisiones = len(tipos)
            todo_ok = True
            for i in range(cantidad_revisiones):
                if not isinstance(args[i], tipos[i]):
                    todo_ok = False
            if not todo_ok:
                print("ERROR DE TIPOS DE ARGUMENTOS")
            else:
                return funcion(*args,**kwargs)
        return revisar_args
    return revisar

#PARTE 1:
#Tipado:
#
#3
#Hello World!
#[1, 2, 3, 4, 5, 6, 7, 8, 9]


#No alcance a terminar pero la idea era hacer overload a la funcion principal sumar() con funciones sumar(args),
#que reciben tipos especificos para sumar. Para esto se agregaria la funcion decorada con los tipos a la lista de
#funciones pareada con los tipos. De manera que al llamar a una funcion se pueda revisar los tipos que recibe como
#argumentos y llamar a la funcion correcta.
class Overload:

    def __init__(self, func):
        # implementar este método para inicializar el decorador
        self.func = func
        self._funcs = [func]

    def overload(self, *tipos):
        # implementar este método para agregar nuevos overloads la
        # función original
        self._funcs.append((self.func.tipar(tipos),tipos))
        return self

    def __call__(self, *args, **kwargs):
        # implementar este método para llamar a la función correspondiente
        # a los argumentos entregados.
        numero_argumentos = len(args)
        for f in self._funcs:
            es_la_funcion = True
            for i in range(numero_argumentos):
                if not isinstance(args[i],f[1][i]):
                    es_la_funcion = False
            if es_la_funcion:
                return f(args, kwargs)
                break

    # El siguiente método es para que puedan usar esta clase como
    # decorador desde otras clases. No deben modificar nada en él.
    def __get__(self, obj, cls):
        def caller(*args, **kwargs):
            return self(obj, *args, **kwargs)
        return caller


if __name__ == "__main__":

    @tipar(int, int)
    def suma(a, b):
        return a + b

    @tipar(str, str)
    def sumar_string(s1, s2):
        return s1 + ' ' + s2 + '!'

    @tipar(list, list, tuple)
    def sumar_lista(lista1, lista2, tupla):
        return lista1 + lista2 + list(tupla)

    class ClaseOverloaded:

        def __init__(self, nombre, edad, lista_cosas):
            self.nombre = nombre
            self.edad = edad
            self.lista_cosas = lista_cosas

        @Overload
        def sumar(self):
            print('Tienes que darme algo para sumar!')

        @sumar.overload(str)
        def sumar(self, string):
            print(self.nombre + ' ' + string)

        @sumar.overload(int)
        def sumar(self, numero):
            self.edad += numero
            print('{} ahora tiene {} años!'.format(self.nombre, self.edad))

        @sumar.overload(list, tuple)
        def sumar(self, cosas_nuevas, precios):
            self.lista_cosas.extend(cosas_nuevas)
            print('{} ahora tiene todas estas cosas: {} y le costaron ${:,}'.format(self.nombre,
                                                                                    self.lista_cosas,
                                                                                    sum(precios)))

    c = ClaseOverloaded('Juan', 22, ['laptop', 'calculadora'])

    print('Tipado:\n')
    print(suma(1, 2))
    print(sumar_string('Hello', 'World'))
    print(sumar_lista([1, 2, 3], [4, 5, 6], (7, 8, 9)))

    print('\n------\nOverloading:\n')
    c.sumar()
    c.sumar('Solo')
    c.sumar(2)
    c.sumar(['celular', 'chocolate'], (68900, 550))
