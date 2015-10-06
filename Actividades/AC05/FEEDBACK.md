### Distribución de puntajes

Requerimientos (**R**):

* **(1.50 pts)** R1: Clase `Commit` y `Branch` correctas.
* **(1.50 pts)** R2: Método `pull` correcto.
* **(1.00 pts)** R3: Método `create_branch` correcto.
* **(2.0 pts)** R4: Método `checkout`.

**Además, se descontará (0.2) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | R4 | Descuento |
|:---|:---|:---|:---|:----------|
| 1.5  | 1.0  | 0.5  | 1.0  | 0         |

| Nota |
|:-----|
| **5.0** |

### Comentarios

* En ``pull`` agregaste las tuplas (``("ACCION", "arhivo"``) a lista que querías retornar (-1.0). Tenías que eliminar, o agregar, el archivo según lo que te indicaba el primer elemento de la tupla.
* ``create_branch`` debería utilizar from_branch_name al momento de crear el nuevo branch (-0.5).
* ``checkout`` debería retornar los archivos al igual que ``pull``.
* Te recomiendo mirar el material de [**Árboles**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/02_EDD/06-arboles.html) antes de revisar la solución de esta actividad.

