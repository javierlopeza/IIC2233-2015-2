## Tarea 06


### Ejemplo Interfaz Funcionando

En la imagen *ejemplo_interfaz.jpg* que se encuentra en la carpeta ````T06```` se puede ver un ejemplo del programa funcionando. La imagen fue tomada cuando todas las funcionalidades mostradas estaban implementadas.


### Estructura de Archivos

* Para que el Cliente corra bien en un computador, se deben tener todos los archivos de la carpeta Cliente. Para correr el Cliente se debe ejecutar ````mainCliente.py````.

* Para que el Servidor corra bien en un computador, se deben tener todos los archivos de la carpeta Servidor. Para correr el Servidor se debe ejecutar ````mainServidor.py````.


### HOST & PORT

En los programas ````mainCliente.py```` y ````mainServidor.py```` se ven a primera vista las variables ````HOST```` y ````PORT```` que hay que cambiar.


### Completado

* Servidor y clientes implementados independientemente.

* Creacion de usuarios unicos. Con HASH + SALT para las claves.

* Log In usuarios.

* Agregar amigos.

* Chat instantáneo, con emojis.

* Cargar historial chat.

* Cargar arbol de archivos en el sistema.

* Cargar lista de amigos.

* Subir archivos.

* Subir carpetas.

* Bajar archivos.

* Bajar carpetas.

* Envío de archivos a amigos.

* Observar carpetas recientemente subidas y bajadas.

* Historial de modificaciones de carpetas y archivos observados.

* Eliminar archivos y carpetas (**bonus**).

* Renombrar archivos y carpetas (**bonus**).


### Consideraciones

* Se recomienda tratar con cuidado la interfaz para evitar que se caiga o pegue :pray::

	* Esperar unos segundos entre cada acción a realizar :clock2:.

	* No hacer clicks seguidos en los botones, con un click y paciencia basta :relieved:.

	* Al subir carpetas pareciera que se queda pegado pero es solo momentaneo, luego de unos segundos se actualiza bien :+1:.

	* No se recomienda subir archivos taaan pesados, es DrobPox no DropBox :disappointed:. Canciones, fotos y archivos de esa magnitud no hay problemas. Pero subir películas puede costarle la vida al programa.
	
	* La mayoría de la interfaz se actualiza automáticamente (lista de amigos, arbol de archivos, etc.) de no actualizarse, por favor hacer click en Actualizar Todo. En el peor de los casos vaciar la carpeta ````database```` y volver a iniciar el servidor.

* El boton Actualizar Todo, actualiza la lista de amigos y los archivos mostrados. Funciona algo lento por todo lo que hace, pero paciencia que sí funciona.

* Cuando yo agrego un usuario a mi lista de amigos, automaticamente queda registrado en mi lista de amigos. De la misma forma, yo soy agregado automaticamente a su lista de amigos.

* Para iniciar el chat con otro usuario, se debe seleccionar el usuario de la lista de amigos y hacer click en Conversar. Al iniciar el chat se carga el historial de conversaciones automaticamente.

* No es necesario que el amigo este online para chatear. Si le envio mensajes cuando esta offline, podra verlos la proxima vez que se conecte.

* Cuando el usuario "sube un archivo" este se guarda en el directorio principal de su DrobPox.

* Cuando el usuario "sube una carpeta" esta se guarda en el directorio principal de su DrobPox.

* La subida de archivos y carpetas demora un poco, pero resulta. Incluso a veces puede quedar unos segundos en "No Responde", pero un par de segundos despues la carga se efectua sin problemas.

* Si se sube una carpeta o un archivo que ya se encontraba en el directorio principal, se reemplaza completamente.

* Si se quiere bajar un archivo, se debe seleccionar uno del arbol en la interfaz y hacer click en el boton Bajar Archivo, el programa no permitira bajar una carpeta con este boton. Funciona de manera analoga para la descarga de carpetas.

* Para enviar un archivo a un amigo, este se debe encontrar en linea, ya que debe aceptar (o rechazar) la notificacion que le pregunta por el envio. En caso de aceptar el envio, debe seleccionar en que lugar de su computador se guardara el archivo. Solo se permitira el envio de archivos, no de carpetas (no se pasa por encima de ningun aspecto del enunciado).
 
* Al recibir un archivo enviado por un amigo, este se guarda con el nombre original en el destino elegido.

* Una carpeta es observada solamente durante el tiempo que el usuario se encuentre en linea. Es decir, si el usuario sube una carpeta, realiza cambios en ella y luego hace click en Actualizar Todo, efectivamente esa carpeta se actualizara en el servidor. De igual forma, si el usuario descarga una carpeta, realiza cambios en ella y luego hace click en Actualizar Todo, esa carpeta se actualizara en el servidor.

* Cuando se observa una carpeta, se debe hacer click en Actualizar Todo para subir los cambios al servidor. Luego para descargar los cambios de la carpeta en otro computador se debe clickear Descargar Carpeta seleccionando la carpeta correspondiente.

* Para ver el Historial de Modificaciones de las carpetas observadas, se debe hacer click en Ver Historial.

* A la carpeta principal (main directory) la llamé ````__ROOT__````.

* **BONUS** Para borrar un archivo se debe seleccionar uno en el arbol de archivos y hacer click en el boton Borrar Archivo.

* **BONUS** Para borrar una carpeta se debe seleccionar una en el arbol de archivos y hacer click en el boton Borrar Carpeta.

* **BONUS** Para renombrar un archivo se debe seleccionar uno en el arbol de archivos y hacer click en el boton Renombrar Archivo, habiendo escrito el nuevo nombre del archivo en el campo inferior al boton (es importante haber escrito el nuevo nombre con la misma extensión del archivo de origen).

* **BONUS** Para renombrar una carpeta se debe seleccionar una en el arbol de archivos y hacer click en el boton Renombrar Carpeta, habiendo escrito el nuevo nombre de la carpeta en el campo inferior al boton.

