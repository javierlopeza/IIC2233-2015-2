## Tarea 01 - Pacmatico

Consideraciones al revisar:

**1.** Considerar que la parte del código referente a la lectura y manejo de los archivos de texto es bastante tediosa debido a la restricción de solo usar lo conocido en el curso introductorio y lo que llevamos del presente curso. Además de lo mencionado por un ayudante en una issue, que los archivos con las propiedades de las personas, cursos, etc. pueden tener las propiedades en desorden.

**2.** En el archivo *cursos.txt* algunos cursos tienen sus datos en distinto orden a los de otros cursos, por dicha razón la parte del código correspondiente a la lectura de este archivo es un poco tediosa. Lo mismo ocurre para el caso del archivo *personas.txt*.

Ejemplo de desorden de datos de cursos:
```
# CURSO 1
  {
    "disp": 77,
    "eng": "NO",
    "apr": "NO",
    "curso": "Álgebra Lineal",
     ...
    "sala_ayud": "M1",
    "campus": "San Joaquin",
    "retiro": "SI",
    "NRC": 14268,
    "profesor": [
      "Huerta Ivan",
      "Becerra Carolina"
    ]
  }
# CURSO 2
  {
    "ofr": 79,
    "ocu": 0,
    "hora_lab": "L:4,5",
    "cred": 0,
     ....
    "curso": "Laboratorio de Electricidad y Magnetismo",
    "sala_lab": "(Por Asignar)",
    "NRC": 16312,
    "profesor": "During Gustavo"
  } 
```

**3.** A diferencia de Bummer UC, el Pacmatico la unica restriccion que pone al pedir cursos es que el alumno cumpla con los prerrequisitos del curso o tenga un permiso especial del profesor.
Si el alumno presenta topes de horario, evaluaciones, campus, creditos maximos, el Pacmatico lo deja pedir el curso igual.

**4.** Al ingresar al Pacmatico, se presenta un menu principal que permite **iniciar sesión**, **buscar cursos**, **dar cursos**, **cargar bacanosidad** o **salir del sistema**.
<br>  - Al seleccionar la opción de **iniciar sesión**, el sistema pregunta al usuario si desea ingresar con credenciales de profesor o alumno, por lo que la lista de personas que revisa sus credenciales (profesores o alumnos) depende de la elección realizada en ese momento. 
<br>  - Para la opción de **buscar cursos** del menu principal del sistema, se debe ingresar la sigla del curso que se quiere obtener la informacion. Luego de entregar los resultados de todas las secciones, se le pregunta al usuario si quiere saber la totalidad de la informacion respecto a los cursos, a lo que debe responder *si* o *no*.
<br>  - Para la opcion de **dar cursos** el sistema opera de forma que segun los cursos que pidieron los alumnos se aceptan o deniegan dichas solicitudes maximizando los puntos efectivos totales.
Esto se hace a traves de aceptar a los que hicieron mayores apuestas en los cursos hasta que estos no tengan mas vacantes disponibles.

**5.** Al ingresar con credenciales válidas de alumno, el sistema desplega el menu de alumno que permite **inscribir un curso**, **pedir cursos**, **mostrar carga academica obtenida**,**generar un horario en consola y en un archivo** "horario.txt"**, **generar un calendario de las evaluaciones en consola y en un archivo "evaluaciones.txt"**,
**mostrar los permisos especiales que tiene el alumno**,
**mostrar la información personal del alumno** y **cerrar sesión**.
<br>  - Cuando el alumno **pide un curso** debe ingresar el NRC del curso a pedir, luego, si cumple los prerrequisitos del curso o tiene permiso especial del profesor, el curso se agrega al atributo *cursos_pedidos* del alumno.
Luego para redistribuir los puntos del alumno en los cursos pedidos, se carga un menu con los cursos pedidos hasta el momento. Aqui se debe seleccionar la opcion correspondiente al curso que se le quiere cambiar la apuesta y luego ingresar cuanto se le quiere sumar o restar a dicha apuesta. 
Se actualizan las demas apuestas automaticamente luego de ingresar esta. Cuando el alumno ya ha redistribuido mas de 1000 puntos o ya ha redistribuido apuestas a 45 creditos, debe continuar ingresando la opcion '0' para registrar en el sistema sus apuestas.
<br>  - Para la opción de **mostrar carga academica obtendia** se muestran los cursos que el Pacmatico le dio luego de realizar la entrega de vacantes. Si todavia esta no se ha realizado le indica al usuario que debe ir al menu principal para ejecutarla.
<br>  - Para la opcion de **generar horario**, se muestra en consola un horario de forma amigable con los cursos que le dio el Pacmatico,
además se crea en el directorio principal de *main.py* un archivo llamado *"horario.txt"* con el mismo horario 
impreso en consola.
<br>  - Para la opcion de **generar calendario**, se imprime en consola las evaluaciones de todos los ramos que le dio el Pacmatico, 
guardando además en un archivo *"evaluaciones.txt"* en el directorio principal de *main.py* que contiene las evaluaciones impresas en consola.
<br>  - Para la opcion de **revisar permisos especiales** se muestran los permisos especiales que los profesores le han dado al alumno.
<br>  - Para la opcion de **mostrar datos personales**, se imprime en consola el Nombre, Usuario, Clave, Maximo de Creditos Permitidos, Cursos por Tomar, Cursos Aprobados, Lista de Idolos.
<br>  - Para la opción de **cerrar sesión**, se vuelve al menu principal de Pacmatico.

