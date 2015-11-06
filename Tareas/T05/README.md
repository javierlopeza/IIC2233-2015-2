## Tarea 05

### Consideraciones

* El Militar puede mover con las flechas o con WASD y, al mismo tiempo, dirigirlo con el mouse.

* El Militar choca con las paredes.

* Los Zombies se dirigen constantemente a la posición del Militar.

* Los Zombies, al tocar al Militar le provocan un daño aleatorio entero entre 1 y 3, con un tiempo aleatorio de ```uniform(0.4, 1)``` segundos entre cada ataque. Consideré que estos valores permiten un correcto funcionamiento del juego, sin hacerlo ni muy dificil ni muy facil.

* El **Control de Colisiones** es simple: si el personaje (Militar/Zombie) intenta moverse a una posicion ocupada por otro personaje, simplemente no se mueve.

* El Militar es más hábil que los Zombies, por lo que tiene la capacidad de avanzar por espacios más estrechos.