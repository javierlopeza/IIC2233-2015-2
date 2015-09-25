## Tarea 03

###Borrador

vacio


###Dudas:

nada por el momento


###Pendiente:

TESTEAR FUNCIONES


### Consideraciones

* Al inicio de la partida se pide elegir si se jugará **contra otra persona o contra la computadora**. Se debe ingresar *p* para la primera opción o *c* para la segunda opción.


* Luego de elegir el tipo de oponente, **se inscriben el o los nombres** de los participantes.


* Luego de inscribir los nombres, se pide **ingresar el tamaño de los mapas** que se van a usar en la partida. Solo se pide ingresar la dimensión *n* ya que **cada sector del mapa es cuadrado de n x n**.


* Luego se **cargan en la flota de cada jugador un vehículo de cada tipo** existente. Se pide **setear la orientación** de cada uno de ellos y luego la coordenada donde serán **posiciónados inicialmente**.


* Luego **por sorteo** se elige el jugador que comienza la partida.


* Agregué la opción *Terminar Turno* para que los jugadores tengan la posibilidad de
finalizar su turno sin realizar ninguna acción.


* Para **consultar un estado del radar** en un turno pasado, se debe elegir la opción *Ver Historial Radar* e ingresar el turno donde se quiere revisar el estado del radar. Se permite revisar el historial todas las veces que quiera en un turno.


* Los vehículos **mantendrán para siempre su orientación impuesta inicialmente**. Es decir, al moverse entre las casillas del mapa estarán orientados siempre en la misma dirección.


* Los **vehículos aéreos no se pueden destruir**. Solo el explorador puede ser paralizado. Los vehículos aéreos se pueden mover a cualquier casilla
de su sector.


* Al **destruir un vehículo este desaparece**, es decir, *se hunde*.


* Los vehículos se pueden **mover en los ejes verticales y horizontales**, no en diagonal.


* Solo los vehículos marítimos tienen el ataque *GBU-43/B Massive Ordnance Air Blast Paralizer*.


* La **Lancha NO tiene ningún ataque**, solo puede moverse libremente para distraer al enemigo. Por ejemplo, si mi enemigo descubrió un vehículo mío (la Lancha) al explorar, yo sabré que el me espió en ciertas casillas y podré mover, en este caso la Lancha, rápidamente a cualquier casilla.


* Para **atacar al oponente**, primero se debe seleccionar el vehículo disponible que se quiere usar, luego seleccionar un ataque disponible que tenga y luego ingresar la casilla *i,j* oponente destino del ataque. Luego de atacar se imprime si el ataque fue efectivo o no, también se agrega dicha efectividad al radar marcando con una O si fue al agua y con una A si fue sobre un vehículo.

* El ataque **Misil de crucrero BGM-109 Tomahawk** ataca toda una fila o columna oponente, la cual se debe especificar al usarlo. Retorna si el ataque fue exitoso (cayo sobre algun vehículo enemigo) o no fue exitoso (todo el ataque cayo en el mar). En caso de ser exitoso entrega la cantidad de piezas afectadas por el ataque. No cambia nada en el radar pues no entrega coordenadas de los ataques exitosos o fallidos, a excepción de destruir un vehículo donde marca en el radar, con una X, las casillas usadas por el vehículo destruido. 

* En caso de **destruir un vehículo enemigo**, mi radar se marca con X en todas las casillas donde estaba el vehículo destruido. Esto debido a la condición de que al destruir un vehículo del oponente se entreguen las coordenadas donde se encontraba.

* El **Kit de Ingenieros** solo se usará sobre vehículos marítimos. Un vehículo sin daños no puede recibir el Kit de Ingenieros. Sí se puede usar sobre el mismo Puerto. Aumenta la vida del vehículo reparado en 1 unidad (sin poder sobrepasar su resistencia inicial).


* Si el **Avión Explorador** se encuentra paralizado no puede Explorar, *pero* si puede usar el ataque Misil UGM-133 Trident II y moverse.


