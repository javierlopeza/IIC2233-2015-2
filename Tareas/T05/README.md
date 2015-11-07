## Tarea 05

### Pendiente

* Revisar funcion lambda(t) frecuencia zombies.

* Helicoptero que entrega cajas de salud y de municiones.

* Disparo de balas.

* Pausar juego.

* Puntaje.

* Menu inicial.

* Menu final.
 
* (?) Buscar mejores SS Zombies.


### Consideraciones

* El Militar puede mover con las flechas o con WASD y, al mismo tiempo, dirigirlo con el mouse.

* El Militar choca con las paredes.

* El tiempo entre llegadas de los Zombies distribuye Exponencial(lambda(t)) donde ```lambda(t) =  1 / log(t + 1, 10)``` es la función de la tasa que aumenta a medida que avanza el tiempo t de una partida, para todo t mayor a 0.

* Los Zombies se dirigen constantemente a la posición del Militar.

* Los Zombies, al tocar al Militar le provocan un daño aleatorio entero entre 1 y 3, con un tiempo aleatorio de ```uniform(0.4, 1)``` segundos entre cada ataque. Consideré que estos valores permiten un correcto funcionamiento del juego, sin hacerlo ni muy dificil ni muy facil.

* El Militar por su parte, al ser atacado, disminuye su vida según lo que el Zombie lo dañe y se muestra gráficamente este ataque al disminuir el ancho de la Barra de Salud en la parte superior de la interfaz.

* El **Control de Colisiones** es simple: si el personaje (Militar/Zombie) intenta moverse a una posicion ocupada por otro personaje, simplemente no se mueve.

* El Militar es más hábil que los Zombies, por lo que tiene la capacidad de avanzar por espacios más estrechos.

* Por una razón que desconozco, el juego se empieza a poner lento cuando hay más de 25 zombies en la Zona de Juego. Por esta razón es que dejaré 25 como máximo de Zombies en un mismo instante.

* Como no se pide considerar las colisiones con los objetos entregados por el helicoptero, a veces, extrañamente, los Zombies podrán pasar "por debajo" de las cajas.

* El puntaje se calcula según el tiempo transcurrido y según la cantidad de Zombies matados. Cada segundo que transcurre le suma 12 al puntaje, premiandolo por la sobrevivencia. Mientras que cada Zombie que mata le suma 57 * t, donde t es el tiempo transcurrido, premiandolo por los Zombies matados y el agotamiento que provoca estar tanto tiempo.

* Las Balas van a una velocidad relativamente lenta con el fin de que gráficamente se vea su trayectoria. Esto no afecta en la precisión de la pistola, ya que los Zombies son lentos.

* En general, todas las velocidades de los personajes y las balas se pueden modificar fácilmente en el programa.



