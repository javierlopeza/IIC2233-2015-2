## Tarea 03

###Borrador

(para el menu que le aparece al jugador cuando le toca jugar)

>Ver mi mapa

>Ver radar (printea radar y vuelve al menu >) LISTO

>Consultar historial radar

>Mover vehiculo (mueve vehiculo y termina turno) LISTO

>Atacar oponente (ataca oponente y termina turno) LISTO

>Explorar (explora y termina turno)

>Kit de Ingenieros






###Dudas:

nada por el momento



###Pendiente:

CARGAR MODO COMPUTADORA

HISTORIAL RADAR

TESTEAR FUNCIONES


### Consideraciones

* Al inicio de la partida se pide elegir si se jugara contra otra persona o contra la computadora.
Se debe ingresar *p* para la primera opcion o *c* para la segunda opcion.


* Luego de elegir el tipo de oponente, se inscriben el o los nombre de los participantes.


* Luego de inscribir los nombres, se pide ingresar el tamaño de los mapas que se van a usar en la partida.
Solo se pide ingresar la dimension *n* ya que el mapa es cuadrado de *n x n*.


* Luego se cargan en la flota de cada jugador un vehiculo de cada tipo existente. Se pide setear la orientacion 
de cada uno de ellos y luego la coordenada donde seran posicionados inicialmente.


* Luego por sorteo se elige el jugador que comienza la partida.


* Los vehiculos mantendran para siempre su orientación impuesta inicialmente. Es decir, al moverse 
entre las casillas del mapa estarán orientados siempre en la misma dirección.


* Los vehiculos aereos no se pueden mover, ni destruir. Solo el explorador puede ser paralizado.


* Los vehiculos se pueden mover en los ejes verticales y horizontales, no en diagonal.


* Solo los vehiculos maritimos tienen el ataque *GBU-43/B Massive Ordnance Air Blast Paralizer*.


* La Lancha si tiene el ataque Misil UGM-133 Trident II.


* Para atacar al oponente, primero se debe seleccionar el vehiculo disponible que se quiere usar, luego
seleccionar un ataque disponible que tenga y luego ingresar la casilla *i,j* oponente destino del ataque.
Luego de atacar se imprime si el ataque fue efectivo o no, tambien se agrega dicha efectividad al radar 
marcando con una O si fue al agua y con una X si fue sobre un vehiculo.


* El ataque Misil de crucrero BGM-109 Tomahawk ataca toda una fila oponente, la cual se debe indicar al 
usarlo. Retorna si el ataque fue exitoso (cayo sobre algun vehiculo enemigo) o no fue exitoso (todo el
ataque cayo en el mar). No cambia nada en el radar pues no entrega coordenadas de los ataques exitosos o fallidos.


* En caso de destruir un vehiculo enemigo, mi radar se marca con X en todas las casillas donde estaba el vehiculo destruido.
Esto debido a la condicion de que al destruir un vehiculo del oponente se entreguen las coordenadas donde se encontraba.


* Consideré que la disponibilidad que se menciona para los ataques, por ejemplo, para el Kit de Ingenieros
(disponibilidad cada 2 turnos), significa que si se usa dicho ataque en un turno 1, el turno 2 siguiente no podré
usarlo, pero en el turno 3 subsiguiente sí podre usarlo. Es analogo para todos los ataques.


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
y quiero explorar el area marcada con *E*, debo ingresar la casilla *7,4*

* La partida finaliza cuando un jugador tiene en su flota maritima solo la Lancha, o no tiene ningun vehiculo en dicha flota.
(puede pasar que el oponente destruya la Lancha antes de destruir otros vehiculos maritimos).


* Para mover un vehículo de dimensiones, por ejemplo, de 2x3, este tendrá una property
```posicion_guia->list``` donde ```posicion_guia[0]->int``` indica la fila y ```posicion_guia[1]->int``` 
indica la columna de la casilla donde se encuentra la *parte guía* del vehículo. 
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