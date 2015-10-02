### Distribución de puntajes

Requerimientos (**R**):

* **(3.0 pts)** R1: Se manejan todos los errores que generan la falla del sistema
* **(3.0 pts)** R2: Se notifica qué no se pudo hacer y la razón del error

**Se descontará (1.5) puntos por cada error que no se maneje (0.75 por no manejo y 0.75 por no notificación del error).**

### Obtenido por el alumno
| R1 | R2 | R3 | R4 | R5 | R6 | Descuento |
|:---|:---|:---|:---|:---|:---|:----------|
| 3 | 2.8 | 0 | 0 | 0 | 0 | 0 |

| Nota |
|:-----|
| **6.8** |

### Comentarios
Muy buena actividad! te recomiendo usar el método .__name__ para obtener el nombre de la excepción en vez de escribirla a mano, mira:

except Exception as err:
    print("[ERROR]", type(err).__name__)

En la parte b no pusiste expresamente en pocos casos que no se pudo realizar aunque se puede sacar por deducción.. lamentablemente el enunciado pedía expresamente (por eso te bajé casi nada).

saludos!

