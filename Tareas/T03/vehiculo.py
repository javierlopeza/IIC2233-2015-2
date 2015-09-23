from verificaciones import \
    verificar_movimiento, \
    verificar_movimiento_mapa, \
    verificar_limite_movimiento


class Vehiculo:
    def __init__(self):
        self.nombre = None
        self.size = None
        self.tipo = ''
        self.simbolo = ''
        self.movimientos = 1
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

    def mover(self, i, j, mapa):
        """
        Recibe las coordenadas i,j de la posicion a la que se quiere mover.
        Y el mapa del usuario poseedor del vehiculo.
        Verifica si la coordenada i,j esta disponible en el mapa,
        de ser asi cambia la posicion del vehiculo
        (restringido a sus posibles movimientos) retornando True,
        de lo contrario retorna False.
        """
        if verificar_movimiento(self, i, j):
            if verificar_limite_movimiento(self, i, j):
                verificar_movimiento_mapa(self, i, j, mapa)
