## Tarea 03

###Borrador

vacio


###Dudas:

nada por el momento


###Pendiente:

TESTEAR FUNCIONES


### Consideraciones

* Al inicio de la partida se pide elegir si se jugara contra otra persona o contra la computadora.
Se debe ingresar *p* para la primera opcion o *c* para la segunda opcion.


* Luego de elegir el tipo de oponente, se inscriben el o los nombres de los participantes.


* Luego de inscribir los nombres, se pide ingresar el tamaño de los mapas que se van a usar en la partida.
Solo se pide ingresar la dimension *n* ya que el mapa es cuadrado de *n x n*.


* Luego se cargan en la flota de cada jugador un vehiculo de cada tipo existente. Se pide setear la orientacion 
de cada uno de ellos y luego la coordenada donde seran posicionados inicialmente.


* Luego por sorteo se elige el jugador que comienza la partida.


* Agregué la opcion *Terminar Turno* para que los jugadores tengan la posibilidad de
finalizar su turno sin realizar ninguna acción.


* Para consultar un estado del radar en un turno pasado, se debe elegir la opcion *Ver Historial Radar* e ingresar
el turno donde se quiere revisar el estador del radar. Se permite revisar el historial todas las veces que quiera en un turno.


* Los vehiculos mantendran para siempre su orientación impuesta inicialmente. Es decir, al moverse 
entre las casillas del mapa estarán orientados siempre en la misma dirección.


* Los vehiculos aereos no se pueden destruir. Solo el explorador puede ser paralizado. Los vehiculos aereos se pueden mover a cualquier casilla
de su sector.


* Los vehiculos se pueden mover en los ejes verticales y horizontales, no en diagonal.


* Solo los vehiculos maritimos tienen el ataque *GBU-43/B Massive Ordnance Air Blast Paralizer*.


* La Lancha NO tiene ningún ataque, solo puede moverse libremente para distraer al enemigo.


* Para atacar al oponente, primero se debe seleccionar el vehiculo disponible que se quiere usar, luego
seleccionar un ataque disponible que tenga y luego ingresar la casilla *i,j* oponente destino del ataque.
Luego de atacar se imprime si el ataque fue efectivo o no, tambien se agrega dicha efectividad al radar 
marcando con una O si fue al agua y con una X si fue sobre un vehiculo.


* El ataque Misil de crucrero BGM-109 Tomahawk ataca toda una fila o columna oponente, la cual se debe especificar al 
usarlo. Retorna si el ataque fue exitoso (cayo sobre algun vehiculo enemigo) o no fue exitoso (todo el
ataque cayo en el mar). En caso de ser exitoso entrega la cantidad de piezas afectadas por el ataque.
No cambia nada en el radar pues no entrega coordenadas de los ataques exitosos o fallidos, a excepcion de destruir un
vehiculo donde marca en el radar, con una X, las casillas usadas por el vehiculo destruido. 


* En caso de destruir un vehiculo enemigo, mi radar se marca con X en todas las casillas donde estaba el vehiculo destruido.
Esto debido a la condicion de que al destruir un vehiculo del oponente se entreguen las coordenadas donde se encontraba.


* El Kit de Ingenieros solo se usará sobre vehículos marítimos. Un vehiculo sin daños no puede recibir el Kit de Ingenieros.
Sí se puede usar sobre el mismo Puerto.


* Si el Avion Explorador se encuentra paralizado no puede Explorar, pero si puede usar el ataque Misil UGM-133 Trident II.


