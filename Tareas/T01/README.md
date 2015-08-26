## Tarea 01

Consideraciones al revisar:

**1.** Considerar que la parte del código referente a la lectura y manejo de los archivos de texto es bastante tediosa debido a la restricción de solo usar lo conocido en el curso introductorio y lo que llevamos del presente curso. Además de lo mencionado por un ayudante en una issue, que los archivos con las propiedades de las personas, cursos, etc. pueden tener las propiedades en desorden.

**2.** En el archivo *cursos.txt* algunos cursos tienen sus datos en distinto orden a los de otros cursos, por dicha razón la parte del código correspondiente a la lectura de este archivo es un poco tediosa. Lo mismo ocurre para el caso del archivo *personas.txt*.

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

**3.** El control de tope de horario en Bummer se realiza solo para CAT-CAT, LAB-LAB, CAT-LAB.

**4.** Al ingresar a Bummer, se presenta un menu principal que permite iniciar sesión, buscar cursos o salir del sistema.
<br>  - Al seleccionar la opción de iniciar sesión, el sistema pregunta al usuario si desea ingresar con credenciales de profesor o alumno, por lo que la lista de personas que revisa sus credenciales (profesores o alumnos) depende de la elección realizada en ese momento. 
<br>  - Para la opción de *buscar cursos* del menu principal del sistema, se debe ingresar la sigla del curso que se quiere obtener la informacion. Luego de entregar los resultados se le pregunta al usuario si quiere saber la totalidad de la informacion respecto a los cursos.

**5.** Al ingresar con credenciales válidas de alumno, el sistema desplega el menu de alumno que permite inscribir un curso, botar un curso, generar un horario en consola y en un archivo *"horario.txt"*, generar un calendario de las evaluaciones en consola y en un archivo *"evaluaciones.txt"*,
mostrar los permisos especiales que tiene el alumno,
mostrar la información personal del alumno y cerrar sesión.
<br>  - Para la opción de inscribir un curso, el alumno ingresa
el NRC del curso que desea inscribir y si el sistema permite la inscripción, 
se le informa al alumno
en consola que el curso fue inscrito exitosamente.
Si existe algún error de inscripción se le informa el tipo de error al alumno en consola, en
específico para el tope de horario se le muestra al alumno el tope de horario en un horario impreso en consola.
<br>  - Para la opción de botar curso, el alumno ingresa el NRC del curso que desea botar, mostrando en consola el exito de botar el ramo.
<br>  - Para la opcion de generar horario, se muestra en consola un horario de forma amigable con los cursos que tiene inscritos hasta el momento,
además se crea en el directorio principal de *main.py* un archivo llamado *"horario.txt"* con el mismo horario 
impreso en consola.
<br>  - Para la opcion de generar calendario, se imprime en consola las evaluaciones de todos los ramos tomados hasta el momento, 
guardando además en un archivo *"evaluaciones.txt"* en el directorio principal de *main.py* que contiene las evaluaciones impresas en consola.
<br>  - Para la opcion de mostrar datos personales, se imprime en consola el Nombre, Usuario, Clave, Horario de Inscripcion, Maximo de Creditos Permitidos, Cursos por Tomar, Cursos Aprobados, Lista de Idolos.
<br>  - Para la opción de cerrar sesión, se vuelve al menu principal de Bummer.

**6.** Al ingresar con credenciales válidas de profesor, el sistema desplega el menu de profesor que permite dar permisos especiales, quitar permisos especiales o cerrar sesión.
<br>  - Para la opción de dar permiso especial, se le pide al profesor que ingrese el NRC del curso que quiere otorgar el permiso especial y el usuario del alumno al que quiere darselo, 
si el profesor dicta el ramo entonces se le da el permiso especial al alumno mostrando el exito en consola. Si existe algun error, que por ejemplo el profesor no dicta el ramo, se muestra en pantalla informando al profesor el tipo de error correspondiente.
<br>  - Para la opción de quitar permiso especial, se le pide al profesor que ingrese el NRC del curso que quiere quitar el permiso especial y el usuario del alumno al que quiere quitarselo, 
si el profesor dicta el ramo entonces se le quita el permiso especial al alumno mostrando el exito en consola. Si existe algun error, que por ejemplo el profesor no dicta el ramo, se muestra en pantalla informando al profesor el tipo de error correspondiente.
<br>  - Para la opción de cerrar sesión, se vuelve al menu principal de Bummer.