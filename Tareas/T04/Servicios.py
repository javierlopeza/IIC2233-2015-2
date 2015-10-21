from Vehiculo import *


class Servicio:
    def __init__(self, posicion, tipo):
        self.posicion = posicion
        self.tipo = tipo
        self.vehiculos_disponibles = 3

    def asistir_urgencia(self, ciudad, ubicacion_emergencia):
        if self.vehiculos_disponibles:
            self.vehiculos_disponibles -= 1
            if self.tipo == 'bomberos':
                nuevo_vehiculo = CarroBomberos()
            elif self.tipo == 'hospital':
                nuevo_vehiculo = Ambulancia()
            elif self.tipo == 'policia':
                nuevo_vehiculo = Patrulla()

            tiempo_total = 0


            camino_ida = ciudad.buscar_ruta_corta(self.posicion, ubicacion_emergencia)
            camino_vuelta = ciudad.buscar_ruta_corta(ubicacion_emergencia, self.posicion)

            if not camino_ida or not camino_vuelta:
                return None

            tiempo_total += len(camino_ida)
            if self.tipo == 'bomberos':
                tiempo_total += ciudad.casas[ubicacion_emergencia].demora_apagar_incendio
                ciudad.tiempos_incendios.append(tiempo_total)
            elif self.tipo == 'hospital':
                tiempo_total += len(camino_vuelta) * 2
                ciudad.tiempos_enfermos.append(tiempo_total)

            # Se muestra como la ambulancia recorre la ciudad de ida.
            pos_calle_inicio = camino_ida[0]
            getattr(ciudad.grilla, 'agregar_'.format(nuevo_vehiculo.tipo))(camino_ida[0],
                                                                           camino_ida[1],
                                                                           ciudad.calles[
                                                                               pos_calle_inicio].pos_vehiculos[0],
                                                                           ciudad.calles[
                                                                               pos_calle_inicio].pos_vehiculos[1])
            for pos in camino_ida[1:]:
                ciudad.quitar_imagen(camino_ida[0][0],
                                     camino_ida[0][1])
                pos_x = int(pos[0].split(',')[0])
                pos_y = int(pos[1].split(',')[1])
                getattr(ciudad.grilla, 'agregar_'.format(nuevo_vehiculo.tipo))(pos_x,
                                                                               pos_y,
                                                                               ciudad.calles[
                                                                                   pos_calle_inicio].pos_vehiculos[0],
                                                                               ciudad.calles[
                                                                                   pos_calle_inicio].pos_vehiculos[1])
            # Se muestra como la ambulancia recorre la ciudad de vuelta.
            pos_calle_vuelta = camino_vuelta[0]
            getattr(ciudad.grilla, 'agregar_'.format(nuevo_vehiculo.tipo))(int(camino_vuelta[0].split(',')[0]),
                                                                           int(camino_vuelta[1].split(',')[1]),
                                                                           ciudad.calles[
                                                                               pos_calle_vuelta].pos_vehiculos[0],
                                                                           ciudad.calles[
                                                                               pos_calle_vuelta].pos_vehiculos[1])
            for pos in camino_vuelta[1:]:
                ciudad.quitar_imagen(int(camino_vuelta[0].split(',')[0]),
                                     int(camino_vuelta[1].split(',')[1]))
                pos_x = pos[0]
                pos_y = pos[1]
                getattr(ciudad.grilla, 'agregar_'.format(nuevo_vehiculo.tipo))(pos_x,
                                                                               pos_y,
                                                                               ciudad.calles[
                                                                                   pos_calle_inicio].pos_vehiculos[0],
                                                                               ciudad.calles[
                                                                                   pos_calle_inicio].pos_vehiculos[1])