* Al utilizar *explorar*, se debe ingresar la casilla central del area de 3x3 que se quiere explorar.
Es decir, si tengo el siguiente mapa de 10x10:
 ```
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
y quiero explorar el area marcada con *E*, debo ingresar la casilla *7,4*. El Avion Explorador no se mueve de su posicion al explorar,
es algo asi como que 'va a explorar y vuelve' o como si lanzara un 'ataque explorador', como se entienda mejor.


* Si el explorador descubre que hay uno o varios barcos en el area explorada, se marcan en el radar del jugador
las casillas donde existe un barco enemigo con una F. Tambien, siempre se le notifica al jugador espiado las casillas en que el
Avion Explorador enemigo encontro vehiculos (Casillas Espiadas).


* Si el explorador revela una de sus coordenadas de su ubicacion (con 50% de probabilidad) se marca con una E en la casilla revelada 
del sector aereo del radar enemigo.


* Para intentar paralizar el Avion Explorador enemigo, se debe elegir dicha opcion he ingresar las coordenadas
en el formato ```i,j h,k```, por ejemplo: ```2,3 2,4```. Estas coordenadas corresponden a las que se deben acertar (ambas)
para poder efectivamente paralizar el Avion Explorador enemigo.


* Consideré que la **disponibilidad** que se menciona para los ataques, por ejemplo, para el Kit de Ingenieros
(disponibilidad cada 2 turnos), significa que si se usa dicho ataque en un turno 1, el turno 2 siguiente no podré
usarlo, pero en el turno 3 subsiguiente sí podre usarlo. Es analogo para todos los ataques.


* **La partida finaliza** cuando un jugador tiene en su flota maritima solo la Lancha, o no tiene ningun vehiculo en dicha flota.
(puede pasar que el oponente destruya la Lancha antes de destruir otros vehiculos maritimos).


* Para **mover un vehículo** de dimensiones, por ejemplo, de 2x3, este tendrá una property
```posicion_guia->list``` donde ```posicion_guia[0]->int``` indica la fila y ```posicion_guia[1]->int``` 
indica la columna de la casilla donde se encuentra la **parte guía** del vehículo. 
Por ejemplo en un mapa de 10x10:
```
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
se ubica el Buque de Guerra ```G```, el cual su posición guía esta dada por la letra mínuscula ```g```.
Si deseo moverlo una posicion a la izquierda, debo indicar su movimiento respecto a la posicion guia, es decir:
```python
Mapa(10).mover_vehiculo(buque)
coordenadas = 2,1  # pseudocodigo
```
lo que provocará que la posicion guia quede en la casilla (2,1):
```
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


* Como el ataque *GBU-43/B Massive Ordnance Air Blast Paralizer* no causa daño sobre el Avion Explorador paralizado,
para el *ataque más eficiente* este ataque no se considerara, ya que no podria calcular la eficiencia de este si no causa
daños sobre oponentes.


* Para los *ataques exitosos* se consideran todos los ataques menos el Kit de Ingenieros.


* Para el *Misil de crucrero BGM-109 Tomahawk* se considera un ataque exitoso si alcanzó al menos una pieza enemiga.
Si alcanzó una o más piezas enemigas, sus éxitos aumentan en 1 unidad.


* Para el *ataque mas utilizado*, *el barco con mas movimientos* y *el ataque mas eficiente* si es que hay mas de un ataque/barco
que cumple con la condicion, se muestran todos los que la cumplen. 



### Inteligencia de la Computadora

**Se detallarán en esta sección las características que determinan la inteligencia de la computadora cuando jugamos contra ella.**

* En general a las clases les di el atributo ```owner``` para que la computadora no revele informacion secreta a la persona
(sino seria muy facil ganarle).


* Para **posicionar vehiculos**, pienso que no existe una estrategia inteligente para ubicarlos, asi que simplemente 
la computadora los ubicará todos libremente en su mapa (aleatoriamente) y en orientaciones arbitrarias.


* En este modo de juego, siempre comienza jugando la persona.


* Cuando le toca jugar a la Computadora, se genera invisiblemente un menu de opciones entre las que puede elegir.


* Las prioridades de sus acciones se ordenan así:
-> Al atacar, la computadora tiene las siguientes prioridades de ataques (por severidad):
	I. Kamikaze
	II. Misil Balístico Intercontinental Minuteman III 
	III. Misil de crucero BGM-109 Tomahawk (en un eje aleatorio que cruce la casilla con la letra A)
	IV. Misil UGM-133 Trident II
	V. Napalm

1. Si en su radar hay alguna letra A, significa que en esa casilla hay un vehiculo que ha atacado pero no ha muerto. Por lo tanto
ataca en dicha casilla.

2. Si en su radar hay alguna letra F, significa que ha explorado antes y encontrado un vehiculo en esa casilla. Por lo tanto ataca
dicha casilla.

3. Si tiene casillas espiadas y hay algun vehiculo en ellas, mueve inmediatamente un vehiculo fuera de dichas casillas.
Esto porque significa que el enemigo ha descubierto dicho vehiculo y pretenderá atacarlo en su próximo turno. Luego de mover dicho
vehiculo elimina la casilla de casillas espiadas, pues ya no es una preocupacion.

4. Si el Avion Explorador esta paralizado y le queda 1 turno para volver a la normalidad,
se mueve a cualquier casilla (sí, puede moverse aunque esté paralizado) para escapar
de volver a ser paralizado en otra instancia.

5. Se elige aleatoriamente una de las siguientes opciones (de las disponibles):

5.1. Explorar una zona aleatoria del mapa enemigo.

5.2. Si el Avion Explorador enemigo no esta paralizado:
- Si es que en su radar hay una E significa que el Avion Explorador enemigo le revelo una coordenada. Se dispara el Paralizador
a esa coordenada y a una contigua elegida aleatoriamente. El vehiculo que dispara el Paralizador se elige aleatoriamente entre los que poseen dicho ataque.
- O en el caso de que ya tenga las dos coordenadas claves descubiertas, disparo el Paralizador directo a dichas dos coordenadas.

5.3. Si algun vehiculo de la flota propia esta dañado, se usa el Kit de Ingenieros sobre él.