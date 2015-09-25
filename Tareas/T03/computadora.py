from random import choice, randint
from jugador import Jugador


class Computadora(Jugador):
    def __init__(self):
        super().__init__()
        self.nombre = 'Computadora'
        self.id = 2
        self.exp_enemigo_turnos_paralizado = 0

    def posicionar_vehiculos(self):
        try:
            if not self.mapa:
                raise AttributeError('La computadora no tiene mapa.')

            if not self.flota:
                raise AttributeError('La computadora no tiene flota de vehiculos.')

            for vehiculo in self.flota:
                vehiculo.setear_orientacion(choice(['h', 'v']))
                while not vehiculo.casillas_usadas:
                    i_random = randint(0, self.mapa.n - 1)
                    j_random = randint(0, self.mapa.n - 1)
                    ij = '{0},{1}'.format(i_random, j_random)
                    self.mapa.agregar_vehiculo(vehiculo, ij)

        except AttributeError as err:
            print('Error: {}', err)

    def jugar(self, oponente):
        turno_actual = self.turnos
        # Mientras no termine el turno, que juegue.
        while self.turnos == turno_actual:
            print('\n === TURNO {} COMPUTADORA -> JUGANDO... ==='.format(self.turnos + 1))
            self.display_menu(oponente)

    def display_menu(self, oponente):
        opciones = {'1': self.puede_atacar,
                    '2': self.mover_espiado
                    }

        proximo_indice = 3

        for vehiculo in self.flota_activa:
            if vehiculo.nombre == 'Avion Explorador':
                if vehiculo.turnos_paralizado == 1:
                    opciones.update({str(proximo_indice): self.mover_avion_paralizado})
                    proximo_indice += 1
            break

        for vehiculo in self.flota_activa:
            if vehiculo.nombre == 'Avion Explorador':
                if vehiculo.turnos_paralizado == 0:
                    opciones.update({str(proximo_indice): self.explorar})
                    proximo_indice += 1
                break

        opciones.update({str(proximo_indice): self.paralizar})
        proximo_indice += 1

        for vehiculo in self.flota_activa:
            if vehiculo.nombre == 'Puerto':
                for ataque in vehiculo.ataques:
                    if ataque.nombre == 'Kit de Ingenieros':
                        if ataque.disponible:
                            for veh in self.flota_activa:
                                if veh.vida < veh.resistencia:
                                    opciones.update({str(proximo_indice): self.kit_ingenieros})
                                    proximo_indice += 1
                                    break
                    break
                break

        opciones.update({str(proximo_indice): self.terminar_turno})

        for d in range(1, len(opciones) + 1):
            eleccion = str(d)
            accion = opciones.get(eleccion)
            if accion:
                if accion.__name__ == 'puede_atacar' \
                        or accion.__name__ == 'explorar' \
                        or accion.__name__ == 'paralizar':
                    if accion(oponente):
                        break
                else:
                    if accion():
                        break
            else:
                print("\n--- {0} no es una opcion valida ---\n".format(
                    eleccion))

    def puede_atacar(self, oponente):
        casilla_destino = None
        for i in range(self.mapa.n):
            for j in range(self.mapa.n):
                if self.radar.sector['maritimo'][i][j] == 'A':
                    casilla_destino = [[i, j]]

        if not casilla_destino:
            for i in range(self.mapa.n):
                for j in range(self.mapa.n):
                    if self.radar.sector['maritimo'][i][j] == 'F':
                        casilla_destino = [[i, j]]

        if not casilla_destino:
            return False

        ataques_disponibles = {}
        for vehiculo in self.flota_activa:
            for ataque in vehiculo.ataques:
                if ataque.nombre not in ataques_disponibles \
                        and ataque.disponible:
                    ataques_disponibles.update({ataque.nombre: [ataque, vehiculo]})

        vehiculo_usar = None
        ataque_usar = None
        if ataques_disponibles:
            if 'Kamikaze' in ataques_disponibles:
                ataque_usar = ataques_disponibles['Kamikaze'][0]
                vehiculo_usar = ataques_disponibles['Kamikaze'][1]
            elif 'Misil Balistico Intercontinental Minuteman III' in ataques_disponibles:
                ataque_usar = ataques_disponibles['Misil Balistico Intercontinental Minuteman III'][0]
                vehiculo_usar = ataques_disponibles['Misil Balistico Intercontinental Minuteman III'][1]
            elif 'Misil de crucero BGM-109 Tomahawk' in ataques_disponibles:
                ataque_usar = ataques_disponibles['Misil de crucero BGM-109 Tomahawk'][0]
                vehiculo_usar = ataques_disponibles['Misil de crucero BGM-109 Tomahawk'][1]
            elif 'Misil UGM-133 Trident II' in ataques_disponibles:
                ataque_usar = ataques_disponibles['Misil UGM-133 Trident II'][0]
                vehiculo_usar = ataques_disponibles['Misil UGM-133 Trident II'][1]
            elif 'Napalm' in ataques_disponibles:
                ataque_usar = ataques_disponibles['Napalm'][0]
                vehiculo_usar = ataques_disponibles['Napalm'][1]

        casillas_dest = casilla_destino
        if ataque_usar.nombre == 'Misil de crucero BGM-109 Tomahawk':
            casillas_dest = []
            foc = choice(['f', 'c'])
            if foc == 'c':
                for j in range(self.mapa.n):
                    casillas_dest.append([casilla_destino[0][0], j])
            elif foc == 'f':
                for i in range(self.mapa.n):
                    casillas_dest.append([i, casilla_destino[0][1]])

        self.atacar(oponente, vehiculo_usar, ataque_usar, casillas_dest)

        return True

    def mover_espiado(self):
        simbolo_esp = None
        for c_esp in self.casillas_espiadas:
            cei = c_esp[0]
            cej = c_esp[1]
            if self.mapa.sector['maritimo'][cei][cej] != '~':
                simbolo_esp = self.mapa.sector['maritimo'][cei][cej]
                break

        if not simbolo_esp:
            return False

        for vehiculo in self.flota_activa:
            if vehiculo.simbolo == simbolo_esp.upper():
                vehiculo_esp = vehiculo
                break

        casillas_prev = vehiculo_esp.casillas_usadas

        while casillas_prev == vehiculo_esp.casillas_usadas:
            imov = randint(0, self.mapa.n - 1)
            jmov = randint(0, self.mapa.n - 1)
            ij = '{0},{1}'.format(imov, jmov)
            self.mapa.mover_vehiculo(vehiculo_esp, ij)

        self.casillas_espiadas = []

        self.terminar_turno()

        print('\n--- La computadora ya realizo una accion. ---\n')

        return True

    def mover_avion_paralizado(self):
        for vehiculo in self.flota_activa:
            if vehiculo.nombre == 'Avion Explorador':
                if vehiculo.turnos_paralizado == 1:
                    avion_exp = vehiculo

            break

        casillas_prev = avion_exp.casillas_usadas

        while casillas_prev == avion_exp.casillas_usadas:
            imov = randint(0, self.mapa.n - 1)
            jmov = randint(0, self.mapa.n - 1)
            ij = '{0},{1}'.format(imov, jmov)
            self.mapa.mover_vehiculo(avion_exp, ij)

        self.terminar_turno()

        return True

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

            v_reparables = self.mostrar_flota_maritima_reparable()

            if len(v_reparables) == 0:
                raise ValueError('No hay ningun vehiculo maritimo'
                                 ' que se pueda reparar.')

            vehiculo_reparar = randint(0, len(v_reparables) - 1)

            vehiculo_reparar_inst = v_reparables[vehiculo_reparar]

            vida_previa = vehiculo_reparar_inst.vida
            kit.usar()
            vehiculo_reparar_inst.vida += 1

            print('\n--- El vehiculo {0} aumento su vida '
                  'de {1} a {2} gracias al Kit de Ingenieros usado por la Computadora ---'.
                  format(vehiculo_reparar_inst.nombre,
                         vida_previa,
                         vehiculo_reparar_inst.vida))

            self.terminar_turno()

            return True

        except (AttributeError, IndexError, TypeError, ValueError) as err:
            print('Error: {}'.format(err))

    def paralizar(self, oponente):
        try:
            v_paralizadores = self.mostrar_flota_paralizadora()

            if len(v_paralizadores) == 0:
                raise AttributeError('Ningun vehiculo tiene GBU-43/B '
                                     'Massive Ordnance Air Blast Paralizer')

            vehiculo_paralizador = randint(0, len(v_paralizadores) - 1)

            vehiculo_paralizador_inst = v_paralizadores[vehiculo_paralizador]

            paralizer_inst = None
            for ataque in vehiculo_paralizador_inst.ataques:
                if ataque.nombre == 'GBU-43/B Massive Ordnance ' \
                                    'Air Blast Paralizer':
                    paralizer_inst = ataque
                    break

            if not paralizer_inst:
                raise AttributeError('Ningun vehiculo tiene el paralizador.')

            for fila in self.mapa.sector['aereo']:
                for casilla in fila:
                    if casilla == 'E' or casilla == 'e':
                        c1i = self.mapa.sector['aereo'].index(fila)
                        c1j = fila.index(casilla)
                        break

            c2i = c1i + randint(0, 1)
            c2j = c1j + randint(0, 1)

            while c1i >= self.mapa.n \
                    or c1j >= self.mapa.n \
                    or c2i >= self.mapa.n \
                    or c2j >= self.mapa.n:
                c2i = c1i + randint(0, 1)
                c2j = c1j + randint(0, 1)

            aire_oponente = oponente.mapa.sector['aereo']

            aciertos = 0
            if aire_oponente[c1i][c1j] == 'E' \
                    or aire_oponente[c1i][c1j] == 'e':
                aciertos += 1
            if aire_oponente[c2i][c2j] == 'E' \
                    or aire_oponente[c2i][c2j] == 'e':
                aciertos += 1

            elif aciertos == 2:
                for vehiculo in oponente.flota_activa:
                    if vehiculo.nombre == 'Avion Explorador':
                        avion_paralizado = vehiculo
                        break
                avion_paralizado.paralizar()
                print('\n--- La Computadora ha paralizado exitosamente '
                      'por 5 turnos el Avion Explorador de {}'
                      ' ---\n'.format(oponente.nombre))
                paralizer_inst.exitos += 1

            paralizer_inst.usadas += 1
            paralizer_inst.usar()

            self.terminar_turno()

            return True

        except (AttributeError, TypeError, IndexError) as err:
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
                raise AttributeError('El jugador {0} no tiene Avion Explorador'.
                                     format(self.nombre))

            if explorador.turnos_paralizado:
                raise AttributeError('El Avion Explorador esta paralizado. '
                                     'Quedan {} turnos para que vuelva a estar'
                                     ' disponible.'.
                                     format(explorador.turnos_paralizado))

            icentral = randint(0, self.mapa.n - 1)
            jcentral = randint(0, self.mapa.n - 1)

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

            algo_encontrado = False
            for casilla in casillas_explorar:
                iexp = casilla[0]
                jexp = casilla[1]
                if oponente.mapa.sector['maritimo'][iexp][jexp] != '~':
                    algo_encontrado = True
                    oponente.casillas_espiadas.append([iexp, jexp])
                    print('--- La Computadora encontro una pieza de un vehiculo tuyo'
                          ' en la casilla ({0}, {1}) y '
                          'se guardo en tus Casillas Espiadas ---'.
                          format(iexp, jexp))
                    self.radar.sector['maritimo'][iexp][jexp] = 'F'

            if not algo_encontrado:
                print('--- La Computadora exploro y no encontro nada. ---')

            revelar_coordenada = randint(0, 1)

            if revelar_coordenada:
                casilla_revelada = choice(explorador.casillas_usadas)
                ir = casilla_revelada[0]
                jr = casilla_revelada[1]
                print('\n--- El Avion Explorador de la Computadora '
                      'ha revelado la '
                      'coordenada ({0}, {1}), '
                      'quedando esta registrada'
                      ' en el tu radar como E ---\n'.
                      format(ir, jr))
                oponente.radar.sector['aereo'][ir][jr] = 'E'

            else:
                print('\n--- El Avion Explorador de la Computadora fue discreto '
                      'y no revelo ninguna coordenada ---\n')

            self.terminar_turno()

            return True

        except (AttributeError, TypeError, IndexError) as err:
            print('Error: {}'.format(err))
