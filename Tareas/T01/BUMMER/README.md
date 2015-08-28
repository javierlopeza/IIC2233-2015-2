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

**7.** Para calcular las bacanosidades de los alumnos, lo que hace el programa es darle un punto por cada 
seguidor que tiene el alumno. Esta decisión de hacerlo así se debe a que probe haciendo que la cantidad de seguidores de los seguidores del alumno se sumaran a la bacanosidad del alumno pero aun ponderando dicha cantidad me encontre con que cada vez que aumentaba la ponderacion más me alejaba de cumplir la verificación del algoritmo que se menciona en *bacanosidad.pdf*.
Es por esto que el algoritmo de: *"asignar un punto de bacanosidad al alumno por cada persona que lo considera ídolo"* calculé que me entrega una eficiencia promedio de un 92.71% respecto a la eficiencia del algoritmo perfecto (*el cual hace que los bacanosipuntos de un alumno equivalen a los puntos recibidos en un 100%*). 
Ejemplificando: *si Juan tiene 100 bacanosipuntos asignados por mi algoritmo, al hacer la verificación de repartición de puntos, me encuentro con que Juan recibe 92,72 puntos (o 107,28)*. Es lo más eficiente que logré hacer el algoritmo, teniendo en cuenta que puede estar afectado en poca parte por cómo Python trabaja los decimales de los *float*.
En el archivo *cargar_bacanosipuntos.py* esta 
el codigo que calcula el porcentaje de eficiencia mencionada anteriormente.
**PD:** Para ordenar el ranking de alumnos por bacanosidad uso la bacanosidad relativa calculada con los puntos recibidos relativos en cuanto al con mayor puntos recibidos, ya que esta permite mayor diferencia en cuanto a decimales.

**8.** Para cargar las bacanosidades a los alumnos del programa hay dos opciones, la primera es elegir la opcion del menu que carga las bacanosidades de los alumnos con el algoritmo creado,
 lo cual demora unos minutos (aproximadamente 3 minutos). La segunda opcion es que al haber realizado previamente la primera opcion se guarda un archivo llamado *bacanosidades_bummer.txt* el cual al iniciar el programa se carga si es que existe dicho archivo, de lo contrario
 hay que ejecutar la opcion del menu mencionada. 

**9.** Como en el enunciado dice que cada grupo de Bummer tiene máximo 435 alumnos, lo que hice fue llenar todos los grupos que se puedan con 435 partiendo del grupo 1 y el grupo 10 quedará con los alumnos que resten.

**10.** Para el caso en que un alumno ingresa e inscribe menos de 30 creditos, al cerrar su sesión le aparecerá una advertencia de que no cumple con esa restricción, aunque igual se le permitirá salir del sistema diciendole que vuelva a ingresar para inscribir mas creditos.