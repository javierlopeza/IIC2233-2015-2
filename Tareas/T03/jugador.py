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
                break

        print(menu_impreso)

        eleccion = input("Ingrese Opcion: ")
        accion = opciones.get(eleccion)
        if accion:
            if accion.__name__ == 'atacar':
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
        print(' X: Ataque Efectivo  |  O: Ataque Fallado')

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

            exito = 'NO fue exitoso'
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
                            exito = 'fue exitoso'
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
                            if vehiculo_victima.vida == 0:
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
                            if not es_tom:
                                self.radar.marcar('maritimo', ii, jj, 'X')
                            break

            if not ataque_elegido_inst.nombre == 'Misil de crucrero' \
                                                 ' BGM-109 Tomahawk':
                print('\n--- El ataque cayo en {0} '
                      'en las coordenadas ({1}, {2}) ---'.
                      format(retornar,
                             ii,
                             jj))
            else:
                print('\n--- El ataque {} ---'.format(exito))

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

            print('\n=== VEHICULOS MARITIMOS REPARABLES CON EL KIT DE INGENIEROS ===')
            v_reparables = self.mostrar_flota_maritima_reparable()

            if len(v_reparables) == 0:
                raise Exception('No hay ningun vehiculo maritimo que se pueda reparar.')

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

        except Exception as err:
            print('Error: {}'.format(err))

    def explorar(self):
        self.terminar_turno()

    def terminar_turno(self):
        # Se agrega un turno al jugador.
        self.turnos += 1

        # Si hay ataques usados esperando turnos, se les disminuye un turno.
        for vehiculo in self.flota_activa:
            for ataque in vehiculo.ataques:
                if ataque.turnos_pendientes:
                    ataque.turnos_pendientes -= 1
