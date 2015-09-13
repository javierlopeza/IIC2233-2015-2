## Tarea 02

**1.** Debido a no poder saber la cantidad de puertos a los que llevan las conexiones aleatorias
pasaré 20 veces por cada conexión. Luego de eso podré dar por recorrida toda la Red.
Para esto se usará bastante tiempo ya que suponiendo que la Red tiene 1100 puertos (cantidad 
promedio aproximadamente que observé) y suponiendo que cada puerto tiene en promedio aproximandamente
5 conexiones, queriendo recorrer cada una 20 veces, se tendrán que realizar aún más de 110000 conexiones, 
ya que por culpa del Robot debo volver a empezar desde mi PC cuando me encuentra husmeando y hay veces que
me veo obligado a realizar conexiones donde ya he realizado las necesarias.
En promedio, he notado que el programa demora aproximadamente 0.02 segundos en encontrar y usar una conexión 
por la cual todavía no pasa 20 veces.
Por ejemplo, para una ejecución del programa, descubrí ** XXXX puertos**, tuve que hacer un total de 
** XXXX conexiones** y demoré un total de 


**1.** Voy a suponer que de las 20 veces que paso por una conexion **alternante** siempre
existen 8 veces consecutivas en las que pasé solamente yo (es decir, de las 8 veces
el Robot no pasó nunca por esa conexión). Es por esto que puedo suponer en base a probabilidades que,
si de las 8 veces que pasé efectivamente fueron alternadas entre 2 puertos, entonces la conexión 
es alternante. La probabilidad de que las 8 veces sucedan alternadas sin ser una conexion
alternada es de aproximadamente 0.0078, es decir, 0.78%, por lo que es realmente muy poco probable 
realizar dicha clasificación erroneamente.

**2.** Si descubro que una conexión me envió a más de dos puertos diferentes, sé de
inmediato que es del tipo aleatoria.


