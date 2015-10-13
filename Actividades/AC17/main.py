from collections import deque
from random import uniform, randint
from random import expovariate


class Jugador:
    # Esta clase modela los jugadores que llegan a la mesa.
    def __init__(self, tiempo_llegada=0):
        self.tiempo_llegada = tiempo_llegada
        self.habilidad = uniform(1, 10)
        self.partidos_jugados = 0

    @property
    def retirarse(self):
        if self.partidos_jugados > 4:
            return True
        return False


class Mesa:
    def __init__(self):
        self.jugadores_actuales = []
        self.tiempo_partido = 0

    def jugador_entra(self, jugador):
        self.jugadores_actuales.append(jugador)
        # Se crea un tiempo de duracion del partido.
        self.tiempo_partido = round(uniform(4, 6))

    def jugador_sale(self, jugador):
        self.jugadores_actuales.remove(jugador)

    @property
    def ocupada(self):
        return len(self.jugadores_actuales) == 2


class Simulacion:
    def __init__(self, tiempo_maximo, tasa_llegada):
        """
        tiempo_maximo_sim : en este caso es el tiempo de 70 min que dura la simulacion completa
        tasa_llegada : corresponde a 1/15 en este caso, la tasa de llegada de jugadores a la mesa
        tiempo_simulacion : es el reloj de la simulacion
        tiempo_proximo_jugador : es el tiempo en el que llegara un proximo jugador
        tiempo_duracion_partido : es el tiempo que durara el partido actual
        tiempo_espera : es el tiempo total que esperaron jugadores en la cola
        mesa : modela la mesa
        cola_espera : contiene a los jugadores en la fila esperando para jugar
        partidos_jugados : total de partidos jugados durante la simulacion
        """
        self.tiempo_maximo_sim = tiempo_maximo
        self.tasa_llegada = tasa_llegada
        self.tiempo_simulacion = 0
        self.tiempo_proximo_jugador = 0
        self.tiempo_duracion_partido = 0
        self.tiempo_espera = 0
        self.mesa = Mesa()
        self.cola_espera = deque()
        self.partidos_jugados = 0

    def proximo_jugador(self, tasa_llegada):
        self.tiempo_proximo_jugador = self.tiempo_simulacion + round(expovariate(tasa_llegada) + 0.5)

    def run(self):
        # La mesa se inicia con dos jugadores en ella, y uno en la cola.
        self.cola_espera.append(Jugador())
        self.mesa.jugador_entra(Jugador())
        self.mesa.jugador_entra(Jugador())

        self.proximo_jugador(self.tasa_llegada)

        while self.tiempo_simulacion < self.tiempo_maximo_sim or (len(self.cola_espera) == 0
                                                                  and len(self.mesa.jugadores_actuales) < 2):
            if (self.mesa.ocupada and self.tiempo_proximo_jugador < self.tiempo_duracion_partido) or (
                    not self.mesa.ocupada):
                self.tiempo_simulacion = self.tiempo_proximo_jugador
            else:
                self.tiempo_simulacion = self.tiempo_duracion_partido

            print("[SIMULACION] Tiempo: {0} minutos.".format(self.tiempo_simulacion))

            if self.tiempo_simulacion == self.tiempo_proximo_jugador:
                self.cola_espera.append(Jugador(self.tiempo_simulacion))
                self.proximo_jugador(self.tasa_llegada)

                print("[COLA] Llega un jugador en tiempo de simulacion: {0} minutos.".format(self.tiempo_simulacion))

                if (not self.mesa.ocupada) and (len(self.cola_espera) > 0):
                    proximo_jugador = self.cola_espera.popleft()
                    self.mesa.jugador_entra(proximo_jugador)

                    self.tiempo_duracion_partido = self.tiempo_simulacion + self.mesa.tiempo_partido

                    for j in self.mesa.jugadores_actuales:
                        j.partidos_jugados += 1

                    print("[MESA Entra un jugador con un tiempo esperado de termino de partido de {0} minutos.".format(
                        self.mesa.tiempo_partido))

            else:
                suma_habilidades = self.mesa.jugadores_actuales[0].habilidad + self.mesa.jugadores_actuales[1].habilidad
                int_ganador = randint(0, round(suma_habilidades))
                if int_ganador <= self.mesa.jugadores_actuales[0].habilidad:
                    perdedor = self.mesa.jugadores_actuales[1]
                else:
                    perdedor = self.mesa.jugadores_actuales[0]

                print("[MESA] Termina un partido a los {0} minutos.".format(self.tiempo_simulacion))

                if perdedor.retirarse:
                    print("[MESA] El jugador perdedor se retiro de la mesa a los {0} minutos".format(
                        self.tiempo_simulacion))
                else:
                    self.cola_espera.append(perdedor)
                    print("[MESA] El jugador perdedor se puso de nuevo en la cola a los {0} minutos".format(
                        self.tiempo_simulacion))

                self.mesa.jugador_sale(perdedor)
                self.tiempo_espera += self.tiempo_simulacion - perdedor.tiempo_llegada
                self.partidos_jugados += 1
        print("[SIMULACION] Finalizada.")

        print()
        print('ESTADISTICAS')
        print('TIEMPO TOTAL PARTIDOS: {0} MINUTOS'.format(self.tiempo_duracion_partido))
        print('TOTAL DE PARTIDOS JUGADOS: {0}'.format(self.partidos_jugados))
        print('TIEMPO PROMEDIO DE ESPERA: {0} MINUTOS'.format(round(self.tiempo_espera / self.partidos_jugados)))


if __name__ == '__main__':
    # Se inicializa la simulacion con 70 minutos como tiempo maximo.
    # Se define la tasa de llegada de los jugadores a la mesa en un jugador cada 15 minutos.
    tasa_llegada_jugadores = 1 / 15
    s = Simulacion(70, tasa_llegada_jugadores)
    s.run()
