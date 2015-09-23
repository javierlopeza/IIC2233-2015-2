from copy import deepcopy


def verificar_movimiento(vehiculo, ij):
    try:
        if not ',' in ij:
            raise TypeError('Verifique la coordenada ingresada, '
                            'debe ser de la forma: i,j')

        l_ij = ij.split(',')

        if not len(l_ij) == 2:
            raise TypeError('Verifique la coordenada ingresada, '
                            'debe ser de la forma: i,j')

        i = l_ij[0]
        j = l_ij[1]

        if not i.isdigit() or not j.isdigit():
            raise TypeError('El o los valores ingresados no son validos.')

        i = int(i)
        j = int(j)

        if not vehiculo.orientacion:
            raise Exception('La orientacion del vehiculo no esta seteada')

        if not vehiculo.nombre:
            raise Exception('No se ha instanciado el vehiculo en detalle')

        if i < 0 or j < 0:
            raise Exception('Coordenadas negativas')

    except (TypeError, Exception) as err:
        print('Error: {}'.format(err))

    else:
        return True


def verificar_movimiento_mapa(vehiculo, i, j, mapa):
    try:
        if not mapa.armado:
            raise Exception('El mapa no esta armado.')

        sector_aux = deepcopy(mapa.sector[vehiculo.tipo])
        if vehiculo.casillas_usadas:
            for pos in range(len(vehiculo.casillas_usadas)):
                pos_i = vehiculo.casillas_usadas[pos][0]
                pos_j = vehiculo.casillas_usadas[pos][1]
                sector_aux[pos_i][pos_j] = '~'
            casillas_nuevas_aux = deepcopy(vehiculo.casillas_usadas)
            mov_i = vehiculo.posicion_guia[0] - i
            mov_j = vehiculo.posicion_guia[1] - j
            for c in range(len(casillas_nuevas_aux)):
                casillas_nuevas_aux[c][0] -= mov_i
                casillas_nuevas_aux[c][1] -= mov_j
        else:
            casillas_nuevas_aux = []
            for k in range(vehiculo.alto):
                for h in range(vehiculo.ancho):
                    casillas_nuevas_aux.append([i + k, j + h])

        for c in range(len(casillas_nuevas_aux)):
            c_aux_i = casillas_nuevas_aux[c][0]
            c_aux_j = casillas_nuevas_aux[c][1]
            if c_aux_i > (mapa.n - 1) \
                    or c_aux_j > (mapa.n - 1) \
                    or c_aux_i < 0 \
                    or c_aux_j < 0:
                raise Exception('El posicionamiento no es valido.')
            if sector_aux[c_aux_i][c_aux_j] != '~':
                raise Exception('La posicion esta ocupada'
                                ' en el mapa presente.')

        for p in range(len(casillas_nuevas_aux)):
            ii = casillas_nuevas_aux[p][0]
            jj = casillas_nuevas_aux[p][1]
            if p == 0:
                sector_aux[ii][jj] = vehiculo.simbolo.lower()
            else:
                sector_aux[ii][jj] = vehiculo.simbolo
        mapa.sector[vehiculo.tipo] = sector_aux
        mapa.vehiculos_in.update({vehiculo.nombre: vehiculo})
        vehiculo.casillas_usadas = casillas_nuevas_aux

    except Exception as err:
        print('Error: {}'.format(err))

    else:
        return True


def verificar_limite_movimiento(vehiculo, i, j):
    """
    Retorna el bool de si es capaz de avanzar a dicha coordenada
    dado sus movimientos maximos y su posicion guia actual.
    """
    try:
        posx = vehiculo.posicion_guia[0]
        posy = vehiculo.posicion_guia[1]
        if posx == i and posy == j:
            raise Exception('El vehiculo {0} no puede moverse a '
                            'la posicion en la que se encuentra ({1}, {2}), '
                            'seria una jugada sin sentido.'.
                            format(vehiculo.nombre,
                                   i,
                                   j))

        if not vehiculo.movimientos:
            raise Exception('El vehiculo {0} no puede moverse.'.
                            format(vehiculo.nombre))

    except (TypeError, Exception) as err:
        print('Error: {}'.format(err))

    else:
        if vehiculo.movimientos == float('infinity'):
            return True
        if (i == posx + 1 or i == posx - 1) and j == posy:
            return True
        if (j == posy + 1 or j == posy - 1) and i == posx:
            return True

        print('Error: El vehiculo {0} no puede moverse hasta la posicion '
              '({1}, {2}) por su limite de movimientos.'.
              format(vehiculo.nombre,
                     i,
                     j))
