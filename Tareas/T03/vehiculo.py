class Vehiculo:
    def __init__(self):
        self.movimientos = 1
        self.posicion_actual = []

    def verificar_limite_movimiento(self, i, j):
        """
        Recibe la coordenada i,j a la que se quiere mover el vehiculo.
        Si tiene tantos movimientos para llegar a el retorna True,
        de lo contrario retorna False.
        """
        if not self.movimientos:
            return False

        if self.movimientos == float('infinity'):
            return True

        posx = self.posicion_actual[0]
        posy = self.posicion_actual[1]
        if posx == i and posy == j:
            print('--- El vehiculo {0} no puede moverse a '
                  'la posicion actual ({1}, {2}), '
                  'seria una jugada sin sentido. ---'.
                  format(self.nombre,
                         i,
                         j))
            return False

        if (i == posx + 1 or i == posx - 1) and j == posy:
            return True
        if (j == posy + 1 or j == posy - 1) and i == posx:
            return True

        print('--- El vehiculo {0} no puede moverse hasta la posicion '
              '({1}, {2}) por su limite de movimientos. ---'.
              format(self.nombre,
                     i,
                     j))
        return False

    def verificar_movimiento_mapa(self, i, j, mapa):
        pass


    def moverse(self, i, j, mapa):
        """
        Recibe las coordenadas i,j de la posicion a la que se quiere mover.
        Y el mapa del usuario poseedor del vehiculo.
        Verifica si la coordenada i,j esta disponible en el mapa,
        de ser asi cambia la posicion del vehiculo
        (restringido a sus posibles movimientos) retornando True,
        de lo contrario retorna False.
        """
        if self.verificar_movimiento(i, j):
            return True
        else:
            return False
