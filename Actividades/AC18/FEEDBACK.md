### Distribución de puntajes

Requerimientos (**R**):

* **(3.0 pts)** R1: El programa imprime registro de todos los eventos que ocurren.
* **(1.0 pts)** R2: Paciencia de los clientes, se van despues de un cierto tiempo de espera.
* **(1.0 pts)** R3: Los clientes llamados por celular se van sin terminar.
* **(1.0 pts)** R4: Crea un main parametrizable.

**Además, se descontará (0.2) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | R4 |Descuento |
|:---|:---|:---|:---|:----------|
| 3.0 | 1.0 | 1.0  | 0.5|  0|

| Nota |
|:-----|
| 6.5 |

### Comentarios

No se requiere el try catch.

No era necesario, que sean parametros significa que en el main aparezcan bajo los nombres de las variables (a las que les das valor al comienzo del programa)
    TABLES = int(input("TABLES: "))
    INTERVAL = int(input("INTERVAL: "))
    SIM_TIME = int(input("SIM TIME: "))

Bastaba con
    env = simpy.Environment()
    res = Restaurante(env, TABLES)
    env.process(generador_clientes(env, INTERVAL, res))
    env.run(until=SIM_TIME)

Con esta pequeña modificación tu programa corre.

* Sin Comentarios