**6.** Al ingresar con credenciales válidas de profesor, el sistema desplega el menu de profesor que permite **dar permisos especiales**, **quitar permisos especiales** o **cerrar sesión**.
<br>  - Para la opción de **dar permiso especial**, se le pide al profesor que ingrese el usuario del alumno al que quiere darselo y el NRC del curso que quiere otorgar el permiso especial. 
si el profesor dicta el ramo entonces se le da el permiso especial al alumno mostrando el exito en consola. Si existe algun error, que por ejemplo el profesor no dicta el ramo, se muestra en pantalla informando al profesor el tipo de error correspondiente.
<br>  - Para la opción de **quitar permiso especial**, se le pide al profesor que ingrese el usuario del alumno al que quiere quitarselo y el NRC del curso que quiere quitar el permiso especial, 
si el profesor dicta el ramo entonces se le quita el permiso especial al alumno mostrando el exito en consola. Si existe algun error, que por ejemplo el profesor no dicta el ramo, se muestra en pantalla informando al profesor el tipo de error correspondiente.
<br>  - Para la opción de **cerrar sesión**, se vuelve al menu principal de Pacmatico.

**7.** Para calcular las bacanosidades de los alumnos, lo que hace el programa es darle un punto por cada 
seguidor que tiene el alumno. Esta decisión de hacerlo así se debe a que probe haciendo que la cantidad de seguidores de los seguidores del alumno se sumaran a la bacanosidad del alumno pero aun ponderando dicha cantidad me encontre con que cada vez que aumentaba la ponderacion más me alejaba de cumplir la verificación del algoritmo que se menciona en *bacanosidad.pdf*.
Es por esto que el algoritmo de: *"asignar un punto de bacanosidad al alumno por cada persona que lo considera ídolo"* calculé que me entrega una eficiencia promedio de un 92.71% respecto a la eficiencia del algoritmo perfecto (*el cual hace que los bacanosipuntos de un alumno equivalen a los puntos recibidos en un 100%*). 
Ejemplificando: *si Juan tiene 100 bacanosipuntos asignados por mi algoritmo, al hacer la verificación de repartición de puntos, me encuentro con que Juan recibe 92,72 puntos (o 107,28)*. Es lo más eficiente que logré hacer el algoritmo, teniendo en cuenta que puede estar afectado en poca parte por cómo Python trabaja los decimales de los *float*.
En el archivo *cargar_bacanosipuntos.py* esta 
el codigo que calcula el porcentaje de eficiencia mencionada anteriormente.
<br>**PD:** Para ordenar el ranking de alumnos por bacanosidad uso la bacanosidad relativa calculada con los puntos recibidos relativos en cuanto al con mayor puntos recibidos, ya que esta permite mayor diferenciacion de los alumnos en cuanto a decimales.

**8.** Para cargar las bacanosidades a los alumnos del programa hay dos opciones, la primera es elegir la opcion del *menu principal* que carga las bacanosidades de los alumnos con el algoritmo creado,
 lo cual demora unos minutos (aproximadamente 3 a 4 minutos). La segunda opcion es que al haber realizado previamente la primera opcion se guarda un archivo llamado *bacanosidades.txt* el cual al iniciar el programa se carga si es que existe dicho archivo, de lo contrario
 hay que ejecutar la opcion del menu mencionada para crearlo.

**9.** Para la generacion del horario del alumno, tomé en cuenta que pueden haber cursos cuyas siglas no tengan una longitud comun (llamese longitud comun a *MAT1620* que mide 7, longitud no comun es *FIL188* que mide 6) asi como tambien las secciones que tienen mas de dos digitos (seccion 12 de Algebra Lineal).
Por lo tanto hice buenos arreglos para que el horario de ninguna forma, ninguna sigla ni numero de seccion, arruine la bonita forma que queda al imprimirlo.

**10.** Para el caso en que un alumno ingresa e inscribe menos de 30 creditos, al cerrar su sesión le aparecerá una advertencia de que *no cumple con esa restricción*, aunque igual se le permitirá salir del sistema diciendole que vuelva a ingresar para inscribir mas creditos.