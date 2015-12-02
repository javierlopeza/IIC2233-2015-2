## Tarea 07

### Consideraciones

* Al iniciar el programa, se carga el arbol completo de archivos del Dropbox del usuario.

* Al subir un archivo, se debe seleccionar algun archivo o carpeta del directorio donde se quiere subir el archivo. Por ejemplo, si quiero subir el archivo ````mifoto.jpg```` y selecciono la carpeta ````carpeta1```` de mi Dropbox, entonces ````mifoto.jpg```` se subirá a la misma carpeta que contiene a la ````carpeta1````, NO se subirá a la ````carpeta1````. De igual forma, si quiero subir el archivo ````mifoto.jpg```` y selecciono el archivo ````archivo1.asd````, entonces ````mifoto.jpg```` se subirá a la misma carpeta que contiene a ````archivo1.asd````. Es decir, se debe posicionar en el archivo o carpeta del arbol de archivos que indica el directorio donde se quiere subir el archivo.

* La consideración anterior funciona de igual forma para la creación de carpetas, mover carpetas y mover archivos.

* Al subir un archivo, mover de un directorio a otro o renombrar, se actualiza todo el arbol de archivos. De esta forma se aprovecha de actualizar posibles cambios que se hayan hecho externamente durante la sesión, dejando al usuario su arbol de archivos verdadero.

* Al descargar una carpeta, no se permite descargarla en una ubicacion donde existe una carpeta con el mismo nombre.