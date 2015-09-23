from vehiculo import Vehiculo
from verificaciones import \
    verificar_movimiento, \
    verificar_movimiento_mapa, \
    verificar_limite_movimiento


class Mapa:
    def __init__(self, n=0):
        self.sector = {'aereo': [], 'maritimo': []}
        self.vehiculos_in = {}
        self.armado = False
        self.armar_mapa(n)

    def armar_mapa(self, n):
        try:
            if self.sector['aereo'] and self.sector['maritimo']:
                raise Exception('Los sectores del mapa ya estan construidos.')

            if not isinstance(n, int):
                raise TypeError('Revise la dimension n entregada.')

            if n <= 0:
                raise Exception('Dimension n negativa o cero')

        except (Exception, TypeError) as err:
            print('Error: {}'.format(err))

        else:
            for i in range(n):
                fila = []
                for j in range(n):
                    fila.append('~')
                self.sector['aereo'].append(fila)
                self.sector['maritimo'].append(fila)
            self.n = n
            self.armado = True

    def mover_vehiculo(self, vehiculo):
        try:
            if not isinstance(vehiculo, Vehiculo):
                raise TypeError('El vehiculo entregado no es una'
                                ' instancia de la clase Vehiculo')

            i = input('Ingrese la fila a la que desea mover el vehiculo {}: '.format(vehiculo.nombre))
            j = input('Ingrese la columna a la que desea mover el vehiculo {}: '.format(vehiculo.nombre))

            if verificar_movimiento(vehiculo, i, j):
                i = int(i)
                j = int(j)
                if verificar_limite_movimiento(vehiculo, i, j):
                    verificar_movimiento_mapa(vehiculo, i, j, self)

        except TypeError as err:
            print('Error: {}'.format(err))

    def agregar_vehiculo(self, vehiculo):
        try:
            if not isinstance(vehiculo, Vehiculo):
                raise TypeError('El vehiculo entregado no es una'
                                ' instancia de la clase Vehiculo')

            i = input('Ingrese la fila en la que desea posicionar el vehiculo {}: '.format(vehiculo.nombre))
            j = input('Ingrese la columna en la que desea posicionar el vehiculo {}: '.format(vehiculo.nombre))

            if verificar_movimiento(vehiculo, i, j):
                i = int(i)
                j = int(j)
                verificar_movimiento_mapa(vehiculo, i, j, self)

        except TypeError as err:
            print('Error: {}'.format(err))

    def eliminar_vehiculo(self, nombre_vehiculo):
        return self.vehiculos_in.pop(nombre_vehiculo)

    def __str__(self):
        try:
            if not (self.sector['aereo'] and self.sector['maritimo']):
                raise Exception('El mapa no esta armado.')

        except Exception as err:
            return 'Error: {}'.format(err)

        else:
            ret = '     ' * (self.n // 2) + 'SECTOR AEREO\n'
            ret += ' ' * (len(str(self.n)) + 4)
            for i in range(self.n):
                ret += '{0}    '.format(i)
            ret += '\n'
            for i in range(self.n):
                ret += '  ' + ' ' * (len(str(self.n)) - len(str(i)))
                ret += '{0}  '.format(i)
                for j in range(self.n):
                    ret += '{0}    '.format(self.sector['aereo'][i][j]) + ' ' * (len(str(j)) - 1)
                ret += '\n'

            ret += '\n'
            ret += '     ' * (self.n // 2) + 'SECTOR MARITIMO\n'
            ret += ' ' * (len(str(self.n)) + 4)
            for i in range(self.n):
                ret += '{0}    '.format(i)
            ret += '\n'
            for i in range(self.n):
                ret += '  ' + ' ' * (len(str(self.n)) - len(str(i)))
                ret += '{0}  '.format(i)
                for j in range(self.n):
                    ret += '{0}    '.format(self.sector['maritimo'][i][j]) + ' ' * (len(str(j)) - 1)
                ret += '\n'
            return ret
