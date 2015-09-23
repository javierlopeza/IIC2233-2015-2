## Tarea 03

REVISAR CUAL VEHICULO TIENE EL ATAQUE PARALIZADOR.

LOS VEHICULOS AEREOS TAMBIEN SE PUEDEN MOVER (?)

### Consideraciones
1. Los vehiculos mantendran para siempre su orientación impuesta inicialmente. Es decir, al moverse 
entre las casillas del mapa estarán orientados siempre en la misma dirección.

2. Para mover un vehículo de dimensiones, por ejemplo, de 2x3, este tendrá un atributo
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
BuqueDeGuerra().mover(2,1)
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