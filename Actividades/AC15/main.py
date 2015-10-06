import threading


class Worker(threading.Thread):
    workers_terminaron = []
    workers_actuales = []
    mean_data = dict()      # para guardar los promedios
    # Sientete libre para usar otras
    # variables estaticas aqui si quieres

    # programa el __init__
    # recuerda imprimir cual es el comando
    # para el cual se creo el worker
    def __init__(self, star_name, function_name):
        super().__init__()
        self.daemon = True
        self.star_name = star_name
        self.func_name = function_name

    @staticmethod
    def functions(func_name):
        """
        Este metodo recibe el nombre de una funcion
        y retorna una funcion que calcula promedio
        o varianza segun el argumento.
        Se necesita haber calculado promedio
        para poder calcular varianza
        """

        def mean(star_name):
            if not ('mean',star_name) in Worker.workers_actuales:
                print('Creando worker para : mean {0}'.format(star_name))
                Worker.workers_actuales.append(('mean',star_name))
                with open("{}.txt".format(star_name), 'r') as file:
                    lines = file.readlines()
                    ans = sum(map(lambda l: float(l), lines))/len(lines)
                    Worker.mean_data[star_name] = ans
                    Worker.workers_actuales.remove(('mean',star_name))
                    return ans
            else:
                print('[ DENIED ] Ya hay un worker ejecutando el comando)')

        def var(star_name):
            if not ('var',star_name) in Worker.workers_actuales:
                if star_name in Worker.mean_data:
                    print('Creando worker para : var {0}'.format(star_name))
                    Worker.workers_actuales.append(('var',star_name))
                    prom = Worker.mean_data[star_name]
                    with open("{}.txt".format(star_name), 'r') as file:
                        lines = file.readlines()
                        n = len(lines)
                        suma = sum(map(lambda l: (float(l) - prom)**2, lines))
                        Worker.workers_actuales.remove(('var',star_name))
                        return suma/(n-1)
                else:
                    print('[ DENIED ] No se puede calcular varianza sin haber calculado el promedio antes !')
            else:
                print('[ DENIED ] Ya hay un worker ejecutando el comando)')

        return locals()[func_name]

    # escriba el metodo run
    def run(self):
        funcion_usada = self.functions(self.func_name)
        ret = funcion_usada(self.star_name)
        if ret:
            print('Soy el {0} y termine mi trabajo !'.format(self.name))
            print('    El resultado de {0} {1} es {2}'.format(self.func_name, self.star_name, ret))
            Worker.workers_terminaron.append((self.func_name, self.star_name))


if __name__ == "__main__":
    estrellas = ['Sirius', 'AlphaCentauri', 'Arcturus', 'Canopus', 'Vega']
    command = input("Ingrese siguiente comando:\n")
    while command != "exit":
        # Complete el main:
        #   - Que no se caiga el programa al ingresar inputs invalidos
        #   - Revisar que no haya un worker ejecutando el comando
        #   - Revisar que solo se puede calcular var estrella
        #           si ya se calculo mean estrella
        #   - Si corresponde: crear worker, echarlo a correr
        if len(command.split(' ')) == 2 \
                and ('mean' == command.split(' ')[0] or 'var' == command.split(' ')[0]) \
                and command.split(' ')[1] in estrellas:
            funcion = command.split(" ")[0]
            estrella = command.split(" ")[1]
            nuevo_worker = Worker(star_name=estrella, function_name=funcion)
            nuevo_worker.start()

        command = input("Ingrese siguiente comando:\n")

    print('Comandos ingresados por el usuario')
    for w in Worker.workers_terminaron:
        print('Alcanzo a terminar: {0} {1}'.format(w[0], w[1]))
    for n in Worker.workers_actuales:
        print('No alcanzo a terminar: {0} {1}'.format(n[0], n[1]))

    # imprimir cuales comandos
    # alcanzaron a terminar, y cuales no
