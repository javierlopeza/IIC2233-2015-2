from verificaciones import \
    verificar_movimiento, \
    verificar_movimiento_mapa, \
    verificar_limite_movimiento


class Vehiculo:
    def __init__(self):
        self.movimientos = 1
        self.nombre = None
        self.size = None
        self.tipo = ''
        self.simbolo = ''
        self.casillas_usadas = []
        self.orientacion = None
        self.ancho = 0
        self.alto = 0

    @property
    def posicion_guia(self):
        try:
            if not self.casillas_usadas:
                raise IndexError('Lista de casillas usadas esta vacia')

        except IndexError as err:
            print('Error: {}'.format(err))

        else:
            return self.casillas_usadas[0]

    def setear_orientacion(self, orientacion):
        try:
            if not self.size:
                raise Exception('No se ha instanciado el vehiculo en detalle')

            if self.orientacion:
                raise Exception('Ya esta seteada la orientacion, '
                                'no se puede cambiar')

            if orientacion != 'h' and orientacion != 'v':
                raise TypeError('No es el tipo de argumentos que'
                                ' recibe como orientacion')

        except Exception as err:
            print('Error: {}'.format(err))

        else:
            self.orientacion = orientacion
            if self.orientacion == 'h':
                self.ancho = max(self.size)
                self.alto = min(self.size)
            elif self.orientacion == 'v':
                self.ancho = min(self.size)
                self.alto = max(self.size)

    def atacar(self):
        pass