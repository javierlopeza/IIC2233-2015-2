# [Tarea 4]

## Overview
----------


### Puntaje
| Item | Puntaje |
|:--------|:--------|
| Parte I: sin `simpy` | 2.4 |
| Parte II: con `simpy` | 0 |
| Estad�sticas e informe | 1.6 |

| Nota |
|:-----|
| **5.0** |

### Comentarios Generales
En general los eventos y el tiempo en que ocurren se encuentran bien modelados.
Aunque la parte con simpy no se encuentra implementada.

Lo que si la simulación toma mucho tiempo.

## Desglose Puntaje
----------

#### Parte I: sin `simpy` **(2.8 pts)**

* **(0.3 pts)** Item 1: Variables de estado
* **(0.4 pts)** Item 2: Detecci�n de eventos
* **(1.0 pts)** Item 3: Tr�fico
* **(0.7 pts)** Item 4: Secuencia de eventos
* **(0.4 pts)** Item 5: Reloj global

| Item | Puntaje | Comentarios |
|:--------|:--------|:--------|
| 1 | 0.3 | - |
| 2 | 0.4 | Utiliza bien la distribución pedida para cada evento |
| 3 | 0.6 | En los autos de emergencia, no se deberian detener todos los otros autos.
 La corrección del tráfico la hice principalmente mirando tu codigo ya que en la simulación.
 En la simulación, los autos como que se mueven bien al inicio hasta que llegan a un estado en que no cambia mucho.
 No se ven en la simulación los autos de emergencia. Como que el semáforo no genera diferencia. |
| 4 | 0.7 | - |
| 5 | 0.4 | - |


#### Parte II: con `simpy` **(1.2 pts)**

* **(0.1 pts)** Item 1: Variables de estado
* **(0.2 pts)** Item 2: Detecci�n de eventos
* **(0.5 pts)** Item 3: Tr�fico
* **(0.3 pts)** Item 4: Secuencia de eventos
* **(0.1 pts)** Item 5: Reloj global

| Item | Puntaje | Comentarios |
|:--------|:--------|:--------|
| 1 | 0 | - |
| 2 | 0 | - |
| 3 | 0 | - |
| 4 | 0 | - |
| 5 | 0 | - |


#### Estad�sticas e informe **(2.0 pts)**

* **(1.0 pts)** Item 1: Posiciones �ptimas
* **(1.0 pts)** Item 2: Reporte

| Item | Puntaje | Comentarios |
|:--------|:--------|:--------|
| 1 | 1.0 | Se calcula bien buscando el minimo |
| 2 | 0.6 | Se generan los archivos pero no contienen todos los estados, 
    falta decir las otras entidades involucradas |
