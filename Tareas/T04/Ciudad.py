# -*- encoding: utf-8 -*-
from gui.gui import GrillaSimulacion
from Casa import Casa
from Vehiculo import VehiculoComun, Taxi, VehiculoEmergencia
from Calle import Calle
from Servicios import Servicio
from random import randint, choice
from copy import deepcopy
from decimal import Decimal


class Ciudad:
    def __init__(self, app, rows, cols, pos_policia, pos_bomberos, pos_hospital):
        self.grilla = GrillaSimulacion(app, rows, cols)
        self.grilla.show()
        self.servicios = {'bomberos': None,
                          'policia': None,
                          'hospital': None}
        self.calles = {}
        self.entradas = {}
        self.salidas = {}
        self.casas = {}
        self.vehiculos = {}
        self.rellenar_ciudad_base(pos_policia, pos_bomberos, pos_hospital)
        # self.grilla.tiempo_intervalo = float(input('Ingrese el intervalo de tiempo '
        #                                          'para los eventos en la simulacion: '))
        self.grilla.tiempo_intervalo = 0

    def rellenar_ciudad_base(self, pos_policia, pos_bomberos, pos_hospital):

        def poner_servicios_emergencia(self, pos_policia, pos_bomberos, pos_hospital):
            self.servicios['policia'] = Servicio(pos_policia, 'policia')
            x_policia = int(pos_policia.split(',')[0])
            y_policia = int(pos_policia.split(',')[1])
            self.servicios['bomberos'] = Servicio(pos_bomberos, 'bomberos')
            x_bomberos = int(pos_bomberos.split(',')[0])
            y_bomberos = int(pos_bomberos.split(',')[1])
            self.servicios['hospital'] = Servicio(pos_hospital, 'hospital')
            x_hospital = int(pos_hospital.split(',')[0])
            y_hospital = int(pos_hospital.split(',')[1])

            self.grilla.agregar_comisaria(x_policia, y_policia)
            self.grilla.agregar_cuartel_bomberos(x_bomberos, y_bomberos)
            self.grilla.agregar_hospital(x_hospital, y_hospital)

            print('[CIUDAD] Servicios de emergencia posicionados')

        def cargar_calles_casas(self):
            mapa_file = open('mapa fix.txt', 'r')
            lineas = mapa_file.readlines()
            for l in range(1, len(lineas)):
                x = int(lineas[l].split(' ')[0].split(',')[0])
                y = int(lineas[l].split(' ')[0].split(',')[1])
                entidad = lineas[l].split(' ')[1]
                if entidad.lower() == 'casa':
                    material = lineas[l].split(' ')[3]
                    duracion_robo = [int(i) for i in lineas[l].split('[')[1][:-2].split(', ')]
                    self.grilla.agregar_casa(x + 1, y + 1)
                    nueva_casa = Casa(material, duracion_robo)
                    self.casas.update({'{},{}'.format(x + 1, y + 1): nueva_casa})
                elif entidad.lower() == 'calle':
                    direccion = lineas[l].split(' ')[2][:-1]
                    self.grilla.agregar_calle(x + 1, y + 1)
                    nueva_calle = Calle(direccion)
                    self.calles.update({'{},{}'.format(x + 1, y + 1): nueva_calle})

            print('[CIUDAD] Se cargaron {} calles y {} casas de mapa.txt'.format(len(self.calles), len(self.casas)))

        def cargar_distancias_comisaria(self):
            if self.servicios['policia']:
                x_policia = int(self.servicios['policia'].posicion.split(',')[0])
                y_policia = int(self.servicios['policia'].posicion.split(',')[1])
                for pos_casa in self.casas:
                    x_casa = int(pos_casa.split(',')[0])
                    y_casa = int(pos_casa.split(',')[1])
                    self.casas[pos_casa].peso_distancia_comisaria = 10 + abs(x_casa - x_policia) + abs(
                        y_casa - y_policia)

        def clasificar_cruces(self):
            for pos_calle in self.calles:
                x = int(pos_calle.split(',')[0])
                y = int(pos_calle.split(',')[1])

                ob_izq1 = '{},{}'.format(x, y - 1)
                ob_der1 = '{},{}'.format(x, y + 1)
                ob_abajo1 = '{},{}'.format(x + 1, y)
                ob_arriba1 = '{},{}'.format(x - 1, y)
                ob_izq2 = '{},{}'.format(x, y - 2)
                ob_der2 = '{},{}'.format(x, y + 2)
                ob_abajo2 = '{},{}'.format(x + 2, y)
                ob_arriba2 = '{},{}'.format(x - 2, y)

                # Cruce tipo + o T de 1 pista
                if ob_izq1 in self.calles and ob_der1 in self.calles:
                    if self.calles[ob_izq1].direccion \
                            == self.calles[ob_der1].direccion \
                            != self.calles[pos_calle].direccion:
                        self.calles[pos_calle].cruce = True

                if ob_abajo1 in self.calles and ob_arriba1 in self.calles:
                    if self.calles[ob_abajo1].direccion \
                            == self.calles[ob_arriba1].direccion \
                            != self.calles[pos_calle].direccion:
                        self.calles[pos_calle].cruce = True

                # Cruce doble +
                if ob_izq2 in self.calles and ob_izq1 in self.calles and ob_der1 in self.calles:
                    if self.calles[ob_izq2].direccion == self.calles[ob_der1].direccion \
                            != self.calles[ob_izq1].direccion == self.calles[pos_calle].direccion:
                        self.calles[pos_calle].cruce = True

                if ob_der2 in self.calles and ob_der1 in self.calles and ob_izq1 in self.calles:
                    if self.calles[ob_der2].direccion == self.calles[ob_izq1].direccion \
                            != self.calles[ob_der1].direccion == self.calles[pos_calle].direccion:
                        self.calles[pos_calle].cruce = True

                if ob_arriba2 in self.calles and ob_arriba1 in self.calles and ob_abajo1 in self.calles:
                    if self.calles[ob_arriba2].direccion == self.calles[ob_abajo1].direccion \
                            != self.calles[ob_arriba1].direccion == self.calles[pos_calle].direccion:
                        self.calles[pos_calle].cruce = True

                if ob_abajo2 in self.calles and ob_abajo1 in self.calles and ob_arriba1 in self.calles:
                    if self.calles[ob_abajo2].direccion == self.calles[ob_arriba1].direccion \
                            != self.calles[ob_abajo1].direccion == self.calles[pos_calle].direccion:
                        self.calles[pos_calle].cruce = True

                # Cruce T peligroso
                if ob_arriba1 in self.calles \
                        and ob_izq1 in self.calles \
                        and ob_der1 in self.calles \
                        and ob_der2 in self.calles \
                        and ob_izq2 in self.calles:
                    if (self.calles[ob_izq1].direccion == self.calles[ob_der1].direccion == self.calles[
                        ob_der2].direccion == self.calles[ob_izq2].direccion == self.calles[pos_calle].direccion) \
                            and (self.calles[ob_arriba1].direccion == ['abajo']):
                        self.calles[pos_calle].cruce = True

                if ob_abajo1 in self.calles \
                        and ob_izq1 in self.calles \
                        and ob_der1 in self.calles \
                        and ob_der2 in self.calles \
                        and ob_izq2 in self.calles:
                    if (self.calles[ob_izq1].direccion == self.calles[ob_der1].direccion == self.calles[
                        ob_der2].direccion == self.calles[ob_izq2].direccion == self.calles[pos_calle].direccion) \
                            and (self.calles[ob_abajo1].direccion == ['arriba']):
                        self.calles[pos_calle].cruce = True

                if ob_izq1 in self.calles and ob_abajo1 in self.calles \
                        and ob_arriba1 in self.calles and ob_abajo2 in self.calles \
                        and ob_arriba2 in self.calles:
                    if (self.calles[ob_arriba1].direccion == self.calles[ob_abajo1].direccion
                            == self.calles[ob_abajo2].direccion == self.calles[ob_arriba2].direccion
                            == self.calles[pos_calle].direccion) and (self.calles[ob_izq1].direccion == ['derecha']):
                        self.calles[pos_calle].cruce = True

                if ob_der1 in self.calles and ob_abajo1 in self.calles and ob_arriba1 in self.calles \
                        and ob_abajo2 in self.calles and ob_arriba2 in self.calles:
                    if (self.calles[ob_arriba1].direccion == self.calles[ob_abajo1].direccion
                            == self.calles[ob_abajo2].direccion == self.calles[ob_arriba2].direccion
                            == self.calles[pos_calle].direccion) and (self.calles[ob_der1].direccion == ['izquierda']):
                        self.calles[pos_calle].cruce = True

                # Cruce T Peligroso segunda fila
                if ob_arriba2 in self.calles and ob_izq1 in self.calles and ob_der1 in self.calles \
                        and ob_der2 in self.calles and ob_izq2 in self.calles:
                    if self.calles[ob_izq1].direccion == self.calles[ob_der1].direccion \
                            == self.calles[ob_der2].direccion == self.calles[ob_izq2].direccion \
                            == self.calles[pos_calle].direccion \
                            and self.calles[ob_arriba2].direccion == ['abajo']:
                        self.calles[pos_calle].cruce = True

                if ob_abajo2 in self.calles and ob_izq1 in self.calles and ob_der1 in self.calles \
                        and ob_der2 in self.calles and ob_izq2 in self.calles:
                    if (self.calles[ob_izq1].direccion == self.calles[ob_der1].direccion
                            == self.calles[ob_der2].direccion == self.calles[ob_izq2].direccion
                            == self.calles[pos_calle].direccion) and (self.calles[ob_abajo2].direccion == ['arriba']):
                        self.calles[pos_calle].cruce = True

                if ob_izq2 in self.calles and ob_abajo1 in self.calles and ob_arriba1 in self.calles \
                        and ob_abajo2 in self.calles and ob_arriba2 in self.calles:
                    if (self.calles[ob_arriba1].direccion == self.calles[ob_abajo1].direccion
                            == self.calles[ob_abajo2].direccion == self.calles[ob_arriba2].direccion
                            == self.calles[pos_calle].direccion) and (self.calles[ob_izq2].direccion == ['derecha']):
                        self.calles[pos_calle].cruce = True

                if ob_der2 in self.calles and ob_abajo1 in self.calles and ob_arriba1 in self.calles \
                        and ob_abajo2 in self.calles and ob_arriba2 in self.calles:
                    if (self.calles[ob_arriba1].direccion == self.calles[ob_abajo1].direccion
                            == self.calles[ob_abajo2].direccion == self.calles[ob_arriba2].direccion
                            == self.calles[pos_calle].direccion) and (self.calles[ob_der2].direccion == ['izquierda']):
                        self.calles[pos_calle].cruce = True

            print('[CIUDAD] Se encontraron y clasificaron todos los cruces')

        def poner_semaforos(self):
            total_semaforos = 0
            for pos_calle in self.calles:
                if self.calles[pos_calle].cruce:
                    # Si la calle corresponde a un cruce, se le agrega por defecto
                    # un semaforo activado en verde en sentido vertical.
                    self.calles[pos_calle].semaforo = ['arriba', 'abajo']
                    self.grilla.agregar_semaforo_vertical(int(pos_calle.split(',')[0]), int(pos_calle.split(',')[1]))
                    total_semaforos += 1

            print('[CIUDAD] Se agregaron {} semaforos en los cruces'.format(total_semaforos))

        def clasificar_entradas_salidas(self):
            for pos_calle in self.calles:
                x = int(pos_calle.split(',')[0])
                y = int(pos_calle.split(',')[1])

                ob_izq1 = '{},{}'.format(x, y - 1)
                ob_der1 = '{},{}'.format(x, y + 1)
                ob_abajo1 = '{},{}'.format(x + 1, y)
                ob_arriba1 = '{},{}'.format(x - 1, y)

                if self.calles[pos_calle].direccion == ['abajo']:
                    if ob_arriba1 not in self.calles:
                        self.entradas.update({pos_calle: self.calles[pos_calle]})
                    if ob_abajo1 not in self.calles:
                        self.salidas.update({pos_calle: self.calles[pos_calle]})

                elif self.calles[pos_calle].direccion == ['arriba']:
                    if ob_abajo1 not in self.calles:
                        self.entradas.update({pos_calle: self.calles[pos_calle]})
                    if ob_arriba1 not in self.calles:
                        self.salidas.update({pos_calle: self.calles[pos_calle]})

                elif self.calles[pos_calle].direccion == ['derecha']:
                    if ob_izq1 not in self.calles:
                        self.entradas.update({pos_calle: self.calles[pos_calle]})
                    if ob_der1 not in self.calles:
                        self.salidas.update({pos_calle: self.calles[pos_calle]})

                elif self.calles[pos_calle].direccion == ['izquierda']:
                    if ob_der1 not in self.calles:
                        self.entradas.update({pos_calle: self.calles[pos_calle]})
                    if ob_izq1 not in self.calles:
                        self.salidas.update({pos_calle: self.calles[pos_calle]})

            print('[CIUDAD] Se clasificaron y encontraron {} entradas y {} salidas de la ciudad'.format(
                len(self.entradas), len(self.salidas)))

        def cargar_autos_iniciales(self):
            autos_iniciales = randint(round(len(self.calles) / 4), round(len(self.calles) / 2) - randint(3, 8))
            for a in range(autos_iniciales):
                while True:
                    rnd_pos = choice(list(self.calles.keys()))
                    calle = self.calles[rnd_pos]
                    if not calle.vehiculos_encima['der'] and not calle.cruce:
                        pos = calle.pos_vehiculos
                        self.grilla.agregar_sedan(int(rnd_pos.split(',')[0]), int(rnd_pos.split(',')[1]), pos[0],
                                                  pos[1])
                        nuevo_vehiculo = VehiculoComun()
                        self.vehiculos.update({rnd_pos: nuevo_vehiculo})
                        calle.vehiculos_encima['der'] = nuevo_vehiculo
                        break

            print('[CIUDAD] Se agregaron {} autos inicialmente'.format(autos_iniciales))

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

            print('[CIUDAD] Se agregaron {} taxis inicialmente'.format(taxis_iniciales))

        def clasificar_continuaciones(self):
            for pos_calle in self.calles:
                x = int(pos_calle.split(',')[0])
                y = int(pos_calle.split(',')[1])

                ob_izq1 = '{},{}'.format(x, y - 1)
                ob_der1 = '{},{}'.format(x, y + 1)
                ob_abajo1 = '{},{}'.format(x + 1, y)
                ob_arriba1 = '{},{}'.format(x - 1, y)

                if ob_izq1 in self.calles:
                    if self.calles[ob_izq1].direccion == ['izquierda']:
                        self.calles[pos_calle].continuaciones.update({ob_izq1: self.calles[ob_izq1]})
                if ob_der1 in self.calles:
                    if self.calles[ob_der1].direccion == ['derecha']:
                        self.calles[pos_calle].continuaciones.update({ob_der1: self.calles[ob_der1]})
                if ob_arriba1 in self.calles:
                    if self.calles[ob_arriba1].direccion == ['arriba']:
                        self.calles[pos_calle].continuaciones.update({ob_arriba1: self.calles[ob_arriba1]})
                if ob_abajo1 in self.calles:
                    if self.calles[ob_abajo1].direccion == ['abajo']:
                        self.calles[pos_calle].continuaciones.update({ob_abajo1: self.calles[ob_abajo1]})
                if not self.calles[pos_calle].continuaciones:
                    self.calles[pos_calle].continuaciones.update({None: None})

        poner_servicios_emergencia(self, pos_policia, pos_bomberos, pos_hospital)
        cargar_calles_casas(self)
        cargar_distancias_comisaria(self)
        clasificar_entradas_salidas(self)
        clasificar_continuaciones(self)
        clasificar_cruces(self)
        poner_semaforos(self)
        cargar_autos_iniciales(self)

    @property
    def lista_pesos_lugares_robos(self):
        probs_lugares = []
        for pos_casa in self.casas:
            for p in range(self.casas[pos_casa].peso_distancia_comisaria):
                probs_lugares.append(pos_casa)
        return probs_lugares

    @property
    def lista_pesos_lugares_incendios(self):
        suma_pesos = 0
        for pos_casa in self.casas:
            material = self.casas[pos_casa].material
            if material == 'madera':
                peso_material = 10
            elif material == 'ladrillos':
                peso_material = 7
            elif material == 'hormigon':
                peso_material = 4
            elif material == 'metal':
                peso_material = 2
            suma_pesos += peso_material

        notaciones_cientificas = ('%.2E' % Decimal(str(p / suma_pesos)) for p in [10, 7, 4, 2])
        max_exp = max((int(nc.split('-')[-1]) for nc in notaciones_cientificas))
        pesos_por_material = [round((10 ** max_exp) * p / suma_pesos) for p in [10, 4, 7, 2]]

        probs_lugares = []
        for pos_casa in self.casas:
            material = self.casas[pos_casa].material
            if material == 'madera':
                for i in range(pesos_por_material[0]):
                    probs_lugares.append(pos_casa)
            elif material == 'ladrillos':
                for i in range(pesos_por_material[1]):
                    probs_lugares.append(pos_casa)
            elif material == 'hormigon':
                for i in range(pesos_por_material[2]):
                    probs_lugares.append(pos_casa)
            elif material == 'metal':
                for i in range(pesos_por_material[3]):
                    probs_lugares.append(pos_casa)
        return probs_lugares

    def avanzar_vehiculos(self):
        def prox_pos(self, pos_vehiculo, vehiculo_actual):
            pos_vehiculo_aux = '{},{}'.format(int(float(pos_vehiculo.split(',')[0])),
                                              int(float(pos_vehiculo.split(',')[1])))
            if pos_vehiculo_aux in self.calles:
                pos_prox_calle = choice(list(self.calles[pos_vehiculo_aux].continuaciones.keys()))
                if pos_prox_calle:
                    if self.calles[pos_prox_calle].direccion == ['derecha']:
                        prox_pos_x = float(pos_vehiculo.split(',')[0])
                        prox_pos_y = float(pos_vehiculo.split(',')[1]) + vehiculo_actual.velocidad
                    elif self.calles[pos_prox_calle].direccion == ['izquierda']:
                        prox_pos_x = float(pos_vehiculo.split(',')[0])
                        prox_pos_y = float(pos_vehiculo.split(',')[1]) - vehiculo_actual.velocidad
                    elif self.calles[pos_prox_calle].direccion == ['arriba']:
                        prox_pos_x = float(pos_vehiculo.split(',')[0]) - vehiculo_actual.velocidad
                        prox_pos_y = float(pos_vehiculo.split(',')[1])
                    elif self.calles[pos_prox_calle].direccion == ['abajo']:
                        prox_pos_x = float(pos_vehiculo.split(',')[0]) + vehiculo_actual.velocidad
                        prox_pos_y = float(pos_vehiculo.split(',')[1])

                else:
                    prox_pos_x = -1
                    prox_pos_y = -1
                prox_pos_str_red = '{},{}'.format(round(prox_pos_x), round(prox_pos_y))
                return prox_pos_str_red, prox_pos_x, prox_pos_y, pos_vehiculo_aux
            else:
                vehiculo_fuera(pos_vehiculo_aux, pos_vehiculo)
                return None

        def avance_comun(self, prox_pos_x, prox_pos_y, vehiculo_actual, pos_vehiculo_aux, prox_pos_str_red):
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
            self.grilla.agregar_sedan(int(prox_pos_str_red.split(',')[0]),
                                      int(prox_pos_str_red.split(',')[1]),
                                      self.calles[prox_pos_str_red].pos_vehiculos[0],
                                      self.calles[prox_pos_str_red].pos_vehiculos[1])

        def avance_cruce(self, prox_pos_x, prox_pos_y, vehiculo_actual, pos_vehiculo_str_redondeada, prox_pos_str_red,
                         pos_vehiculo):
            # TODO A la posicion actual del vehiculo en self.vehiculos, se le suma los cuadrados que avanzaria en 1 segundo.
            prox_pos_str = '{},{}'.format(prox_pos_x, prox_pos_y)
            self.vehiculos.update({prox_pos_str: vehiculo_actual})

            # TODO Se elimina el vehiculo de la pista derecha de la calle actual y de self.vehiculos.
            self.calles[pos_vehiculo_str_redondeada].vehiculos_encima['der'] = None
            del self.vehiculos[pos_vehiculo]

            # TODO Se agrega el vehiculo a la pista derecha de la calle correspondiente a su nueva posicion redondeada.
            self.calles[prox_pos_str_red].vehiculos_encima['der'] = vehiculo_actual

            # TODO Se borra el auto de la grilla.
            self.grilla.quitar_imagen(int(pos_vehiculo_str_redondeada.split(',')[0]),
                                      int(pos_vehiculo_str_redondeada.split(',')[1]))

            # TODO Se agrega el auto a la grilla en la nueva posicion.
            self.grilla.agregar_sedan(int(prox_pos_str_red.split(',')[0]),
                                      int(prox_pos_str_red.split(',')[1]),
                                      self.calles[prox_pos_str_red].pos_vehiculos[0],
                                      self.calles[prox_pos_str_red].pos_vehiculos[1])

            # TODO: Si la proxima posicon es una calle,

        def vehiculo_fuera(self, pos_vehiculo_aux, pos_vehiculo):
            # TODO Se elimina el vehiculo de la pista derecha de la calle actual y de self.vehiculos.
            self.calles[pos_vehiculo_aux].vehiculos_encima['der'] = None
            del self.vehiculos[pos_vehiculo]

            # TODO Se borra el auto de la grilla.
            self.grilla.quitar_imagen(int(pos_vehiculo_aux.split(',')[0]),
                                      int(pos_vehiculo_aux.split(',')[1]))

            # TODO Se agregan entre aleatoriamente entre 0 y 2 vehiculos a la ciudad sin superar el maximo de autos.
            n_autos_nuevos = randint(0, min(2, int(len(self.calles) / 2 - len(self.vehiculos))))
            for a in range(n_autos_nuevos):

                # Se instancia el nuevo auto
                nuevo_auto = VehiculoComun()
                # Se agrega el auto a la pista derecha vacia de una calle de entrada aleatoria
                for pos_entrada in self.entradas:
                    if not self.entradas[pos_entrada].vehiculos_encima['der']:
                        self.calles[pos_entrada].vehiculos_encima['der'] = nuevo_auto
                        break
                # Se agrega el auto a self.vehiculos
                self.vehiculos[pos_entrada] = nuevo_auto
                # Se agrega el auto a la grilla
                x = int(pos_entrada.split(',')[0])
                y = int(pos_entrada.split(',')[1])
                theta = self.calles[pos_entrada].pos_vehiculos[0]
                mirror = self.calles[pos_entrada].pos_vehiculos[1]
                self.grilla.agregar_sedan(x, y, theta, mirror)

        aux_vehiculos = deepcopy(self.vehiculos)
        for pos_vehiculo in aux_vehiculos:
            vehiculo_actual = aux_vehiculos[pos_vehiculo]
            PPP = prox_pos(self, pos_vehiculo, vehiculo_actual)
            if PPP:
                prox_pos_str_redondeada = PPP[0]
                prox_pos_x = PPP[1]
                prox_pos_y = PPP[2]
                pos_vehiculo_str_redondeada = PPP[3]

                # TODO Si la proxima posicion escogida es una calle, no es un cruce y esta la pista derecha vacia, entonces:
                if prox_pos_str_redondeada in self.calles:
                    if not self.calles[prox_pos_str_redondeada].cruce:
                        if not self.calles[prox_pos_str_redondeada].vehiculos_encima['der']:
                            avance_comun(self, prox_pos_x, prox_pos_y, vehiculo_actual, pos_vehiculo_str_redondeada,
                                         prox_pos_str_redondeada)

                # TODO: Si la proxima posicion escogida es una calle, es un cruce, el semaforo lo deja pasar, y la pista derecha siguiente y subsiguiente estan vacias, entonces: #ARREGLAR!!!!!!!
                if prox_pos_str_redondeada in self.calles:
                    if self.calles[prox_pos_str_redondeada].cruce:
                        if self.calles[pos_vehiculo_str_redondeada].direccion[0] in self.calles[
                            prox_pos_str_redondeada].semaforo:
                            if not self.calles[prox_pos_str_redondeada].vehiculos_encima['der']:
                                avance_cruce(self, prox_pos_x, prox_pos_y, vehiculo_actual, pos_vehiculo_str_redondeada,
                                             prox_pos_str_redondeada, pos_vehiculo)

                # TODO: Si la proxima posicion escogida no es una calle, entonces:
                if prox_pos_str_redondeada not in self.calles:
                    vehiculo_fuera(self, pos_vehiculo_str_redondeada, pos_vehiculo)




                    # print('[SIMULACION] Los vehiculos han avanzado durante {segundos} segundos')

    def cambiar_semaforos(self):
        for pos_calle in self.calles:
            if self.calles[pos_calle].cruce:
                x_pos = int(pos_calle.split(',')[0])
                y_pos = int(pos_calle.split(',')[1])
                self.calles[pos_calle].cambiar_semaforo(self.grilla, x_pos, y_pos)
        # print('[SIMULACION] Semaforos cambiados')
