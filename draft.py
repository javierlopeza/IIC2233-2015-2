import random
import simpy


RANDOM_SEED = 42          # Incluir para lograr repetibilidad en los resultados
NUM_MAQUINAS = 1           # Número de máquinas de lavado. Corresponde al problema de colas mm1
TIEMPO_LAVADO = 5          # El tiempo de atención de una máquina 
TIEMPO_LLEGADA = 7         # Se define el intervalo de llega de autos en 1 cada 7 minutos
TIEMPO_SIMULACION = 20     # tiempo de simulación en minutos


class MaquinaLavado:
    # Una máquina de lavado tiene un número limitado de maquinas. En este ejemplo solo una. 
    # Los vehículos solicitan el recurso de la máquina disponible mediante el método request().
    # Una vez que se le asigna el recurso, comienza el lavado y se debe esperar a que termine
    # en el TIEMPO_LAVADO difinido

    def __init__(self, env, num_maquinas, tiempo_lavado):
        self.env = env
        self.maquinas = simpy.Resource(env, capacity= num_maquinas)  # El recurso para una máquina
        self.tiempo_lavado = tiempo_lavado

    def lavar(self, vehiculo):
        # Definimos el lavado con un tiempo que distribuye exponencial a tasa 1/TIEMPO_LAVADO
        yield self.env.timeout(round(random.expovariate(1/self.tiempo_lavado) + 0.5))


def vehiculo(env, id_vehiculo, maquina_lavado):
    # Durante el lavado un vehiculo con id llega a la máquina y solicita el uso de la máquina.
    # Una vez que inicia el lavado, espera a que termine y luego deja la máquina.

    print('{0} llega a la maquina en {1:.2f}.'.format(id_vehiculo, env.now))
    
    with maquina_lavado.maquinas.request() as solicitud:
        yield solicitud

        print('{0} entra a la maquina en {1:.2f}.'.format(id_vehiculo, env.now))
        yield env.process(maquina_lavado.lavar(id_vehiculo))

        print('{0} deja la maquina en {1:.2f}.'.format(id_vehiculo, env.now))


def configuracion_sim(env, num_maquinas, tiempo_lavado, tiempo_llegada):
    # En esta rutina se crea la o las máquinas de lavado, un número inicial de autos (2), 
    # y luego siguen llegando autos a una tasa de 1/tiempo_llegada.
    
    # Crea una maquina de lavados
    maquina = MaquinaLavado(env, num_maquinas, tiempo_lavado)

    # Se crean 2 vehiculos que ya existen en la cola
    print('En la cola ya existen 2 vehiculos')
    for i in range(2):
        env.process(vehiculo(env, 'Vehiculo {0}'.format(i), maquina))

        
    # Mientras funciona la máquina siguen llegando más vehículos a una tasa 1/tiempo llegada
    while True:
        yield env.timeout(round(random.expovariate(1/tiempo_llegada) + 0.5))
        i += 1
        env.process(vehiculo(env, 'Vehiculo {0}'.format(i), maquina))


# Configuración de la simulación
random.seed(RANDOM_SEED)  # Inicializamos la secuencia aleatoria

# Crea el ambiente de simulación
env = simpy.Environment()
env.process(configuracion_sim(env, NUM_MAQUINAS, TIEMPO_LAVADO, TIEMPO_LLEGADA))

# Ejecuta la simulación duran TIEMPO_SIMULACION minutos
env.run(until=TIEMPO_SIMULACION)