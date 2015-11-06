## Tarea 04

### Consideraciones

* Al agregar una casa se fija el tiempo de duración de un robo en ella, escogiendo un randint en el rango especificado en `mapa.txt` para dicha casa.

* El total de autos iniciales en la ciudad será un randint entre un cuarto y la mitad del total de calles. El total de autos comunes iniciales sera el 80% de autos iniciales, mientras que el total de taxis iniciales será igual al 20% de dichos autos iniciales.

* Luego de rellenar la grilla con las calles, casas y autos iniciales, se pide ingresar el tiempo intervalo para la actualizacion de la grilla.

* Simulé que también los autos pueden ir por una calle y meterse a una casa o servicio adyacente, es decir, a veces los vehiculos "desaparecen" de la grilla pero es porque se simula esta entrada a casas o servicios. En el caso de cuando lo vehiculos desaparecen, simule que entran a la ciudad (por alguna de las entradas aleatorias) un randint de entre 0 y 2 autos nuevos, sin sobrepasar el limite establecido en el enunciado.

* [PROBLEMA] Luego de las actualizaciones de las `gui` tuve un problema para mostrar la actualizacion de la interfaz. Al principio los vehiculos se movian bien por la ciudad, pero luego de los cambios hechos la interfaz parece congelada o actualizandose con fallas. Es por esto que pido por favor revisar en detalle las funciones que internamente mueven los vehiculos, más que las actualizaciones de la interfaz.

* Para cada simulación, al inicializarla se carga una *línea de tiempo* de todos los eventos que sucederán en el tiempo de simulación ingresado. Luego la simulacion mueve los vehiculos durante un tiempo *delta* segundos hasta el proximo evento en la linea de tiempo, en ese instante ocurre el evento y sus consecuencias respectivas.

* Como se mencionó en la issue #345 cada bloque es una pista, es decir, cada bloque de la interfaz puede contener solamente 1 auto.

* Todas las unidades de tiempos en el programa están en segundos.

* Las simulaciones de los lugares e instantes en que ocurren robos, incendios y enfermos funcionan correctamente.

* Para una emergencia, supuse que todos los autos dejan se detienen y dejan pasar al vehiculo de emergencia. En el caso de que el vehiculo de emergencia no tenga una ruta disponible para llegar a la emergencia (debido al sentido de las calles), modele la simulacion como que en este caso el vehiculo de emergencia toma las calles contra el transito para llegar rapidamente a la emergencia (supuse que seria lo mas real)

* Para decidir cual era el mejor posicionamiento, decidi que la estacion de policia tiene prioridad en cuanto a posicionarse, ya que los robos estan directamente relacionados con la distancia a la comisaria. Por lo tanto se prioriza que los robos frustrados sean maximos y los robos escapados sean minimos, en primer lugar.
Luego, el hospital y los bomberos tienen igual prioridad, es decir, su posicion ideal se definira por la minimizacion de sus dos tiempos promedios sumados.