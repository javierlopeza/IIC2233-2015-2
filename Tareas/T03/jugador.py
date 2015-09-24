from random import randint, choice


class Jugador:
    def __init__(self, nombre, ide):
        self.nombre = nombre
        self.id = ide
        self.mapa = None
        self.radar = None
        self.flota = None
        self.flota_activa = []
        self.flota_muerta = []
        self.turnos = 0

    def jugar(self, oponente):
        turno_actual = self.turnos

        # Mientras no termine el turno, que juegue.
        # El turno termina al atacar, mover vehiculo,
        # explorar o usar el Kit.
        while self.turnos == turno_actual:
            print('\n === TURNO {2} PLAYER {0}: {1} -> JUEGUE ==='.format(
                self.id, self.nombre, self.turnos + 1))
            self.display_menu(oponente)

    def display_menu(self, oponente):
        opciones = {'1': self.ver_mapa,
                    '2': self.ver_radar,
                    '3': self.mover_vehiculo,
                    '4': self.atacar
                    }

        menu_impreso = '  [1]: Ver Mi Mapa\n' \
                       '  [2]: Ver Radar\n' \
                       '  [3]: Mover Vehiculo\n' \
                       '  [4]: Atacar Oponente\n'

        proximo_indice = 5

        for vehiculo in self.flota_activa:
            if vehiculo.nombre == 'Puerto':
                opciones.update({'5': self.kit_ingenieros})
                menu_impreso += '  [5]: Usar Kit de Ingenieros\n'
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

    def mostrar_flota_activa(self):
        try:
            if not self.flota_activa:
                raise Exception('No se han cargado los vehiculos a la flota')

            ret = ''
            for vehiculo in self.flota_activa:
                ret += '  [{0}]: {1}\n'.format(
                    self.flota_activa.index(vehiculo),
                    vehiculo.nombre)
            print(ret)

        except Exception as err:
            print('Error: {}'.format(err))

    def mostrar_flota_movible(self):
        try:
            if not self.flota_activa:
                raise Exception('No se han cargado los vehiculos a la flota')

            n_movibles = 0
            ret = ''
            for vehiculo in self.flota_activa:
                if vehiculo.movimientos != 0:
                    n_movibles += 1
                    ret += '  [{0}]: {1}\n'.format(
                        self.flota_activa.index(vehiculo),
                        vehiculo.nombre)
            print(ret)
            self.n_movibles = n_movibles

        except Exception as err:
            print('Error: {}'.format(err))

    def mostrar_flota_maritima_reparable(self):
        try:
            if not self.flota_activa:
                raise Exception('No se han cargado los vehiculos a la flota')

            v_reparables = []
            ret = ''
            for vehiculo in self.flota_activa:
                if vehiculo.tipo == 'maritimo' and vehiculo.vida < vehiculo.resistencia:
                    v_reparables.append(vehiculo)
                    ret += '  [{0}]: {1}\n'.format(
                        self.flota_activa.index(vehiculo),
                        vehiculo.nombre)
            print(ret)
            return v_reparables

        except Exception as err:
            print('Error: {}'.format(err))

    def mostrar_flota_paralizadora(self):
        try:
            if not self.flota_activa:
                raise Exception('No se han cargado los vehiculos a la flota')

            v_paralizadores = []
            ret = ''
            for vehiculo in self.flota_activa:
                for ataque in vehiculo.ataques:
                    if ataque.nombre == 'GBU-43/B Massive ' \
                                        'Ordnance Air Blast ' \
                                        'Paralizer':
                        v_paralizadores.append(vehiculo)
                        ret += '  [{0}]: {1}\n'.format(
                            self.flota_activa.index(vehiculo),
                            vehiculo.nombre)
                        break
            print(ret)
            return v_paralizadores

        except Exception as err:
            print('Error: {}'.format(err))

    @property
    def flota_activa_maritima(self):
        try:
            if not self.flota_activa:
                raise Exception('La flota esta vacia')

            v_maritimos = []
            for vehiculo in self.flota_activa:
                if vehiculo.tipo == 'maritimo':
                    v_maritimos.append(vehiculo)

            return v_maritimos

        except Exception as err:
            print('Error: {}'.format(err))

    def mover_vehiculo(self):
        try:
            if not self.flota_activa:
                raise Exception('La flota no esta cargada.')

            print('\n=== VEHICULOS QUE SE PUEDEN MOVER ===')
            self.mostrar_flota_movible()

            vehiculo_mover = input('Ingrese el numero del vehiculo '
                                   'que desea mover: ')
            if not vehiculo_mover.isdigit():
                raise TypeError('La opcion {} '
                                'no es un numero'.
                                format(vehiculo_mover))

            vehiculo_mover = int(vehiculo_mover)
            if not vehiculo_mover < self.n_movibles:
                raise IndexError('El numero {} no esta '
                                 'dentro de las opciones'.
                                 format(vehiculo_mover))

            vehiculo_mover_inst = self.flota_activa[vehiculo_mover]
            mover = self.mapa.mover_vehiculo(
                vehiculo_mover_inst)
            if mover:
                print('--- El vehiculo {0} se movio '
                      'correctamente a la posicion ({1}, {2}) ---'.
                      format(vehiculo_mover_inst.nombre, mover[0], mover[1]))
                self.terminar_turno()

        except (Exception, TypeError, IndexError) as err:
            print('Error: {}'.format(err))

    def atacar(self, oponente):
        try:
            if not self.flota_activa:
                raise Exception('La flota no esta cargada.')

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
                    raise Exception('La casilla no se encuentra '
                                    'en el mapa oponente.')
                casillas_atacadas = [[ii, jj]]

            else:
                es_tom = True
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
                                for casilla in vehiculo_victima.casillas_usadas:
                                    iii = casilla[0]
                                    jjj = casilla[1]
                                    self.radar.marcar('maritimo', iii, jjj, 'X')
                            # Si sigue con vida se retorna el exito
                            # del ataque.
                            else:
                                retornar = 'un vehiculo'
                            if not es_tom and not vehiculo_destruido:
                                self.radar.marcar('maritimo', ii, jj, 'A')
                            break

            if not ataque_elegido_inst.nombre == 'Misil de crucrero' \
                                                 ' BGM-109 Tomahawk':
                print('\n--- El ataque cayo en {0} '
                      'en las coordenadas ({1}, {2}) ---'.
                      format(retornar,
                             ii,
                             jj))
            else:
                if exito:
                    print('\n--- El ataque fue exitoso '
                          'y se afectaron {0} piezas enemigas ---'.
                          format(n_piezas_afectadas))
                else:
                    print('\n--- El ataque NO fue exitoso')

            if ataque_elegido_inst.nombre == 'Kamikaze':
                # El Kamikaze IXXI muere luego de atacar.
                self.mapa.eliminar_vehiculo(vehiculo_atacador_inst, 'aereo')
                self.flota_muerta.append(vehiculo_atacador_inst)
                self.flota_activa.remove(vehiculo_atacador_inst)

        except (Exception, TypeError, IndexError) as err:
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
                raise Exception('El jugador {0} no tiene Puerto'.
                                format(self.nombre))

            kit = None
            for ataque in puerto.ataques:
                if ataque.nombre == 'Kit de Ingenieros':
                    kit = ataque
                    break

            if not kit:
                raise Exception('El Puerto no posee Kit de Ingenieros')

            if not kit.disponible:
                raise Exception('El Kit de Ingenieros no esta disponible'
                                ' para ser usado este turno. '
                                'Quedan {} turnos para que vuelva a estar'
                                'disponible.'.format(kit.turnos_pendientes))

            print('\n=== VEHICULOS MARITIMOS REPARABLES CON '
                  'EL KIT DE INGENIEROS ===')
            v_reparables = self.mostrar_flota_maritima_reparable()

            if len(v_reparables) == 0:
                raise Exception('No hay ningun vehiculo maritimo'
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

        except (Exception, IndexError, TypeError) as err:
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
                raise Exception('El jugador {0} no tiene Avion Explorador'.
                                format(self.nombre))

            if explorador.turnos_paralizado:
                raise Exception('El Avion Explorador esta paralizado. '
                                'Quedan {} turnos para que vuelva a estar'
                                ' disponible.'.
                                format(explorador.turnos_paralizado))

            ij_explorar = input('Ingrese la coordenada central '
                                'del area de 3x3 a explorar [i,j]: ')

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

            casillas_explorar = []
            for n in range(2):
                for m in range(2):
                    c1 = [icentral + n, jcentral + m]
                    if self.mapa.n > (icentral + n) >= 0:
                        if self.mapa.n > jcentral + m >= 0:
                            if c1 not in casillas_explorar:
                                casillas_explorar.append(c1)
                    c2 = [icentral - n, jcentral - m]
                    if self.mapa.n > icentral - n >= 0:
                        if self.mapa.n > jcentral - m >= 0:
                            if c2 not in casillas_explorar:
                                casillas_explorar.append(c2)
                    c3 = [icentral - n, jcentral + m]
                    if self.mapa.n > icentral - n >= 0:
                        if self.mapa.n > jcentral + m >= 0:
                            if c3 not in casillas_explorar:
                                casillas_explorar.append(c3)
                    c4 = [icentral + n, jcentral - m]
                    if self.mapa.n > icentral + n >= 0:
                        if self.mapa.n > jcentral - m >= 0:
                            if c4 not in casillas_explorar:
                                casillas_explorar.append(c4)

            for casilla in casillas_explorar:
                iexp = casilla[0]
                jexp = casilla[1]
                if oponente.mapa.sector['maritimo'][iexp][jexp] != '~':
                    print('--- Se encontro una pieza de vehiculo enemigo'
                          ' en la casilla ({0}, {1}) y '
                          'se guardo en el radar como F ---'.
                          format(iexp, jexp))
                    self.radar.sector['maritimo'][iexp][jexp] = 'F'

            revelar_coordenada = randint(0, 1)

            if revelar_coordenada:
                casilla_revelada = choice(explorador.casillas_usadas)
                ir = casilla_revelada[0]
                jr = casilla_revelada[1]
                print('\n--- El Avion Explorador ha revelado la '
                      'coordenada ({0}, {1}) a tu oponente, '
                      'quedando esta registrada'
                      ' en el radar enemigo como E ---\n'.
                      format(ir, jr))
                oponente.radar.sector['aereo'][ir][jr] = 'E'

            else:
                print('\n--- El Avion Explorador fue discreto '
                      'y no revelo ninguna coordenada ---\n')

            self.terminar_turno()

        except (Exception, TypeError, IndexError) as err:
            print('Error: {}'.format(err))

    def paralizar(self, oponente):
        try:
            print('\n=== VEHICULOS MARITIMOS '
                  'CON GBU-43/B Massive Ordnance '
                  'Air Blast Paralizer ===')
            v_paralizadores = self.mostrar_flota_paralizadora()

            if len(v_paralizadores) == 0:
                raise Exception('Ningun vehiculo tiene GBU-43/B '
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
                raise Exception('Ningun vehiculo tiene el paralizador.')

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

            paralizer_inst.usadas += 1
            paralizer_inst.usar()

            self.terminar_turno()


        except (Exception, TypeError, IndexError) as err:
            print('Error: {}'.format(err))

    def terminar_turno(self):
        # Se agrega un turno al jugador.
        self.turnos += 1

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

    def verificar_fracaso(self):
        if len(self.flota_activa_maritima) == 0:
            return True
        if len(self.flota_activa_maritima) == 1:
            if self.flota_activa_maritima[0].nombre == 'Lancha':
                return True
        return False
