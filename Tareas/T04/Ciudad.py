# -*- encoding: utf-8 -*-
from gui.gui import GrillaSimulacion
from Casa import Casa
from Vehiculo import VehiculoComun, Taxi, VehiculoEmergencia
from Calle import Calle
from random import randint, choice
from copy import deepcopy


class Ciudad:
    def __init__(self, app):
        self.grilla = GrillaSimulacion(app)
        self.grilla.show()
        self.servicios = {'bomberos': None,
                          'policia': None,
                          'hospital': None}
        self.calles = {}
        self.casas = {}
        self.vehiculos = {}
        self.rellenar_ciudad_base()
        # self.grilla.tiempo_intervalo = float(input('Ingrese el intervalo de tiempo '
        #                                          'para los eventos en la simulacion: '))
        self.grilla.tiempo_intervalo = 0.01

    def rellenar_ciudad_base(self):

        def cargar_calles_casas(self):
            mapa_file = open('mapa.txt', 'r')
            lineas = mapa_file.readlines()
            for l in range(1, len(lineas)):
                x = int(lineas[l].split(' ')[0].split(',')[0])
                y = int(lineas[l].split(' ')[0].split(',')[1])
                entidad = lineas[l].split(' ')[1]
                if entidad == 'casa':
                    material = lineas[l].split(' ')[3]
                    duracion_robo = [int(i) for i in lineas[l].split('[')[1][:-2].split(', ')]
                    self.grilla.agregar_casa(y + 1, x + 1)
                    nueva_casa = Casa(material, duracion_robo)
                    self.casas.update({'{},{}'.format(y + 1, x + 1): nueva_casa})
                elif entidad == 'calle':
                    direccion = lineas[l].split(' ')[2][:-1]
                    self.grilla.agregar_calle(y + 1, x + 1)
                    nueva_calle = Calle(direccion)
                    self.calles.update({'{},{}'.format(y + 1, x + 1): nueva_calle})

            print('[GRILLA] Se cargaron {} calles y {} casas de mapa.txt'.format(len(self.calles), len(self.casas)))

        def clasificar_cruces(self):
            total_cruces = 0
            for pos_calle in self.calles:
                x = int(pos_calle.split(',')[0])
                y = int(pos_calle.split(',')[1])

                ob_izq = '{},{}'.format(x - 1, y)
                ob_der = '{},{}'.format(x + 1, y)
                ob_abajo = '{},{}'.format(x, y - 1)
                ob_arriba = '{},{}'.format(x, y + 1)

                # Cruce tipo + o T de 1 pista
                if ob_izq in self.calles and ob_der in self.calles:
                    if self.calles[ob_izq].direccion == self.calles[ob_der].direccion != self.calles[
                        pos_calle].direccion:
                        self.calles[pos_calle].cruce = True
                        total_cruces += 1

                if ob_abajo in self.calles and ob_arriba in self.calles:
                    if self.calles[ob_abajo].direccion \
                            == self.calles[ob_arriba].direccion \
                            != self.calles[pos_calle].direccion:
                        self.calles[pos_calle].cruce = True
                        total_cruces += 1

            # Cruces que no pude alcanzar e ingrese manualmente
            cruces_extra = [[2, 20], [8, 4], [9, 4], [12, 4], [13, 4],
                            [19, 4], [8, 8], [9, 8], [8, 13], [9, 13],
                            [12, 13], [13, 13], [19, 13], [8, 17], [9, 17],
                            [12, 17], [13, 17], [19, 17], [5, 20], [9, 20],
                            [12, 20], [13, 20], [16, 20], [19, 20]]
            for cruce in cruces_extra:
                self.calles['{},{}'.format(cruce[0], cruce[1])].cruce = True
                total_cruces += 1

            print('[GRILLA] Se encontraron y clasificaron {} cruces'.format(total_cruces))

        def poner_semaforos(self):
            total_semaforos = 0
            for pos_calle in self.calles:
                if self.calles[pos_calle].cruce:
                    # Si la calle corresponde a un cruce, se le agrega por defecto
                    # un semaforo activado en verde en sentido vertical.
                    self.calles[pos_calle].semaforo = ['arriba', 'abajo']
                    self.grilla.agregar_semaforo_vertical(int(pos_calle.split(',')[0]), int(pos_calle.split(',')[1]))
                    total_semaforos += 1

            print('[GRILLA] Se agregaron {} semaforos en los cruces'.format(total_semaforos))

        def cargar_autos_iniciales(self):
            autos_iniciales = randint(round(len(self.calles) / 4), round(len(self.calles) / 2) - randint(3, 8))
            for a in range(autos_iniciales):
                while True:
                    rnd_pos = choice(list(self.calles.keys()))
                    calle = self.calles[rnd_pos]
                    if not calle.vehiculos_encima['der'] and not calle.cruce:
                        pos = calle.pos_vehiculos
                        self.grilla.agregar_auto(int(rnd_pos.split(',')[0]), int(rnd_pos.split(',')[1]), pos[0], pos[1])
                        nuevo_vehiculo = VehiculoComun()
                        self.vehiculos.update({rnd_pos: nuevo_vehiculo})
                        calle.vehiculos_encima['der'] = nuevo_vehiculo
                        break

            print('[GRILLA] Se agregaron {} autos inicialmente'.format(autos_iniciales))

            taxis_iniciales = randint(1, round(len(self.calles) / 2) - autos_iniciales)
            for t in range(taxis_iniciales):
                while True:
                    rnd_pos = choice(list(self.calles.keys()))
                    calle = self.calles[rnd_pos]
                    if not calle.vehiculos_encima['der'] and not calle.cruce:
                        pos = calle.pos_vehiculos
                        self.grilla.agregar_taxi(int(rnd_pos.split(',')[0]), int(rnd_pos.split(',')[1]), pos[0], pos[1])
                        nuevo_taxi = Taxi()
                        self.vehiculos.update({rnd_pos: nuevo_taxi})
                        calle.vehiculos_encima['der'] = nuevo_taxi
                        break

            print('[GRILLA] Se agregaron {} taxis inicialmente'.format(taxis_iniciales))

        cargar_calles_casas(self)
        clasificar_cruces(self)
        poner_semaforos(self)
        cargar_autos_iniciales(self)

    def avanzar_vehiculos(self):
        def prox_pos(self, pos_vehiculo, vehiculo_actual):
            pos_vehiculo_aux = '{},{}'.format(round(float(pos_vehiculo.split(',')[0])),
                                              round(float(pos_vehiculo.split(',')[1])))
            if self.calles[pos_vehiculo_aux].direccion == ['derecha']:
                prox_pos_x = int(pos_vehiculo_aux.split(',')[0]) + vehiculo_actual.velocidad
                prox_pos_y = int(pos_vehiculo_aux.split(',')[1])
            elif self.calles[pos_vehiculo_aux].direccion == ['izquierda']:
                prox_pos_x = int(pos_vehiculo_aux.split(',')[0]) - vehiculo_actual.velocidad
                prox_pos_y = int(pos_vehiculo_aux.split(',')[1])
            elif self.calles[pos_vehiculo_aux].direccion == ['arriba']:
                prox_pos_x = int(pos_vehiculo_aux.split(',')[0])
                prox_pos_y = int(pos_vehiculo_aux.split(',')[1]) - vehiculo_actual.velocidad
            elif self.calles[pos_vehiculo_aux].direccion == ['abajo']:
                prox_pos_x = int(pos_vehiculo_aux.split(',')[0])
                prox_pos_y = int(pos_vehiculo_aux.split(',')[1]) + vehiculo_actual.velocidad
            prox_pos_str_red = '{},{}'.format(round(prox_pos_x), round(prox_pos_y))

            return prox_pos_str_red, prox_pos_x, prox_pos_y, pos_vehiculo_aux

        # TODO Si la proxima posicion es una calle, no es un cruce y esta la pista derecha vacia, entonces:
        def mover1(self, prox_pos_x, prox_pos_y, vehiculo_actual, pos_vehiculo_aux, prox_pos_str_red):
            # TODO A la posicion actual del vehiculo en self.vehiculos, se le suma los cuadrados que avanzaria en 1 segundo.
            prox_pos_str = '{},{}'.format(prox_pos_x, prox_pos_y)
            self.vehiculos.update({prox_pos_str: vehiculo_actual})

            # TODO Se elimina el vehiculo de la pista derecha de la calle actual y de self.vehiculos.
            self.calles[pos_vehiculo_aux].vehiculos_encima['der'] = None
            del self.vehiculos[pos_vehiculo]

            # TODO Se agrega el vehiculo a la pista derecha de la calle correspondiente a su nueva posicion redondeada.
            self.calles[prox_pos_str_red].vehiculos_encima['der'] = vehiculo_actual

            # TODO Se borra el auto de la grilla.
            self.grilla.quitar_imagen(int(pos_vehiculo_aux.split(',')[0]),
                                      int(pos_vehiculo_aux.split(',')[1]))

            # TODO Se agrega el auto a la grilla en la nueva posicion.
            self.grilla.agregar_auto(int(prox_pos_str_red.split(',')[0]),
                                     int(prox_pos_str_red.split(',')[1]),
                                     self.calles[prox_pos_str_red].pos_vehiculos[0],
                                     self.calles[prox_pos_str_red].pos_vehiculos[1])

        # TODO: Si la proxima posicion es una calle, es un cruce, el semaforo lo deja pasar y la pista derecha esta vacia, entonces: #ARREGLAR!!!!!!!
        def mover2(self, prox_pos_x, prox_pos_y, vehiculo_actual, pos_vehiculo_aux, prox_pos_str_red):
            # TODO A la posicion actual del vehiculo en self.vehiculos, se le suma los cuadrados que avanzaria en 1 segundo.
            prox_pos_str = '{},{}'.format(prox_pos_x, prox_pos_y)
            self.vehiculos.update({prox_pos_str: vehiculo_actual})

            # TODO Se elimina el vehiculo de la pista derecha de la calle actual y de self.vehiculos.
            self.calles[pos_vehiculo_aux].vehiculos_encima['der'] = None
            del self.vehiculos[pos_vehiculo]

            # TODO Se agrega el vehiculo a la pista derecha de la calle correspondiente a su nueva posicion redondeada.
            self.calles[prox_pos_str_red].vehiculos_encima['der'] = vehiculo_actual

            # TODO Se borra el auto de la grilla.
            self.grilla.quitar_imagen(int(pos_vehiculo_aux.split(',')[0]),
                                      int(pos_vehiculo_aux.split(',')[1]))

            # TODO Se agrega el auto a la grilla en la nueva posicion.
            self.grilla.agregar_auto(int(prox_pos_str_red.split(',')[0]),
                                     int(prox_pos_str_red.split(',')[1]),
                                     self.calles[prox_pos_str_red].pos_vehiculos[0],
                                     self.calles[prox_pos_str_red].pos_vehiculos[1])

            # TODO: Si la proxima posicon es una calle,

        # TODO: Si la proxima posicion no es una calle, entonces:
        def mover3(self, pos_vehiculo_aux, pos_vehiculo):
            # TODO Se elimina el vehiculo de la pista derecha de la calle actual y de self.vehiculos.
            self.calles[pos_vehiculo_aux].vehiculos_encima['der'] = None
            del self.vehiculos[pos_vehiculo]

            # TODO Se borra el auto de la grilla.
            self.grilla.quitar_imagen(int(pos_vehiculo_aux.split(',')[0]),
                                      int(pos_vehiculo_aux.split(',')[1]))

            # TODO Se agregan entre aleatoriamente entre 0 y 2 vehiculos a la ciudad si es que no se ha superado el maximo de autos.
            posiciones_entrada = []
            if not self.calles['2,1'].vehiculos_encima['der']:
                posiciones_entrada.append('2,1')
            if not self.calles['8,1'].vehiculos_encima['der']:
                posiciones_entrada.append('8,1')
            if not self.calles['16,1'].vehiculos_encima['der']:
                posiciones_entrada.append('16,1')
            if len(self.vehiculos) + 2 < len(self.calles) /2 :
                n_autos_nuevos = randint(0,len(posiciones_entrada))
                for a in range(n_autos_nuevos):
                    # Se instancia el nuevo auto
                    nuevo_auto = VehiculoComun()
                    # Se agrega el auto a la pista derecha de la calle de entrada
                    self.calles[posiciones_entrada[a]].vehiculos_encima['der'] = nuevo_auto
                    # Se agrega el auto a self.vehiculos
                    self.vehiculos[posiciones_entrada[a]] = nuevo_auto
                    # Se agrega el auto a la grilla
                    x = int(posiciones_entrada[a].split(',')[0])
                    y = int(posiciones_entrada[a].split(',')[1])
                    theta = self.calles[posiciones_entrada[a]].pos_vehiculos[0]
                    mirror = self.calles[posiciones_entrada[a]].pos_vehiculos[1]
                    self.grilla.agregar_auto(x, y, theta, mirror)

        aux_vehiculos = deepcopy(self.vehiculos)
        for pos_vehiculo in aux_vehiculos:
            vehiculo_actual = aux_vehiculos[pos_vehiculo]
            prox_pos_str_red = prox_pos(self, pos_vehiculo, vehiculo_actual)[0]
            prox_pos_x = prox_pos(self, pos_vehiculo, vehiculo_actual)[1]
            prox_pos_y = prox_pos(self, pos_vehiculo, vehiculo_actual)[2]
            pos_vehiculo_aux = prox_pos(self, pos_vehiculo, vehiculo_actual)[3]

            # TODO Si la proxima posicion es una calle, no es un cruce y esta la pista derecha vacia, entonces:
            if prox_pos_str_red in self.calles:
                if not self.calles[prox_pos_str_red].cruce:
                    if not self.calles[prox_pos_str_red].vehiculos_encima['der']:
                        mover1(self, prox_pos_x, prox_pos_y, vehiculo_actual, pos_vehiculo_aux, prox_pos_str_red)

            # TODO: Si la proxima posicion es una calle, es un cruce, el semaforo lo deja pasar y la pista derecha esta vacia, entonces:
            if prox_pos_str_red in self.calles:
                if self.calles[prox_pos_str_red].cruce:
                    direccion_elegida = choice(self.calles[pos_vehiculo_aux].direccion)
                    if direccion_elegida in self.calles[prox_pos_str_red].semaforo:
                        if not self.calles[prox_pos_str_red].vehiculos_encima['der']:
                            mover2(self, prox_pos_x, prox_pos_y, vehiculo_actual, pos_vehiculo_aux, prox_pos_str_red)

            # TODO: Si la proxima posicion no es una calle, entonces:
            if prox_pos_str_red not in self.calles:
                mover3(self, pos_vehiculo_aux, pos_vehiculo)




                            # print('[SIMULACION] Los vehiculos han avanzado durante {segundos} segundos')

    def cambiar_semaforos(self):
        for pos_calle in self.calles:
            if self.calles[pos_calle].cruce:
                x_pos = int(pos_calle.split(',')[0])
                y_pos = int(pos_calle.split(',')[1])
                self.calles[pos_calle].cambiar_semaforo(self.grilla, x_pos, y_pos)
        print('[SIMULACION] Semaforos cambiados')
