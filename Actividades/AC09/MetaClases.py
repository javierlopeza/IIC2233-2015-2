__author__ = 'Javier Lopez'


class MetaRobot(type):
    def __new__(meta, nombre, base_clases, diccionario):
        atributos = {'creador': 'javierlopeza',
                     'ip_inicio': '190.102.62.283'}
        diccionario.update(atributos)

        def check_creator(self):
            if self.creador in self.creadores:
                print('{0} es un programador oficial.'.format(self.creador))
            else:
                print('{0} NO es un programador oficial.'.format(self.creador))

        def cortar_conexion(self):
            if self.Verificar():
                self.actual.hacker = 0
                mensaje = 'HACKER DETECTADO EN EL PUERTO {0},' \
                          ' SE LE HA CORTADO LA CONEXION'.format(self.actual.ide)
                raise NameError(mensaje)
            # En caso de no haber Hacker no imprime nada.

        def cambiar_nodo(self, nuevo_nodo):
            print('El Robot proviene del nodo {0} y su destino '
                  'es el nodo {1}'.format(self.actual.ide, nuevo_nodo.ide))
            self.actual = nuevo_nodo

        metodos = {'check_creator': check_creator,
                   'cortar_conexion': cortar_conexion,
                   'cambiar_nodo': cambiar_nodo}
        diccionario.update(metodos)

        return super().__new__(meta, nombre, base_clases, diccionario)