* Al utilizar **explorar**, se debe ingresar la casilla central del area de 3x3 que se quiere explorar.
Es decir, si tengo el siguiente mapa de 10x10 y quiero explorar el area marcada con *E*:
	```python
                         SECTOR MARITIMO
       0    1    2    3    4    5    6    7    8    9  
   0  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   1  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   2  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   3  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   4  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   5  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   6  ~    ~    ~    E    E    E    ~    ~    ~    ~     
   7  ~    ~    ~    E    E    E    ~    ~    ~    ~     
   8  ~    ~    ~    E    E    E    ~    ~    ~    ~     
   9  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
	```
	debo ingresar la casilla *7,4*. 

* El **Avión Explorador no se mueve de su posición al explorar**, es algo así como que *va a explorar y vuelve* o como si lanzara un *ataque explorador* a dicha área de 3x3, como se entienda mejor.

* Si el **explorador descubre** alguna pieza enemiga en el área explorada, se marcarán en el radar con una F las casillas de dichas piezas descubiertas. 

* También, siempre se le notificará al jugador espiado las casillas en que el Avión Explorador enemigo encontró piezas de sus vehículos (en Casillas Espiadas).

* Si el explorador **revela una de las coordenadas** de su ubicación (con 50% de probabilidad) se marca con una E la casilla revelada del sector aéreo del radar enemigo.

* Para intentar **paralizar el Avión Explorador enemigo**, se debe elegir dicha opción he ingresar las coordenadas en el formato ```i,j h,k```, por ejemplo: ```2,3 2,4```. Estas coordenadas corresponden a las que se deben acertar (ambas) para poder efectivamente paralizar el Avión Explorador enemigo por 5 turnos.

* Consideré que la **disponibilidad** que se menciona para los ataques, por ejemplo, para el Kit de Ingenieros (disponibilidad cada 2 turnos), significa que si se usa dicho ataque en un turno 1, el turno 2 siguiente no podré usarlo, pero en el turno 3 subsiguiente sí podre usarlo. Es análogo para todos los ataques.


* **La partida finaliza** cuando un jugador tiene en su flota marítima **solo la Lancha**, o no tiene **ningún vehículo** en dicha flota (puede pasar que el oponente destruya la Lancha antes de destruir otros vehículos marítimos).


* Para **mover un vehículo**, este tendrá una *property* ```posición_guia->list``` donde ```posición_guia[0]->int``` indica la fila y ```posición_guia[1]->int``` indica la columna de la casilla donde se encuentra la **posición guía** del vehículo. 
Por ejemplo en un ```mapa``` de 10x10 se ubica el Buque de Guerra ```buque```, el cual su posición guía esta dada por la letra mínuscula ```g```:
	```python
                         SECTOR MARITIMO
       0    1    2    3    4    5    6    7    8    9  
   0  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   1  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   2  ~    ~    g    G    G    ~    ~    ~    ~    ~     
   3  ~    ~    G    G    G    ~    ~    ~    ~    ~     
   4  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   5  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   6  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   7  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   8  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   9  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
	```
	En este caso,  ```buque.posición_guia = [2,2]``` .  Si deseo moverlo una posición a la izquierda, debo indicar su movimiento respecto a la posición guía, es decir:
	```python	
	coordenadas = '2,1'  # Durante la partida se usan inputs
	mapa.mover_vehículo(buque, coordenadas)
	```
lo que provocará que la posición guia quede en la casilla (2,1):
	```python
                         SECTOR MARITIMO
       0    1    2    3    4    5    6    7    8    9
   0  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~ 
   1  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   2  ~    g    G    G    ~    ~    ~    ~    ~    ~     
   3  ~    G    G    G    ~    ~    ~    ~    ~    ~     
   4  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   5  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   6  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   7  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   8  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     
   9  ~    ~    ~    ~    ~    ~    ~    ~    ~    ~     

	```


