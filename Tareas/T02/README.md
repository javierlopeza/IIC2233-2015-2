## Tarea 02

**1.** Debido a no poder saber la cantidad de puertos a los que llevan las conexiones aleatorias
pasaré 10 veces por cada conexión y así poder clasificarlas. Luego de eso podré dar por recorrida toda la Red.
Para esto se usará bastante tiempo ya que suponiendo que la Red tiene 1100 puertos (cantidad 
promedio aproximada que observé) y suponiendo que cada puerto tiene en promedio aproximadamente
5 conexiones, queriendo recorrer cada una 10 veces, se tendrán que realizar aún más de 55000 conexiones, 
ya que por culpa del Robot debo volver a empezar desde mi PC (puerto 0) cuando me encuentra husmeando.
Debido al problema del Robot y a las conexiones que va almacenando en memoria,
el tiempo puede variar dependiendo de la cantidad de veces que me pilla en la Red y el total de
conexiones que se almacenan en el sistema. También, para las últimas conexiones que les falten "pasadas" 
será más tedioso llegar a ellas ya que debo pasar por conexiones que ya completaron sus 10 pasadas.

**2.** Voy a suponer que de las 10 veces que paso por una conexion **alternante** siempre
existen 8 veces consecutivas en las que pasé solamente yo (es decir, de las 8 veces
el Robot no pasó nunca por esa conexión). Es por esto que puedo suponer en base a probabilidades que,
si de las 8 veces que pasé efectivamente fueron alternadas entre 2 puertos, entonces la conexión 
es alternante. La probabilidad de que las 8 veces sucedan alternadas sin ser una conexion
alternada es de aproximadamente 0.0078, es decir, 0.78%, por lo que es realmente muy poco probable 
realizar dicha clasificación erroneamente.

**3.** Si descubro que una conexión me envió a más de dos puertos diferentes, sé de
inmediato que es del tipo aleatoria.


**4.** Las Rutas Doble Sentido se detectan y arman perfectamente. Lo probé con casos más pequeños.