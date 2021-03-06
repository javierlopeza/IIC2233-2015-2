from random import randint, choice
from operator import itemgetter
from copy import deepcopy


class Jugador:
    def __init__(self, nombre='', ide=0):
        self.nombre = nombre
        self.id = ide
        self.mapa = None
        self.radar = None
        self.radares = []
        self.casillas_espiadas = []
        self.flota = None
        self.flota_activa = []
        self.flota_muerta = []
        self.turnos = 0
        self.loser = False

    def jugar(self, oponente):
        turno_actual = self.turnos

        # Mientras no termine el turno, que juegue.
        # El turno termina al atacar, mover vehiculo,
        # explorar o usar el Kit.

        while self.turnos == turno_actual:
            print('\n === TURNO {2} PLAYER {0}: {1} -> JUEGUE ==='.format(
                self.id, self.nombre, self.turnos + 1))
            self.enviar_napalm_pendiente(oponente)
            self.display_menu(oponente)

    def enviar_napalm_pendiente(self, oponente):
        for vehiculo in oponente.flota_activa:
            if vehiculo.napalm_pendiente:
                vehiculo.napalm_pendiente = False
                vehiculo.vida -= 5
                if vehiculo.vida <= 0:
                    vehiculo.vida = 0
                    print(' --> Por un ataque Napalm en el turno pasado, '
                          'el vehiculo {0} ha sido destruido.'.
                          format(vehiculo.nombre))
                    oponente.flota_muerta.append(vehiculo)
                    oponente.flota_activa.remove(vehiculo)
                    oponente.mapa.eliminar_vehiculo(vehiculo,
                                                    'maritimo')
                    for cas in vehiculo.casillas_usadas:
                        iii = cas[0]
                        jjj = cas[1]
                        self.radar.marcar('maritimo', iii, jjj, 'X')
                else:
                    print(' --> Por un ataque Napalm en el turno pasado, '
                          'el vehiculo {0} ha recibido 5 extra de damage.'.
                          format(vehiculo.nombre))

    def display_menu(self, oponente):
        opciones = {'1': self.ver_mapa,
                    '2': self.ver_radar,
                    '3': self.revisar_historial_radar,
                    '4': self.revisar_casillas_espiadas,
                    '5': self.mover_vehiculo,
                    '6': self.atacar
                    }

        menu_impreso = '  [1]: Ver Mi Mapa\n' \
                       '  [2]: Ver Radar\n' \
                       '  [3]: Revisar Historial Radar\n' \
                       '  [4]: Revisar Casillas Espiadas\n' \
                       '  [5]: Mover Vehiculo\n' \
                       '  [6]: Atacar Oponente\n'

        proximo_indice = 7

        for vehiculo in self.flota_activa:
            if vehiculo.nombre == 'Puerto':
                opciones.update({'7': self.kit_ingenieros})
                menu_impreso += '  [7]: Usar Kit de Ingenieros\n'
                proximo_indice += 1
                break

        for vehiculo in self.flota_activa:
            if vehiculo.nombre == 'Avion Explorador':
                opciones.update({str(proximo_indice): self.explorar})
                menu_impreso += '  [{0}]: Explorar\n'. \
                    format(str(proximo_indice))
                proximo_indice += 1
                break

        opciones.update({str(proximo_indice): self.paralizar})
        menu_impreso += '  [{0}]: Paralizar Avion Explorador Enemigo\n'. \
            format(str(proximo_indice))
        proximo_indice += 1

        opciones.update({str(proximo_indice): self.terminar_turno})
        menu_impreso += '  [{0}]: Terminar Turno\n'. \
            format(str(proximo_indice))

        print(menu_impreso)

        eleccion = input("Ingrese Opcion: ")
        accion = opciones.get(eleccion)
        if accion:
            if accion.__name__ == 'atacar' \
                    or accion.__name__ == 'explorar' \
                    or accion.__name__ == 'paralizar':
                accion(oponente)
            else:
                accion()
        else:
            print("\n--- {0} no es una opcion valida ---\n".format(
                eleccion))

    def ver_mapa(self):
        print('\n=== MAPA ===\n')
        print(self.mapa)
        nota_simbolos = 'SIMBOLOGIA  ->  '
        for vehiculo in self.flota_activa:
            nota_simbolos += ' {0}{1}: {2}  |'.format(
                vehiculo.simbolo.lower(), vehiculo.simbolo, vehiculo.nombre)
        print(nota_simbolos)

    def ver_radar(self):
        print('\n=== RADAR ===\n')
        print(self.radar)
        print('SIMBOLOGIA  ->  A: Vehiculo enemigo atacado  '
              '|  X: Vehiculo enemigo muerto  '
              '|  O: Disparo al agua  '
              '|  F: Vehiculo encontrado con el explorador  '
              '|  E: Coordenada explorador revelada por el enemigo')

    def revisar_historial_radar(self):
        print('\n=== REVISAR HISTORIAL RADAR ===\n')
        try:
            if len(self.radares) == 0:
                raise AttributeError('No hay radares en el historial.')

            print('   -> Estan disponibles los estados del radar hasta el turno {}.\n'.format(len(self.radares)))
            turno = input('Ingrese el turno del cual '
                          'quiere revisar el estado del Radar: ')

            if not turno.isdigit():
                raise TypeError('El turno ingresado debe ser un numero.')

            turno = int(turno)
            if not (len(self.radares) >= turno >= 1):
                raise IndexError('Solo estan disponibles los estados del radar'
                                 ' hasta el turno {}'.
                                 format(len(self.radares)))

            radar = self.radares[turno - 1]
            print('\n  --- ESTADO DEL RADAR EN EL TURNO {} ---\n'.format(turno))
            print(radar)
            print('SIMBOLOGIA  ->  A: Vehiculo enemigo atacado  '
                  '|  X: Vehiculo enemigo muerto  '
                  '|  O: Disparo al agua  '
                  '|  F: Vehiculo encontrado con el explorador  '
                  '|  E: Coordenada explorador revelada por el enemigo')

        except (AttributeError, TypeError, IndexError) as err:
            print('Error: {}'.format(err))

    def revisar_casillas_espiadas(self):
        try:
            if not self.casillas_espiadas:
                raise AttributeError('El enemigo no ha '
                                     'descubierto ningun vehiculo.')

            print('\n=== CASILLAS ESPIADAS POR EL ENEMIGO ===\n')
            for casilla in self.casillas_espiadas:
                ie = casilla[0]
                je = casilla[1]
                print('   ->  Casilla ({0}, {1})'.format(ie, je))

        except AttributeError as err:
            print('Error: {}'.format(err))

    def mostrar_flota_activa(self):
        try:
            if not self.flota_activa:
                raise AttributeError('No se han cargado los vehiculos a la flota')

            ret = ''
            for vehiculo in self.flota_activa:
                if vehiculo.nombre != 'Lancha':
                    ret += '  [{0}]: {1}\n'.format(
                        self.flota_activa.index(vehiculo),
                        vehiculo.nombre)
            print(ret)

        except AttributeError as err:
            print('Error: {}'.format(err))

    def mostrar_flota_movible(self):
        try:
            if not self.flota_activa:
                raise AttributeError('No se han cargado los vehiculos a la flota')

            movibles = []
            ret = ''
            indice = 0
            for vehiculo in self.flota_activa:
                if vehiculo.movilidad != 0:
                    movibles.append(vehiculo)
                    ret += '  [{0}]: {1}\n'.format(
                        indice,
                        vehiculo.nombre)
                    indice += 1
            print(ret)
            self.movibles = movibles

        except AttributeError as err:
            print('Error: {}'.format(err))

    def mostrar_flota_maritima_reparable(self):
        try:
            if not self.flota_activa:
                raise AttributeError('No se han cargado los vehiculos a la flota')

            v_reparables = []
            ret = ''
            for vehiculo in self.flota_activa:
                if vehiculo.tipo == 'maritimo' and vehiculo.vida < vehiculo.resistencia:
                    v_reparables.append(vehiculo)
                    ret += '  [{0}]: {1}\n'.format(
                        v_reparables.index(vehiculo),
                        vehiculo.nombre)
            if self.nombre != 'Computadora':
                print(ret)
            return v_reparables

        except AttributeError as err:
            print('Error: {}'.format(err))

    def mostrar_flota_paralizadora(self):
        try:
            if not self.flota_activa:
                raise AttributeError('No se han cargado los vehiculos a la flota')

            v_paralizadores = []
            ret = ''
            for vehiculo in self.flota_activa:
                for ataque in vehiculo.ataques:
                    if ataque.nombre == 'GBU-43/B Massive ' \
                                        'Ordnance Air Blast ' \
                                        'Paralizer':
                        v_paralizadores.append(vehiculo)
                        ret += '  [{0}]: {1}\n'.format(
                            v_paralizadores.index(vehiculo),
                            vehiculo.nombre)
                        break
            if self.nombre != 'Computadora':
                print(ret)
            return v_paralizadores

        except AttributeError as err:
            print('Error: {}'.format(err))

    @property
    def flota_activa_maritima(self):
        try:
            if not self.flota_activa:
                raise AttributeError('La flota esta vacia')

            v_maritimos = []
            for vehiculo in self.flota_activa:
                if vehiculo.tipo == 'maritimo':
                    v_maritimos.append(vehiculo)

            return v_maritimos

        except AttributeError as err:
            print('Error: {}'.format(err))

    def mover_vehiculo(self):
        try:
            if not self.flota_activa:
                raise AttributeError('La flota no esta cargada.')

            print('\n=== VEHICULOS QUE SE PUEDEN MOVER ===')
            self.mostrar_flota_movible()

            vehiculo_mover = input('Ingrese el numero del vehiculo '
                                   'que desea mover: ')
            if not vehiculo_mover.isdigit():
                raise TypeError('La opcion {} '
                                'no es un numero'.
                                format(vehiculo_mover))

            vehiculo_mover = int(vehiculo_mover)
            if not vehiculo_mover < len(self.movibles):
                raise IndexError('El numero {} no esta '
                                 'dentro de las opciones'.
                                 format(vehiculo_mover))

            vehiculo_mover_inst = self.movibles[vehiculo_mover]
            mover = self.mapa.mover_vehiculo(
                vehiculo_mover_inst)
            if mover:
                print('--- El vehiculo {0} se movio '
                      'correctamente a la posicion ({1}, {2}) ---'.
                      format(vehiculo_mover_inst.nombre, mover[0], mover[1]))
                vehiculo_mover_inst.movimientos += 1
                self.terminar_turno()

        except (AttributeError, TypeError, IndexError) as err:
            print('Error: {}'.format(err))

    def atacar(self, oponente,
               vehiculo_atacador_inst=None,
               ataque_elegido_inst=None,
               casillas_atacadas=None):
        try:
            if not self.flota_activa:
                raise AttributeError('La flota no esta cargada.')

            if not vehiculo_atacador_inst:
                print('\n=== VEHICULOS QUE PUEDEN ATACAR ===')
                self.mostrar_flota_activa()

                vehiculo_atacador = input('Ingrese el numero del vehiculo '
                                          'con el que desea atacar: ')
                if not vehiculo_atacador.isdigit():
                    raise TypeError('La opcion {} '
                                    'no es un numero'.
                                    format(vehiculo_atacador))

                vehiculo_atacador = int(vehiculo_atacador)
                if not vehiculo_atacador < len(self.flota_activa):
                    raise IndexError('El numero {} no esta '
                                     'dentro de las opciones'.
                                     format(vehiculo_atacador))

                vehiculo_atacador_inst = self.flota_activa[vehiculo_atacador]

                if vehiculo_atacador_inst.nombre == 'Lancha':
                    raise IndexError('El numero {} no esta '
                                     'dentro de las opciones'.
                                     format(vehiculo_atacador))

            if not ataque_elegido_inst:
                print('\n=== ATAQUES DISPONIBLES PARA EL VEHICULO {} ==='.
                      format(vehiculo_atacador_inst.nombre))

                vehiculo_atacador_inst.mostrar_ataques_disponibles()

                ataque_elegido = input('Ingrese el numero del ataque '
                                       'que quiere utilizar: ')

                if not ataque_elegido.isdigit():
                    raise TypeError('La opcion {} '
                                    'no es un numero'.
                                    format(vehiculo_atacador))

                ataque_elegido = int(ataque_elegido)
                if not ataque_elegido < \
                        len(vehiculo_atacador_inst.ataques_disponibles):
                    raise IndexError('El numero {} no esta '
                                     'dentro de las opciones'.
                                     format(vehiculo_atacador))

                ataque_elegido_inst = \
                    vehiculo_atacador_inst.ataques_disponibles[ataque_elegido]

            if not ataque_elegido_inst.nombre == 'Misil de crucrero ' \
                                                 'BGM-109 Tomahawk':
                es_tom = False
                if not casillas_atacadas:
                    casilla_ataque = input('Ingrese la casilla oponente '
                                           'a la que quiere atacar [i,j]: ')
                    if ',' not in casilla_ataque:
                        raise TypeError('El formato de casilla no es valido.')

                    l_ij = casilla_ataque.split(',')
                    if len(l_ij) != 2:
                        raise TypeError('El formato de casilla no es valido.')

                    ii = l_ij[0]
                    jj = l_ij[1]
                    if not ii.isdigit() or not jj.isdigit():
                        raise TypeError('El formato de casilla no es valido.')

                    ii = int(ii)
                    jj = int(jj)
                    if ii >= self.mapa.n or jj >= self.mapa.n:
                        raise AttributeError('La casilla no se encuentra '
                                             'en el mapa oponente.')
                    casillas_atacadas = [[ii, jj]]

            else:
                es_tom = True
                if not casillas_atacadas:
                    fila_columna = input('Ingrese si desea '
                                         'atacar una fila o columna [f/c]: ')

                    if not fila_columna == 'c' and not fila_columna == 'f':
                        raise TypeError('Opcion invalida.')

                    if fila_columna == 'f':
                        fila_ataque = input('Ingrese la fila oponente '
                                            'a la que quiere atacar [i]: ')
                        if not fila_ataque.isdigit():
                            raise TypeError('El formato de fila no es valido.')

                        fila_ataque = int(fila_ataque)
                        if not fila_ataque < self.mapa.n:
                            raise IndexError('La fila no existe '
                                             'en el mapa oponente.')

                        casillas_atacadas = []
                        for k in range(self.mapa.n):
                            casillas_atacadas.append([fila_ataque, k])

                    else:
                        columna_ataque = input('Ingrese la columna oponente '
                                               'a la que quiere atacar [j]: ')
                        if not columna_ataque.isdigit():
                            raise TypeError('El formato de fila no es valido.')

                        columna_ataque = int(columna_ataque)
                        if not columna_ataque < self.mapa.n:
                            raise IndexError('La columna no existe '
                                             'en el mapa oponente.')

                        casillas_atacadas = []
                        for k in range(self.mapa.n):
                            casillas_atacadas.append([k, columna_ataque])

            # Se agrega una usada al ataque elegido y se usa.
            ataque_elegido_inst.usadas += 1
            ataque_elegido_inst.usar()

            exito = False
            n_piezas_afectadas = 0
            for casilla in casillas_atacadas:
                ii = casilla[0]
                jj = casilla[1]
                retornar = None
                simbolo_casilla_oponente = \
                    oponente.mapa.sector['maritimo'][ii][jj]
                # Si el ataque cae en agua, se retorna el fracaso del ataque.
                if simbolo_casilla_oponente == '~':
                    retornar = 'el mar'
                    if not es_tom:
                        self.radar.marcar('maritimo', ii, jj, 'O')

                else:
                    simbolo_casilla_oponente = simbolo_casilla_oponente.upper()
                    for vehiculo_oponente in oponente.flota_activa:
                        if vehiculo_oponente.simbolo == \
                                simbolo_casilla_oponente:
                            exito = True
                            n_piezas_afectadas += 1
                            vehiculo_victima = vehiculo_oponente
                            vida_previa = vehiculo_victima.vida
                            # Le baja la vida al vehiculo oponente.
                            vehiculo_victima.vida -= ataque_elegido_inst.damage
                            # Si la vida nueva queda negativa,
                            # simplemente queda en cero.
                            if vehiculo_victima.vida < 0:
                                vehiculo_victima.vida = 0
                            # Se suma el damage realizado al damage
                            # efectivo del ataque.
                            ataque_elegido_inst.damage_efectivo += \
                                (vida_previa - vehiculo_victima.vida)
                            # Si el vehiculo se ha destruido se retorna
                            # el tipo y sus coordenadas.
                            vehiculo_destruido = False
                            if vehiculo_victima.vida == 0:
                                vehiculo_destruido = True
                                retornar = 'el vehiculo {0} y lo destruyo'. \
                                    format(vehiculo_victima.nombre)
                                oponente.flota_muerta.append(vehiculo_victima)
                                oponente.flota_activa.remove(vehiculo_victima)
                                oponente.mapa.eliminar_vehiculo(
                                    vehiculo_victima,
                                    'maritimo')
                                for cas in vehiculo_victima.casillas_usadas:
                                    iii = cas[0]
                                    jjj = cas[1]
                                    self.radar.marcar('maritimo', iii, jjj, 'X')
                            # Si sigue con vida se retorna el exito
                            # del ataque.
                            else:
                                retornar = 'un vehiculo'
                            if not es_tom and not vehiculo_destruido:
                                self.radar.marcar('maritimo', ii, jj, 'A')
                            break
            if exito:
                ataque_elegido_inst.exitos += 1

                if ataque_elegido_inst.nombre == 'Napalm':
                    vehiculo_victima.napalm_pendiente = True
                    if (vehiculo_victima.vida - 5) < 0:
                        damage_extra_efectivo = 5 - abs(vehiculo_victima.vida - 5)
                    else:
                        damage_extra_efectivo = 5
                    ataque_elegido_inst.damage_efectivo += damage_extra_efectivo

            if not ataque_elegido_inst.nombre == 'Misil de crucrero' \
                                                 ' BGM-109 Tomahawk':
                print('\n--- El ataque {0} hecho por {1} cayo en {2} '
                      'en las coordenadas ({3}, {4}) ---'.
                      format(ataque_elegido_inst.nombre,
                             self.nombre,
                             retornar,
                             ii,
                             jj))
            else:
                if exito:
                    print('\n--- El ataque Misil de crucrero'
                          ' BGM-109 Tomahawk hecho por {0} fue exitoso '
                          'y se afectaron {1} piezas enemigas ---'.
                          format(self.nombre, n_piezas_afectadas))
                else:
                    print('\n--- El ataque NO fue exitoso')

            if ataque_elegido_inst.nombre == 'Kamikaze':
                # El Kamikaze IXXI muere luego de atacar.
                self.mapa.eliminar_vehiculo(vehiculo_atacador_inst, 'aereo')
                self.flota_muerta.append(vehiculo_atacador_inst)
                self.flota_activa.remove(vehiculo_atacador_inst)

        except (IndexError, TypeError, AttributeError) as err:
            print('Error: {}'.format(err))

        else:
            self.terminar_turno()

    def kit_ingenieros(self):
        try:
            tiene_puerto = False
            puerto = None
            for vehiculo in self.flota_activa:
                if vehiculo.nombre == 'Puerto':
                    tiene_puerto = True
                    puerto = vehiculo
                    break
            if not tiene_puerto:
                raise AttributeError('El jugador {0} no tiene Puerto'.
                                     format(self.nombre))

            kit = None
            for ataque in puerto.ataques:
                if ataque.nombre == 'Kit de Ingenieros':
                    kit = ataque
                    break

            if not kit:
                raise AttributeError('El Puerto no posee Kit de Ingenieros')

            if not kit.disponible:
                raise AttributeError('El Kit de Ingenieros no esta disponible'
                                     ' para ser usado este turno. '
                                     'Quedan {} turnos para que vuelva a estar'
                                     'disponible.'.format(kit.turnos_pendientes))

            print('\n=== VEHICULOS MARITIMOS REPARABLES CON '
                  'EL KIT DE INGENIEROS ===')
            v_reparables = self.mostrar_flota_maritima_reparable()

            if len(v_reparables) == 0:
                raise ValueError('No hay ningun vehiculo maritimo'
                                 ' que se pueda reparar.')

            vehiculo_reparar = input('Ingrese el numero del vehiculo '
                                     'que desea reparar: ')
            if not vehiculo_reparar.isdigit():
                raise TypeError('La opcion {} '
                                'no es un numero'.
                                format(vehiculo_reparar))

            vehiculo_reparar = int(vehiculo_reparar)
            if not vehiculo_reparar < len(v_reparables):
                raise IndexError('El numero {} no esta '
                                 'dentro de las opciones'.
                                 format(vehiculo_reparar))

            vehiculo_reparar_inst = v_reparables[vehiculo_reparar]

            vida_previa = vehiculo_reparar_inst.vida
            kit.usar()
            vehiculo_reparar_inst.vida += 1

            print('\n--- El vehiculo {0} aumento su vida '
                  'de {1} a {2} gracias al Kit de Ingenieros ---'.
                  format(vehiculo_reparar_inst.nombre,
                         vida_previa,
                         vehiculo_reparar_inst.vida))

            self.terminar_turno()

        except (AttributeError, IndexError, TypeError, ValueError) as err:
            print('Error: {}'.format(err))

    def explorar(self, oponente):
        try:
            tiene_explorador = False
            explorador = None
            for vehiculo in self.flota_activa:
                if vehiculo.nombre == 'Avion Explorador':
                    tiene_explorador = True
                    explorador = vehiculo
                    break

            if not tiene_explorador:
                raise AttributeError('El jugador {0} no tiene '
                                     'Avion Explorador'.
                                     format(self.nombre))

            if explorador.turnos_paralizado:
                raise AttributeError('El Avion Explorador esta paralizado. '
                                     'Quedan {} turnos para que vuelva a estar'
                                     ' disponible.'.
                                     format(explorador.turnos_paralizado))

            ij_explorar = input('Ingrese la coordenada de la posicion guia '
                                'del area de 3x3 donde quiere mover el'
                                ' Avion Explorador para que explore [i,j]: ')

            if ',' not in ij_explorar:
                raise TypeError('Formato invalido de coordenada, '
                                'debe ser de la forma i,j')

            ij_lista = ij_explorar.split(',')
            if len(ij_lista) != 2:
                raise TypeError('Formato invalido de coordenada, '
                                'debe ser de la forma i,j')

            icentral = ij_lista[0]
            jcentral = ij_lista[1]
            if not icentral.isdigit() or not jcentral.isdigit():
                raise TypeError('Se deben ingreser numeros validos '
                                'como coordenadas.')

            icentral = int(icentral)
            jcentral = int(jcentral)
            if icentral >= self.mapa.n or jcentral >= self.mapa.n:
                raise IndexError('La casilla ingresada no esta dentro de '
                                 'las dimensiones del mapa.')

            if self.mapa.mover_vehiculo(explorador, ij_explorar):
                casillas_explorar = explorador.casillas_usadas

            else:
                raise AttributeError('No se pudo mover el Avion Explorador')

            algo_encontrado = False
            for casilla in casillas_explorar:
                iexp = casilla[0]
                jexp = casilla[1]
                if oponente.mapa.sector['maritimo'][iexp][jexp] != '~':
                    algo_encontrado = True
                    print('--- Se encontro una pieza de vehiculo enemigo'
                          ' en la casilla ({0}, {1}) y '
                          'se guardo en el radar como F ---'.
                          format(iexp, jexp))
                    self.radar.sector['maritimo'][iexp][jexp] = 'F'

            if not algo_encontrado:
                print('--- No se encontro ninguna pieza enemiga. ---')

            revelar_coordenada = randint(0, 1)

            if revelar_coordenada:
                casilla_revelada = choice(explorador.casillas_usadas)
                ir = casilla_revelada[0]
                jr = casilla_revelada[1]
                oponente.radar.sector['aereo'][ir][jr] = 'E'
                print('\n--- El Avion Explorador ha revelado la '
                      'coordenada ({0}, {1}) a tu oponente, '
                      'quedando esta registrada'
                      ' en el radar enemigo como E ---\n'.
                      format(ir, jr))
                if algo_encontrado:
                    oponente.casillas_espiadas.append([ir, jr])
                    print('--- Ahora el enemigo sabe que '
                          'descubriste un vehiculo suyo '
                          'en la coordenada ({0}, {1}). '
                          'Se guardo esta coordenada '
                          'en sus Casillas Espiadas ---\n'.
                          format(ir, jr))

            else:
                print('\n--- El Avion Explorador fue discreto '
                      'y no revelo ninguna coordenada ---\n')

            self.terminar_turno()

        except (AttributeError, TypeError, IndexError) as err:
            print('Error: {}'.format(err))

    def paralizar(self, oponente):
        try:
            print('\n=== VEHICULOS MARITIMOS '
                  'CON GBU-43/B Massive Ordnance '
                  'Air Blast Paralizer ===')
            v_paralizadores = self.mostrar_flota_paralizadora()

            if len(v_paralizadores) == 0:
                raise AttributeError('Ningun vehiculo tiene GBU-43/B '
                                     'Massive Ordnance Air Blast Paralizer')

            vehiculo_paralizador = input('Ingrese el numero del '
                                         'vehiculo con el que quiere '
                                         'paralizar: ')

            if not vehiculo_paralizador.isdigit():
                raise TypeError('No es un numero valido')

            vehiculo_paralizador = int(vehiculo_paralizador)
            if vehiculo_paralizador >= len(v_paralizadores):
                raise TypeError('No existe el numero {}'
                                ' en las opciones'.
                                format(vehiculo_paralizador))

            vehiculo_paralizador_inst = v_paralizadores[vehiculo_paralizador]

            paralizer_inst = None
            for ataque in vehiculo_paralizador_inst.ataques:
                if ataque.nombre == 'GBU-43/B Massive Ordnance ' \
                                    'Air Blast Paralizer':
                    paralizer_inst = ataque
                    break

            if not paralizer_inst:
                raise AttributeError('Ningun vehiculo tiene el paralizador.')

            cs = input('Ingrese las dos coordenadas a las que '
                       'quiere enviar el paralizador [i,j h,k]: ')
            if ' ' not in cs:
                raise TypeError('Coordenadas invalidas')

            cs_lista = cs.split(' ')
            if len(cs_lista) != 2:
                raise TypeError('Coordenadas invalidas')

            cs1 = cs_lista[0]
            cs2 = cs_lista[1]
            if ',' not in cs1 or ',' not in cs2:
                raise TypeError('Coordenadas invalidas')

            cs1_lista = cs1.split(',')
            cs2_lista = cs2.split(',')
            if len(cs1_lista) != 2 or len(cs2_lista) != 2:
                raise TypeError('Coordenadas invalidas')

            c1i = cs1_lista[0]
            c1j = cs1_lista[1]
            c2i = cs2_lista[0]
            c2j = cs2_lista[1]
            if not (c1i.isdigit()
                    and c1j.isdigit()
                    and c2i.isdigit()
                    and c2j.isdigit()):
                raise TypeError('Coordenadas invalidas, '
                                'deben ser numeros.')

            c1i = int(c1i)
            c1j = int(c1j)
            c2i = int(c2i)
            c2j = int(c2j)
            if c1i >= self.mapa.n \
                    or c1j >= self.mapa.n \
                    or c2i >= self.mapa.n \
                    or c2j >= self.mapa.n:
                raise IndexError('Alguna coordenada no esta'
                                 ' dentro de las dimensiones del '
                                 'mapa')

            aire_oponente = oponente.mapa.sector['aereo']

            aciertos = 0
            if aire_oponente[c1i][c1j] == 'E' \
                    or aire_oponente[c1i][c1j] == 'e':
                aciertos += 1
            if aire_oponente[c2i][c2j] == 'E' \
                    or aire_oponente[c2i][c2j] == 'e':
                aciertos += 1

            if aciertos < 2:
                print('\n--- El ataque paralizador ha fallado. ---\n')

            elif aciertos == 2:
                avion_paralizado = None
                for vehiculo in oponente.flota_activa:
                    if vehiculo.nombre == 'Avion Explorador':
                        avion_paralizado = vehiculo
                        break
                avion_paralizado.paralizar()
                print('\n--- Se ha paralizado exitosamente '
                      'por 5 turnos el Avion Explorador enemigo'
                      ' ---\n')
                paralizer_inst.exitos += 1

            paralizer_inst.usadas += 1
            paralizer_inst.usar()

            self.terminar_turno()

        except (AttributeError, TypeError, IndexError) as err:
            print('Error: {}'.format(err))

    def terminar_turno(self):
        # Si hay ataques usados esperando turnos,
        # se les disminuye un turno.
        # Si el Avion Explorador esta paralizado,
        # se disminuye un turno paralizado.
        for vehiculo in self.flota_activa:
            for ataque in vehiculo.ataques:
                if ataque.turnos_pendientes:
                    ataque.turnos_pendientes -= 1
            if vehiculo.nombre == 'Avion Explorador':
                if vehiculo.turnos_paralizado:
                    vehiculo.turnos_paralizado -= 1

        # Se agrega el estado del radar al historial de radares.
        self.radares.append(deepcopy(self.radar))

        # Se agrega un turno al jugador.
        self.turnos += 1

    @property
    def damage_total_recibido(self):
        dam = 0
        for vehiculo in self.flota_activa:
            if vehiculo.tipo == 'maritimo':
                dam += vehiculo.damage_recibido
        for vehiculo in self.flota_muerta:
            if vehiculo.tipo == 'maritimo':
                dam += vehiculo.damage_recibido
        return dam

    @property
    def ataques_mas_utilizados(self):
        ataques_contados = {}
        for vehiculo in self.flota_activa:
            for ataque in vehiculo.ataques:
                if ataque.nombre not in ataques_contados:
                    ataques_contados.update({ataque.nombre: ataque.usadas})
                else:
                    ataques_contados[ataque.nombre] += ataque.usadas
        for vehiculo in self.flota_muerta:
            for ataque in vehiculo.ataques:
                if ataque.nombre not in ataques_contados:
                    ataques_contados.update({ataque.nombre: ataque.usadas})
                else:
                    ataques_contados[ataque.nombre] += ataque.usadas

        ataques_contados = ataques_contados.items()

        maximos_usos = max(ataques_contados, key=itemgetter(1))[1]

        mas_utilizados = []

        for ataque in ataques_contados:
            if ataque[1] == maximos_usos:
                mas_utilizados.append(ataque[0])

        return mas_utilizados, maximos_usos

    @property
    def barcos_mas_movidos(self):
        vehiculos_contados = {}
        for vehiculo in self.flota_activa:
            if vehiculo.tipo == 'maritimo':
                if vehiculo.nombre not in vehiculos_contados:
                    vehiculos_contados.update({vehiculo.nombre: vehiculo.movimientos})
                else:
                    vehiculos_contados[vehiculo.nombre] += vehiculo.movimientos
        for vehiculo in self.flota_muerta:
            if vehiculo.tipo == 'maritimo':
                if vehiculo.nombre not in vehiculos_contados:
                    vehiculos_contados.update({vehiculo.nombre: vehiculo.movimientos})
                else:
                    vehiculos_contados[vehiculo.nombre] += vehiculo.movimientos

        vehiculos_contados = vehiculos_contados.items()

        maximos_movs = max(vehiculos_contados, key=itemgetter(1))[1]

        mas_movidos = []

        for vehiculo in vehiculos_contados:
            if vehiculo[1] == maximos_movs:
                mas_movidos.append(vehiculo[0])

        return mas_movidos, maximos_movs

    @property
    def ataques_mas_eficientes(self):
        ataques_usadas_damage = {}  # {nombre_ataque: [usadas, damage_efectivo]}
        for vehiculo in self.flota_activa:
            for ataque in vehiculo.ataques:
                if ataque.nombre not in ataques_usadas_damage:
                    ataques_usadas_damage.update({ataque.nombre: [ataque.usadas, ataque.damage_efectivo]})
                else:
                    ataques_usadas_damage[ataque.nombre][0] += ataque.usadas
                    ataques_usadas_damage[ataque.nombre][1] += ataque.damage_efectivo
        for vehiculo in self.flota_muerta:
            for ataque in vehiculo.ataques:
                if ataque.nombre not in ataques_usadas_damage:
                    ataques_usadas_damage.update({ataque.nombre: [ataque.usadas, ataque.damage_efectivo]})
                else:
                    ataques_usadas_damage[ataque.nombre][0] += ataque.usadas
                    ataques_usadas_damage[ataque.nombre][1] += ataque.damage_efectivo

        for data in ataques_usadas_damage:
            usadas = ataques_usadas_damage[data][0]
            damage_efectivo = ataques_usadas_damage[data][1]
            if usadas != 0:
                efectividad = damage_efectivo / usadas
                ataques_usadas_damage.update({data: efectividad})
            else:
                ataques_usadas_damage.update({data: 0})

        ataques_efe = ataques_usadas_damage.items()

        max_efe = max(ataques_efe, key=itemgetter(1))[1]

        mas_efectivos = []

        for ataque in ataques_efe:
            if ataque[1] == max_efe:
                mas_efectivos.append(ataque[0])

        return mas_efectivos, max_efe

    def mostrar_estadisticas(self, oponente):
        # Datos Base:
        n_ataques_totales = 0
        n_ataques_exitosos = 0
        for vehiculo in self.flota_activa:
            for ataque in vehiculo.ataques:
                n_ataques_totales += ataque.usadas
                n_ataques_exitosos += ataque.exitos
        for vehiculo in self.flota_muerta:
            for ataque in vehiculo.ataques:
                n_ataques_totales += ataque.usadas
                n_ataques_exitosos += ataque.exitos

        # 1. Porcentaje Ataques Exitosos:
        if n_ataques_totales != 0:
            p_ataques_exitosos = round((n_ataques_exitosos / n_ataques_totales) * 100, 2)
            print('  (1) Porcentaje ataques exitosos: {}%'.format(p_ataques_exitosos))
        else:
            print('  (1) Porcentaje ataques exitosos: NO HUBO ATAQUES')

        # 2. Porcentaje Ataques Exitosos por barco y avion:
        print('  (2) Porcentaje de ataques exitosos por barco y avion:')
        for vehiculo in self.flota_activa:
            print('    ->  {0}: {1}'.
                  format(vehiculo.nombre,
                         vehiculo.ptje_ataques_exitosos))
        for vehiculo in self.flota_muerta:
            print('    ->  {0}: {1}'.
                  format(vehiculo.nombre,
                         vehiculo.ptje_ataques_exitosos))

        # 3. Damage recibido por cada barco:
        print('  (3) Damage recibido por cada barco:')
        for vehiculo in self.flota_activa:
            if vehiculo.tipo == 'maritimo':
                print('    ->  {0}: {1}'.
                      format(vehiculo.nombre,
                             vehiculo.damage_recibido))
        for vehiculo in self.flota_muerta:
            if vehiculo.tipo == 'maritimo':
                print('    ->  {0}: {1}'.
                      format(vehiculo.nombre,
                             vehiculo.damage_recibido))

        # 4. Damage total causado:
        damage_total_causado = oponente.damage_total_recibido
        print('  (4) Damage total causado: {0}'.
              format(damage_total_causado))

        # 5. Damage total recibido:
        damage_total_recibido = self.damage_total_recibido
        print('  (5) Damage total recibido: {0}'.
              format(damage_total_recibido))

        # 6. Ataques mas utilizados:
        ataques_mas_utilizados = self.ataques_mas_utilizados[0]
        max_usos = self.ataques_mas_utilizados[1]
        print('  (6) Ataques mas utilizados:')
        for ataque in ataques_mas_utilizados:
            print('    -> {0}: {1} usadas'.
                  format(ataque, max_usos))

        # 7. Barco con mas movimientos:
        barcos_mas_movidos = self.barcos_mas_movidos[0]
        max_movs = self.barcos_mas_movidos[1]
        print('  (7) Barcos con mas movimientos:')
        for barco in barcos_mas_movidos:
            print('    -> {0}: {1} movimientos'.
                  format(barco, max_movs))

        # 8. Cantidad de turnos:
        print('  (8) Cantidad de turnos: {}'.
              format(self.turnos))

        # 9. Ataque mas eficiente:
        mas_eficientes = self.ataques_mas_eficientes[0]
        max_efe = self.ataques_mas_eficientes[1]
        print('  (9) Ataques mas eficientes:')
        for ataque in mas_eficientes:
            print('    -> {0}: {1} puntos de eficiencia'.
                  format(ataque, round(max_efe, 2)))

    def verificar_fracaso(self):
        if len(self.flota_activa_maritima) == 0:
            self.loser = True
            return True
        if len(self.flota_activa_maritima) == 1:
            if self.flota_activa_maritima[0].nombre == 'Lancha':
                self.loser = True
                return True
        return False
