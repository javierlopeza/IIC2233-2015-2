## Tarea 01

Consideraciones al revisar:

* **01.** El archivo *personas.txt* debe tener el mismo formato que el entregado junto al enunciado, es decir, sin cambiar el orden de los datos de las personas, así:
```
    "idolos"
    "nombre"
    "clave"
    "ramos_pre"
    "alumno"
    "usuario"
```

* **02.** En el archivo *cursos.txt* algunos cursos tienen sus datos en distinto orden a los de otros cursos, por dicha razón la parte del código correspondiente a la lectura de este archivo es un poco tediosa.

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
