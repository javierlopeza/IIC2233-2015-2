## Tarea 02

**0.** Se pide detallar cómo implementé las estructuras que utilicé en la Tarea 2.
La estructura que construí fue ```ListaLigada```.
Se construye de la siguiente manera:

XXXX ------------------XXXXXXXX-------------XXXXXXXX

**1.** Debido a no poder saber la cantidad de puertos a los que llevan las conexiones aleatorias
pasaré 10 veces por cada conexión para así poder clasificarlas correctamente. 
Es importante notar que al no saber si algunas conexiones me llevan a puertos que no había descubierto,
no puedo minimizar más la construcción de la red, ya que la red tiene forma de grafo y sino podría 
perder tramos de esta.
Luego de recorrer 10 veces cada conexión podré dar por recorrida toda la Red.
Para esto se usará bastante tiempo ya que suponiendo que la Red tiene 1100 puertos (cantidad 
promedio aproximada que observé) y suponiendo que cada puerto tiene en promedio aproximadamente
5 posibles conexiones, queriendo recorrer cada una 10 veces, se tendrán que realizar aún más de 55000 conexiones, 
ya que por culpa del Robot debo volver a empezar desde mi PC (puerto 0) cuando me encuentra husmeando.
Debido al problema del Robot y a las conexiones que va almacenando en memoria,
el tiempo puede variar dependiendo de la cantidad de veces que me pilla en la Red y el total de
conexiones que se almacenan en el sistema. También, para las últimas conexiones que les falten "pasadas" 
será más tedioso llegar a ellas ya que debo pasar por conexiones que ya completaron sus 10 pasadas.

**2.** Voy a suponer que de las 10 veces que paso por una conexion **alternante** siempre
existen 7 veces consecutivas en las que pasé solamente yo (es decir, de las 7 veces
el Robot no pasó nunca por esa conexión). Es por esto que puedo suponer en base a probabilidades que,
si de las 7 veces que pasé efectivamente fueron alternadas entre 2 puertos, entonces la conexión 
es alternante. La probabilidad de que las 7 veces sucedan alternadas sin ser una conexion
alternada es de aproximadamente 0.015625, es decir, 1.5625% de probabilidades de realizar erroneamente
la clasificacion.

**3.** Si descubro que una conexión me envió a más de dos puertos diferentes, sé de
inmediato que es del tipo aleatoria.

**4.** El programa da la opción de considerar las rutas ALT y RAND, o no considerarlas para 
cargar la red. Al considerarlas el programa demora 10 veces más tiempo ya que debe
recorrer 10 veces cada conexión. Es por esto que al no considerarlas, obviamente no realiza la clasificación,
pero si es que son consideradas sí realiza la clasificación de las conexiones, mostrando el tipo de ellas en el 
archivo *red.txt*.

**5.** Para efectos de encontrar la ruta de capacidad máxima, se consideran todas las conexiones como normales,
aun cuando se hayan encontrado las conexiones RAND y ALT.

**6.** Debido a que mi algoritmo de modelar la red no es rápido, lo corrí una vez y guarde en el archivo
*ARCOS.txt* todos los arcos del grafo de la red. Con estos arcos pude testear de manera correcta la
detección de ciclos triangulares y cuadrados, y encontrar los caminos a Bummer.
Para la detección de rutas bidireccionales, utilicé la 'lista' de todos los pares de padres-destinos
que se crea al momento de hacer ```cargar_padres(hacker)```. Consideré esto más útil en esta parte de la tarea.

**7.** Para la parte III donde se pide hackear la red, lo que hice fue ir revisando conexión a conexión, si
al eliminar una dejaba de ser o no fuertemente conexo. De esta forma si al eliminar una conexión se mantenía 
fuertemente conexo, eliminaba definitivamente dicha conexión de la red que se escribirá en el archivo *noCycle.txt*.
Para testear el hackeo usé la siguiente mini_red (implementada con las ListaLigada obviamente, pero aquí la escribo como
listas de python para facilitar comprensión del ejemplo):
```
mini_red = [
    [0, [2, 3]],
    [1, [0, 6]],
    [2, [1, 5]],
    [3, [5, 10]],
    [4, [1, 2, 7]],
    [5, [0, 4]],
    [6, [8, 9]],
    [7, [1, 6]],
    [8, [3, 5]],
    [9, [7, 10]],
    [10, [5, 8]]
]
```
Luego, al usar el metodo ```hackear_red(mini_red)``` se retorna la mini_red con menos conexiones manteniendose fuertemente conexa.
```
print(es_fuertemente_conexo(mini_red)) 
# True

print(hackear_red(mini_red)) 
'''
mini_red = [
    [0, [3]],
    [1, [6]],
    [2, [5]],
    [3, [10]],
    [4, [2, 7]],
    [5, [4, 0]],
    [6, [9]],
    [7, [6, 1]],
    [8, [5]],
    [9, [10]],
    [10, [8]]
]
'''
```