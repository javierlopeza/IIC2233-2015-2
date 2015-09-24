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
                    i_random = randint(0, self.mapa.n)
                    j_random = randint(0, self.mapa.n)
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
        opciones = {'1': self.ver_mapa,
                    '2': self.ver_radar,
                    '3': self.revisar_historial_radar,
                    '4': self.revisar_casillas_espiadas,
                    '5': self.mover_vehiculo,
                    '6': self.atacar
                    }

        proximo_indice = 7

        for vehiculo in self.flota_activa:
            if vehiculo.nombre == 'Puerto':
                opciones.update({'7': self.kit_ingenieros})
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

        opciones.update({str(proximo_indice): self.terminar_turno})

        eleccion = self.elegir_opcion(opciones)
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

    def elegir_opcion(self, opciones):
        pass

    def paralizar(self, oponente):
        try:

            v_paralizadores = self.mostrar_flota_paralizadora()

            if len(v_paralizadores) == 0:
                raise AttributeError('Ningun vehiculo tiene GBU-43/B '
                                     'Massive Ordnance Air Blast Paralizer')

            vehiculo_paralizador = randint(0, len(v_paralizadores))

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
                self.casillas_claves = [[c1i, c1j], [c2i, c2j]]
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