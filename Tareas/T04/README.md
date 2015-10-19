## Tarea 03

### Consideraciones

* Al agregar una casa se fija el tiempo de duración de un robo en ella, escogiendo un randint en el rango especificado en `mapa.txt` para dicha casa.

* El total de autos iniciales en la ciudad será un randint entre un cuarto y la mitad del total de calles. Mientras que el total de taxis iniciales será igual a un randint entre 1 y la mitad del total de calles menos los autos iniciales.

* Luego de rellenar la grilla con las calles, casas y autos iniciales, se pide ingresar el tiempo intervalo para la actualizacion de la grilla.

* Simulé que también los autos pueden ir por una calle y meterse a una casa o servicio adyacente, es decir, a veces los vehiculos "desaparecen" de la grilla pero es porque se simula esta entrada a casas o servicios.

* Para la simulación, al inicializarla se carga una 'línea de tiempo' de todos los eventos que sucederán en el tiempo de simulación ingresado.

* Todas las unidades de tiempos en el programa están en segundos.



