## Tarea 01

Consideraciones al revisar:

* **01.** Considerar que la parte del código referente a la lectura y manejo de los archivos de texto es bastante tediosa debido a la restricción de solo usar lo conocido en el curso introductorio y lo que llevamos del presente curso. Además de lo mencionado por un ayudante en una issue, que los archivos con las propiedades de las personas, cursos, etc. pueden tener las propiedades en desorden.

* **02.** En el archivo *cursos.txt* algunos cursos tienen sus datos en distinto orden a los de otros cursos, por dicha razón la parte del código correspondiente a la lectura de este archivo es un poco tediosa. Lo mismo ocurre para el caso del archivo *personas.txt*.

Ejemplo de desorden de datos de cursos:
```
#CURSO 1
  {
    "disp": 77,
    "eng": "NO",
    "apr": "NO",
    "curso": "Álgebra Lineal",
    "sala_lab": "(Por Asignar)",
    "hora_cat": "L-W-V:3",
    "sala_cat": "CS-101",
    "hora_ayud": "W:6",
    "ofr": 77,
    "ocu": 0,
    "hora_lab": "W:5",
    "cred": 10,
    "sec": 1,
    "sigla": "MAT1203",
    "sala_ayud": "M1",
    "campus": "San Joaquin",
    "retiro": "SI",
    "NRC": 14268,
    "profesor": [
      "Huerta Ivan",
      "Becerra Carolina"
    ]
  }
#CURSO 2
  {
    "ofr": 79,
    "ocu": 0,
    "hora_lab": "L:4,5",
    "cred": 0,
    "sec": 1,
    "disp": 79,
    "retiro": "SI",
    "sigla": "FIS0153",
    "eng": "NO",
    "apr": "NO",
    "campus": "San Joaquin",
    "curso": "Laboratorio de Electricidad y Magnetismo",
    "sala_lab": "(Por Asignar)",
    "NRC": 16312,
    "profesor": "During Gustavo"
  } 
```

* **03.** El control de tope de horario en Bummer se realiza solo para CAT-CAT, LAB-LAB, CAT-LAB.

* **04.** Al ingresar a Bummer, se presenta un menu principal que permite iniciar sesión, buscar cursos o salir del sistema.
<br>Al seleccionar la opción de iniciar sesión, el sistema pregunta al usuario si desea ingresar con credenciales de profesor o alumno, por lo que la lista de personas que revisa sus credenciales (profesores o alumnos) depende de la elección realizada en ese momento. 
<br>Para la opción de *buscar cursos* del menu principal del sistema, se debe ingresar la sigla del curso que se quiere obtener la informacion. Luego de entregar los resultados se le pregunta al usuario si quiere saber la totalidad de la informacion respecto a los cursos.