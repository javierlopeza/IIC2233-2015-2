from clases.vehiculo import Vehiculo
from funciones.verificaciones import \
    verificar_movimiento, \
    verificar_movimiento_mapa, \
    verificar_limite_movimiento
from copy import deepcopy


class Mapa:
    def __init__(self, n=0, owner='p'):
        self.sector = {'aereo': [], 'maritimo': []}
        self.armado = False
        self.armar_mapa(n)
        self.owner = owner

    def armar_mapa(self, n):
        try:
            if self.sector['aereo'] and self.sector['maritimo']:
                raise AttributeError('Los sectores del mapa ya estan construidos.')

            if not isinstance(n, int):
                raise TypeError('Revise la dimension n entregada.')

            if n <= 0:
                raise ValueError('Dimension n negativa o cero')

        except (AttributeError, TypeError, ValueError) as err:
            print('Error: {}'.format(err))

        else:
            for i in range(n):
                fila = []
                for j in range(n):
                    fila.append('~')
                fila_copia = deepcopy(fila)
                self.sector['aereo'].append(fila)
                self.sector['maritimo'].append(fila_copia)
            self.n = n
            self.armado = True

    def mover_vehiculo(self, vehiculo, ij=None):
        try:
            if not isinstance(vehiculo, Vehiculo):
                raise TypeError('El vehiculo entregado no es una'
                                ' instancia de la clase Vehiculo')
            if not ij:
                ij = input('Ingrese las coordenadas (fila,columna) '
                           'a la que desea mover el vehiculo {} [i,j]: '.
                           format(vehiculo.nombre))

            if verificar_movimiento(vehiculo, ij, self):
                i = int(ij.split(',')[0])
                j = int(ij.split(',')[1])
                return verificar_movimiento_mapa(vehiculo, i, j, self)

        except TypeError as err:
            print('Error: {}'.format(err))

    def agregar_vehiculo(self, vehiculo, ij=None):
        try:
            if not isinstance(vehiculo, Vehiculo):
                raise TypeError('El vehiculo entregado no es una'
                                ' instancia de la clase Vehiculo')

            if not ij:
                ij = input('Ingrese las coordenadas (fila,columna) '
                           'en la que desea posicionar el vehiculo {} [i,j]: '.
                           format(vehiculo.nombre))

            if verificar_movimiento(vehiculo, ij, self):
                i = int(ij.split(',')[0])
                j = int(ij.split(',')[1])
                verificar_movimiento_mapa(vehiculo, i, j, self)
                if vehiculo.casillas_usadas:
                    if self.owner == 'p':
                        print('--- Vehiculo {0} agregado correctamente'
                              ' en la casilla ({1}, {2}) ---'.
                              format(vehiculo.nombre, i, j))
                    return True

        except TypeError as err:
            print('Error: {}'.format(err))

    def eliminar_vehiculo(self, vehiculo, sector_e):
        try:
            if not self.sector[sector_e]:
                raise AttributeError('No hay vehiculos en sector {}'.
                                     format(sector_e))
            for casilla in vehiculo.casillas_usadas:
                i = casilla[0]
                j = casilla[1]
                self.sector[sector_e][i][j] = '~'

        except AttributeError as err:
            print('Error: {}'.format(err))

    def marcar(self, sector_e, i, j, simbolo):
        try:
            if not self.sector[sector_e]:
                raise AttributeError('No se han cargado los sectores del mapa.')
            self.sector[sector_e][i][j] = simbolo

        except AttributeError as err:
            print('Error: {}'.format(err))

    def __str__(self):
        try:
            if not (self.sector['aereo'] and self.sector['maritimo']):
                raise AttributeError('El mapa no esta armado.')

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

        except AttributeError as err:
            return 'Error: {}'.format(err)

        else:
            return ret
