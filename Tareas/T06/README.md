## Tarea 06

### Ahora

* Observar carpeta.


### Pendiente

* Observar carpeta.

* Permitir eliminar archivos y carpetas.

* Fix tiempo carga de archivos y carpetas.


### Completado

* Servidor y clientes implementados independientemente.

* Creacion de usuarios unicos. Con HASH + SALT para las claves.

* Log In usuarios.

* Chat instantáneo, con emojis.

* Cargar historial chat.

* Cargar arbol de archivos en el sistema.

* Cargar lista de amigos.

* Subir archivos.

* Subir carpetas.

* Bajar archivos.

* Bajar carpetas.

* Envío de archivos a amigos.


### Consideraciones

* Se recomienda tratar con cuidado la interfaz para evitar que se caiga o pegue :pray::

	* Esperar unos segundos entre cada acción a realizar :clock2:.

	* No hacer clicks seguidos en los botones, con un click y paciencia basta :relieved:.

	* **ARREGLAR:** Al subir carpetas pareciera que se queda pegado pero es solo momentaneo, luego de unos segundos se actualiza bien :+1:.

	* No se recomienda subir archivos tan pesados, es DrobPox no DropBox :disappointed:.

* El boton Actualizar Todo, actualiza la lista de amigos y los archivos mostrados.

* Cuando yo agrego un usuario a mi lista de amigos, automaticamente queda registrado en mi lista de amigos. De la misma forma, yo soy agregado automaticamente a su lista de amigos.

* Para iniciar el chat con otro usuario, se debe seleccionar el usuario de la lista de amigos y hacer click en Conversar. Al iniciar el chat se carga el historial de conversaciones automaticamente.

* No es necesario que el amigo este online para chatear. Si le envio mensajes cuando esta offline, podra verlos la proxima vez que se conecte.

* Cuando el usuario "sube un archivo" este se guarda en el directorio principal de su DrobPox.

* Cuando el usuario "sube una carpeta" esta se guarda en el directorio principal de su DrobPox.

* **ARREGLAR:** La subida de archivos y carpetas demora un poco, pero resulta. Incluso a veces puede quedar unos segundos en "No Responde", pero un par de segundos despues la carga se efectua sin problemas.

* Si se sube una carpeta o un archivo que ya se encontraba en el directorio principal, se reemplaza completamente.

* Si se quiere bajar un archivo, se debe seleccionar uno del arbol en la interfaz y hacer click en el boton Bajar Archivo, el programa no permitira bajar una carpeta con este boton. Funciona de manera analoga para la descarga de carpetas.

* Para enviar un archivo a un amigo, este se debe encontrar en linea, ya que debe aceptar (o rechazar) la notificacion que le pregunta por el envio. En caso de aceptar el envio, debe seleccionar en que lugar de su computador se guardara el archivo. Solo se permitira el envio de archivos, no de carpetas (no se pasa por encima de ningun aspecto del enunciado).
 
* Al recibir un archivo enviado por un amigo, este se guarda con el nombre original en el destino elegido.

* Una carpeta es observada solamente durante el tiempo que el usuario se encuentre en linea. Es decir, si el usuario sube una carpeta, realiza cambios en ella y luego hace click en Actualizar Todo, efectivamente esa carpeta se actualizara en el servidor. De igual forma, si el usuario descarga una carpeta, realiza cambios en ella y luego hace click en Actualizar Todo, esa carpeta se actualizara en el servidor.

* Cuando se observa una carpeta, se debe hacer click en Actualizar Todo para subir los cambios al servidor. Luego para descargar los cambios de la carpeta en otro computador se debe clickear Descargar Carpeta seleccionando la carpeta correspondiente.




