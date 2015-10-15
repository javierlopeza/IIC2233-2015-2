import random
import simpy


def paciencia(cliente):
    return 2 * cliente.priority + 7


class Cliente():
    def __init__(self, *args, **kwargs):
        self.priority = kwargs['priority']
        self.name = kwargs['name']
        self.arrive = kwargs['arrive']
        self.number = kwargs['arrival_number']
        self.exit = None

    @property
    def recibe_llamada(self):
        prob = random.randint(1,10)
        if prob == 1:
            return True
        return False


class Restaurante():
    def __init__(self, env, capacity):
        self.env = env
        self.mesas = simpy.PriorityResource(env, capacity=capacity)
        self.__clientes = []
        self.n_atendidos = 1

    def espera(self, cliente):
        try:
            with self.mesas.request() as req:
                results = yield req | self.env.timeout(paciencia(cliente))
                if req not in results:
                    self.env.process(self.espera(cliente)).interrupt()
                else:
                    print("[ATENCION] El cliente {0} llego en el instante {1} y fue atendido al instante {2}, "
                          "tuvo que esperar {3} minutos para que lo atendieran.".
                          format(cliente.name,
                                 round(cliente.arrive, 2),
                                 round(self.env.now, 2),
                                 round(self.env.now - cliente.arrive, 2)))
                    if cliente.recibe_llamada:
                        yield self.env.timeout(random.uniform(7,12))
                        print("[LLAMADA] El cliente {0} recibio una llamada importante "
                              "y se tuvo que ir al instante {1}".
                              format(cliente.name,
                                     round(self.env.now, 2)))

                    else:
                        yield self.env.timeout(random.uniform(30, 40))
                        print("[COMIDA FINALIZADA] El cliente {0} termino de comer normalmente y se fue al instante"
                              " {1}".format(cliente.name,
                                            round(self.env.now, 2)))
        except simpy.Interrupt:
            print("[PACIENCIA] El cliente {0} se le acabo la paciencia "
                  "y se fue del restaurante al instante {1}, alcanzo a esperar {2} minutos".
                  format(cliente.name,
                         round(self.env.now, 2),
                         round(paciencia(cliente), 2)))




def generador_clientes(env, lambdat, res):
    count = 0
    while True:
        yield env.timeout(random.expovariate(1 / lambdat))
        priority = random.randint(0, 25)
        cliente = Cliente(name=NAME.format(
            count), priority=priority, arrive=int(env.now), arrival_number=count)
        print("[LLEGADA] {0} ha arrivado al restaurant al instante {1} "
              "y es el cliente numero {2} del dia".format
            (
            cliente.name,
            round(env.now, 2),
            count
        ))
        count += 1
        env.process(res.espera(cliente))


if __name__ == '__main__':
    # Implemente el input de los parametros como se pide en el enunciado.
    TABLES = int(input("TABLES: "))
    INTERVAL = int(input("INTERVAL: "))
    SIM_TIME = int(input("SIM TIME: "))
    NAME = "Cliente {0}"
    env = simpy.Environment()
    res = Restaurante(env, TABLES)
    lambdat = INTERVAL
    env.process(generador_clientes(env, lambdat, res))
    env.run(until=SIM_TIME)