* Se calculan los puntos de eficiencia de un ataque como ```eficiencia = daño_causado/veces_usado```.

* En general, para estadísticas de ataques, se consideran todos los ataques menos el *Kit de Ingenieros .*

* Como el ataque *GBU-43/B Massive Ordnance Air Blast Paralizer* no causa daño sobre el Avión Explorador paralizado, para el *ataque más eficiente* este ataque no se considerara, ya que no podría calcular la eficiencia de este si no causa daños sobre oponentes.

* Para el *Misil de crucrero BGM-109 Tomahawk* se considera un ataque exitoso si alcanzó al menos una pieza enemiga. Es decir, si alcanzó una o más piezas enemigas, sus éxitos aumentan en 1 unidad.

* Para el *ataque más utilizado*, *el barco con más movimientos* y *el ataque más eficiente* si es que hay más de un ataque/barco que cumple con la condición, se muestran todos los que la cumplen. 

### Inteligencia de la Computadora

**Se detallarán en esta sección las características que determinan la inteligencia de la computadora cuando jugamos contra ella.**

* La computadora **no revelará información secreta** de sus acciones a la persona contrincante (sino seria obvio ganarle). Por ejemplo, si la computadora mueve algún vehículo, obviamente no se imprimirá en consola dónde fue movido el vehículo.

* Para **posicionar vehículos**, pienso que no existe una estrategia inteligente para ubicarlos, así que simplemente la computadora los ubicará todos libremente en su mapa (aleatoriamente) y en orientaciones arbitrarias.

* En este modo de juego, siempre comienza jugando la persona.

* Cuando le toca jugar a la Computadora, se genera internamente (invisible) un conjunto de opciones entre las que puede elegir ciertas acciones. La acción que elija se determina por las prioridades señaladas a continuación.

* **Las prioridades de sus acciones se ordenan así**:

	1. Si en su radar hay alguna letra A, significa que en esa casilla hay un vehículo que ha atacado pero no ha muerto. Por lo tanto ataca en dicha casilla.

	2. Si en su radar hay alguna letra F, significa que ha explorado antes y encontrado un vehículo en esa casilla. Por lo tanto ataca dicha casilla.

	3. Si tiene casillas espiadas y hay algún vehículo en ellas, mueve inmediatamente un vehículo fuera de dichas casillas. Porque significa que el enemigo ha descubierto dicho vehículo y pretenderá atacarlo en su próximo turno. Luego de mover dicho vehículo elimina las casillas de casillas espiadas, pues ya no es una preocupación para la computadora.

	4. Si el Avión Explorador esta paralizado y le queda 1 turno para volver a la normalidad, se mueve a cualquier casilla (sí, puede moverse aunque esté paralizado) para escapar de volver a ser paralizado en otra instancia.

	5. Se elige aleatoriamente una de las siguientes opciones (de las disponibles):

		* Explorar una zona aleatoria del mapa enemigo.
	
		* Si el Avión Explorador enemigo no esta paralizado, si es que en su radar hay una E significa que el Avión Explorador enemigo le revelo una coordenada. Se dispara el Paralizador a esa coordenada y a una contigua elegida aleatoriamente. El vehículo que dispara el Paralizador se elige aleatoriamente entre los que poseen dicho ataque.
	
		* Si algún vehículo de la flota propia esta dañado, se usa el Kit de Ingenieros sobre él.


* **Al atacar, la computadora tiene las siguientes prioridades de ataques (por severidad):**
1. Kamikaze
2. Misil Balístico Intercontinental Minuteman III 
3. Misil de crucero BGM-109 Tomahawk (en un eje aleatorio que cruce la casilla objetivo)
4. Misil UGM-133 Trident II
5. Napalm

* Con este metodo la computadora de todas maneras tiene probabilidades de ganar la partida (lo probé y logra ganarme :unamused:).
