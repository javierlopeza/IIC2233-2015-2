### Distribución de puntajes

Requerimientos (**R**):

* **(2.0 pts)** R1: Sonda 4D 
* **(2.0 pts)** R2: Traidores
* **(2.0 pts)** R3: Pizzas

**Además, se descontará (0.2) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | Descuento |
|:---|:---|:---|:----------|
| 1.0 | 1.0 | 2.0 | 0 |

| Nota |
|:-----|
| **5.0** |

### Comentarios

* En **R1** la idea era usar un diccionario, que es ideal para los casos en que tienes que asociar un valor a una clave. La lista es menos eficiente para ellos (-1).
* En **R2** tenías que usar dos ``set`` y encontrar la intersección (-1). Los sets son ideales en estos casos en que te interesa el conjunto en sí y no manipular los componentes:
```python
    bufalos = set()
    rivales = set()
    # Rellenar...
    traidores = bufalos & rivales
    # O también
    traidores = bufalos.intersection(rivales)
```
