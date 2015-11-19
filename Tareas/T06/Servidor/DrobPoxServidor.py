# -*- coding: utf-8 -*-

import socket
import hashlib
from Servidor.cargar_database_usuarios import cargar_database_usuarios
from Servidor.cargar_database_amistades import cargar_database_amistades
from Servidor.cargar_database_chats import cargar_database_chats
from Servidor.cargar_database_archivos import cargar_database_archivos
from Servidor.cargar_database_arboles import cargar_database_arboles
from Servidor.cargar_database_historiales import cargar_database_historiales
from Servidor.hashear import hashear
from datetime import datetime
import threading
import json
import pickle
import select
import os
from time import sleep


class DrobPoxServidor:
    def __init__(self, host, port):
        # HOST y PORT
        self.host = host
        self.port = port

        # Base de datos de los usuarios, salts y claves hasheadas.
        self.cargar_database()

        # Configuracion Networking
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen(5)
        self.clientes_conectados = {}
        self.conexiones = []

        # Thread Aceptador
        thread_aceptador = threading.Thread(target=self.aceptar())
        thread_aceptador.setDaemon(True)
        thread_aceptador.start()

    def cargar_database(self):
        self.database_usuarios = cargar_database_usuarios()
        self.database_amistades = cargar_database_amistades()
        self.database_chats = cargar_database_chats()
        self.database_archivos = cargar_database_archivos()
        self.database_arboles = cargar_database_arboles()
        self.database_historiales = cargar_database_historiales()

    def aceptar(self):
        print("SERVIDOR ACTIVO...")
        while True:
            cliente_nuevo, address = self.socket_servidor.accept()
            self.conexiones.append(cliente_nuevo)
            thread_cliente = threading.Thread(target=self.recibir_data, args=(cliente_nuevo,))
            thread_cliente.daemon = True
            thread_cliente.start()

    def recibir_data(self, cliente):
        while cliente in self.conexiones:
            data = cliente.recv(1024)
            data_dec = data.decode('utf-8', errors="ignore")

            if data_dec.startswith("SUBIR_ARCHIVO"):
                # Recepcion archivos.
                data_str = ""
                meta = []  # [Usuario, Padre, Filename]
                largo_info_meta = 0
                for B in data:
                    data_str += chr(B)
                    if "SEPARADOR123456789ESPECIAL" in data_str:
                        info = data_str.split("SEPARADOR123456789ESPECIAL")[0]
                        meta.append(info)
                        data_str = ""
                    largo_info_meta += 1
                    if len(meta) == 4:
                        break

                usuario = meta[1]
                padre = meta[2]
                filename = meta[3]
                data = data[largo_info_meta:]

                data_contenido = b''
                while data:
                    data_contenido += data
                    ready = select.select([cliente], [], [], 0)
                    if (ready[0]):
                        data = cliente.recv(1024)
                    else:
                        data = b''

                if data_contenido:
                    self.agregar_archivo(usuario, padre, filename, data_contenido)

                if usuario in self.clientes_conectados.keys():
                    self.clientes_conectados[usuario].send("ARCHIVO_SUBIDO".encode('utf-8'))

            elif data_dec.startswith("SUBIR_CARPETA"):
                usuario = data_dec.split("SEPARADOR123456789ESPECIAL")[1]
                padre = data_dec.split("SEPARADOR123456789ESPECIAL")[2]
                foldername = data_dec.split("SEPARADOR123456789ESPECIAL")[3]
                self.agregar_carpeta(usuario, padre, foldername)
                if usuario in self.clientes_conectados.keys():
                    self.clientes_conectados[usuario].send("CARPETA_SUBIDA".encode('utf-8'))

            elif data_dec.startswith("BAJAR_ARCHIVO"):
                usuario = data_dec.split("SEPARADOR123456789ESPECIAL")[1]
                nombre_archivo = data_dec.split("SEPARADOR123456789ESPECIAL")[2]
                ruta_hijo = data_dec.split("SEPARADOR123456789ESPECIAL")[3]

                data_archivo = self.encontrar_archivo(usuario, nombre_archivo, ruta_hijo)

                if usuario in self.clientes_conectados.keys():
                    if data_archivo != "ERROR":
                        cliente.send(data_archivo)
                    else:
                        cliente.send("ERROR".encode("utf-8"))

            elif data_dec.startswith("BAJAR_CARPETA"):
                usuario = data_dec.split("SEPARADOR123456789ESPECIAL")[1]
                nombre_carpeta = data_dec.split("SEPARADOR123456789ESPECIAL")[2]
                ruta_llegar = data_dec.split("SEPARADOR123456789ESPECIAL")[3]
                ruta_llegar = ruta_llegar.split("\\")

                carpeta = self.encontrar_carpeta(usuario, nombre_carpeta, ruta_llegar)
                data_enviar_carpeta = self.enviar_carpeta(usuario, carpeta)

                cliente.send(data_enviar_carpeta)

            elif data_dec.startswith("ENVIAR_ARCHIVO"):
                usuario = data_dec.split("SEPARADOR123456789ESPECIAL")[1]
                amigo = data_dec.split("SEPARADOR123456789ESPECIAL")[2]
                nombre_archivo = data_dec.split("SEPARADOR123456789ESPECIAL")[3]
                ruta_hijo = data_dec.split("SEPARADOR123456789ESPECIAL")[4]

                if amigo not in self.clientes_conectados.keys():
                    cliente.send("ERROR...Tu amigo {} no se encuentra online.".format(amigo).encode('utf-8'))

                else:
                    data_archivo = self.encontrar_archivo(usuario, nombre_archivo, ruta_hijo)
                    if data_archivo == "ERROR":
                        cliente.send("ERROR...Recuerda que solo puedes enviar archivos a tus amigos"
                                     " , no carpetas.".encode('utf-8'))

                    else:
                        verificar_aceptacion = (("ARCHIVO_AMIGO1"
                                                 + "SEPARADOR123456789ESPECIAL"
                                                 + usuario
                                                 + "SEPARADOR123456789ESPECIAL"
                                                 + nombre_archivo
                                                 + "SEPARADOR123456789ESPECIAL").encode('utf-8')
                                                + data_archivo)

                        self.clientes_conectados[amigo].send(verificar_aceptacion)

                        cliente.send("TODO_OK".encode('utf-8'))

            elif data_dec.startswith("ELIMINAR_ARCHIVO"):
                usuario = data_dec.split("SEPARADOR123456789ESPECIAL")[1]
                nombre_archivo = data_dec.split("SEPARADOR123456789ESPECIAL")[2]
                ruta_hijo = data_dec.split("SEPARADOR123456789ESPECIAL")[3]

                data_archivo = self.eliminar_archivo(usuario, nombre_archivo, ruta_hijo)
                if data_archivo == "ERROR":
                    cliente.send("ERROR...Recuerda que solo puedes "
                                 "eliminar archivos con este boton.".encode('utf-8'))

                else:
                    tiempo = str(datetime.now()).split(".")[0]
                    padre = ruta_hijo
                    path_log = "__ROOT__" + "\\" + padre
                    log_historial = '{0} - REMOVED  "{1}" by {2}'.format(tiempo, path_log, usuario)

                    self.database_historiales[usuario].append(log_historial)
                    with open("database/database_historiales.txt", "w") as historiales:
                        json.dump(self.database_historiales, historiales)

                    cliente.send("TODO_OK".encode('utf-8'))

            elif data_dec.startswith("RENOMBRAR_ARCHIVO"):
                usuario = data_dec.split("SEPARADOR123456789ESPECIAL")[1]
                nombre_archivo = data_dec.split("SEPARADOR123456789ESPECIAL")[2]
                ruta_hijo = data_dec.split("SEPARADOR123456789ESPECIAL")[3]
                nuevo_nombre = data_dec.split("SEPARADOR123456789ESPECIAL")[4]

                data_archivo = self.renombrar_archivo(usuario, nombre_archivo, ruta_hijo, nuevo_nombre)
                if data_archivo == "ERROR":
                    cliente.send("ERROR...Recuerda que solo puedes "
                                 "renombrar archivos con este boton.".encode('utf-8'))

                else:
                    tiempo = str(datetime.now()).split(".")[0]
                    padre = ruta_hijo
                    path_log = "__ROOT__" + "\\" + padre
                    log_historial = '{0} - RENAMED  "{1}" to "{3}" by {2}'.format(tiempo,
                                                                                  path_log,
                                                                                  usuario,
                                                                                  nuevo_nombre)

                    self.database_historiales[usuario].append(log_historial)
                    with open("database/database_historiales.txt", "w") as historiales:
                        json.dump(self.database_historiales, historiales)

                    cliente.send("TODO_OK".encode('utf-8'))

            elif data_dec.startswith("ELIMINAR_CARPETA"):
                usuario = data_dec.split("SEPARADOR123456789ESPECIAL")[1]
                nombre_carpeta = data_dec.split("SEPARADOR123456789ESPECIAL")[2]
                ruta_hijo = data_dec.split("SEPARADOR123456789ESPECIAL")[3]

                data_carpea = self.eliminar_carpeta(usuario, nombre_carpeta, ruta_hijo)
                if data_carpea == "ERROR":
                    cliente.send("ERROR...Recuerda que solo puedes "
                                 "eliminar carpetas con este boton.".encode('utf-8'))

                else:
                    tiempo = str(datetime.now()).split(".")[0]
                    padre = ruta_hijo
                    path_log = "__ROOT__" + "\\" + padre
                    log_historial = '{0} - REMOVED  "{1}" by {2}'.format(tiempo, path_log, usuario)

                    self.database_historiales[usuario].append(log_historial)
                    with open("database/database_historiales.txt", "w") as historiales:
                        json.dump(self.database_historiales, historiales)

                    cliente.send("TODO_OK".encode('utf-8'))

            elif data_dec.startswith("RENOMBRAR_CARPETA"):
                usuario = data_dec.split("SEPARADOR123456789ESPECIAL")[1]
                nombre_carpeta = data_dec.split("SEPARADOR123456789ESPECIAL")[2]
                ruta_hijo = data_dec.split("SEPARADOR123456789ESPECIAL")[3]
                nuevo_nombre = data_dec.split("SEPARADOR123456789ESPECIAL")[4]

                data_archivo = self.renombrar_carpeta(usuario, nombre_carpeta, ruta_hijo, nuevo_nombre)
                if data_archivo == "ERROR":
                    cliente.send("ERROR...Recuerda que solo puedes "
                                 "renombrar carpetas con este boton.".encode('utf-8'))

                else:
                    tiempo = str(datetime.now()).split(".")[0]
                    padre = ruta_hijo
                    path_log = "__ROOT__" + "\\" + padre
                    log_historial = '{0} - RENAMED  "{1}" to "{3}" by {2}'.format(tiempo,
                                                                                  path_log,
                                                                                  usuario,
                                                                                  nuevo_nombre)

                    self.database_historiales[usuario].append(log_historial)
                    with open("database/database_historiales.txt", "w") as historiales:
                        json.dump(self.database_historiales, historiales)

                    cliente.send("TODO_OK".encode('utf-8'))

            elif data_dec.startswith("ACEPTAR"):
                usuario = data_dec.split(" ")[1]
                self.clientes_conectados.update({usuario: cliente})

            elif data_dec.startswith("STOP_ESCUCHAR"):
                cliente.send("STOP_ESCUCHAR".encode('utf-8'))

            elif data_dec.startswith("INGRESO"):
                usuario = data_dec.split(" ")[1]
                clave = data_dec.split(" ")[2]

                if self.verificar_ingreso(usuario, clave):
                    cliente.send("True".encode('utf-8'))
                else:
                    cliente.send("False".encode('utf-8'))

            elif data_dec.startswith("REGISTRO"):
                usuario = data_dec.split(" ")[1]
                clave = data_dec.split(" ")[2]

                if self.verificar_registro(usuario, clave):
                    self.registrar(usuario, clave)
                    cliente.send("True".encode('utf-8'))
                else:
                    cliente.send("False".encode('utf-8'))

            elif data_dec.startswith("AGREGAR_AMIGO"):
                usuario = data_dec.split(" ")[1]
                nuevo_amigo = data_dec.split(" ")[2]

                if nuevo_amigo != usuario:
                    if nuevo_amigo in self.database_usuarios.keys():
                        if nuevo_amigo not in self.database_amistades[usuario]:
                            self.agregar_amigo(usuario, nuevo_amigo)
                            cliente.send("True".encode('utf-8'))
                            if nuevo_amigo in self.clientes_conectados.keys():
                                self.clientes_conectados[nuevo_amigo].send("NUEVO_AMIGO".encode('utf-8'))
                        else:
                            cliente.send("El usuario ya es tu amigo.".encode('utf-8'))
                    else:
                        cliente.send("El usuario no existe.".encode('utf-8'))

                else:
                    cliente.send("No te puedes agregar a ti mismo.".encode('utf-8'))

            elif data_dec.startswith("LISTA_AMIGOS"):
                usuario = data_dec.split(" ")[1]
                lista_amigos = self.database_amistades[usuario]
                lista_enc = json.dumps(lista_amigos)
                cliente.send(lista_enc.encode('utf-8'))

            elif data_dec.startswith("LISTA_HISTORIAL"):
                usuario = data_dec.split(" ")[1]
                lista_historial = self.database_historiales[usuario]
                lista_enc = json.dumps(lista_historial)
                cliente.send(lista_enc.encode('utf-8'))

            elif data_dec.startswith("HISTORIAL_CHAT"):
                usuario = data_dec.split(" ")[1]
                amigo = data_dec.split(" ")[2]
                amistad = sorted([usuario, amigo])
                chat_name = "{0}-{1}".format(amistad[0], amistad[1])
                lista_historial = self.database_chats[chat_name]
                lista_enc = json.dumps(lista_historial)
                cliente.send(lista_enc.encode('utf-8'))

            elif data_dec.startswith("MENSAJE"):
                usuario = data_dec.split("S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5")[1]
                amigo = data_dec.split("S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5")[2]
                mensaje = data_dec.split("S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5")[3]
                amistad = sorted([usuario, amigo])
                chat_name = "{0}-{1}".format(amistad[0], amistad[1])
                self.database_chats[chat_name].append(mensaje)
                with open("database/database_chats.txt", "w") as chats:
                    json.dump(self.database_chats, chats)

                if amigo in self.clientes_conectados.keys():
                    notificacion_mensaje = "NUEVO_MENSAJE" \
                                           + "S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5" \
                                           + usuario \
                                           + "S1E2P3A4R5A6D7O8R9M0A1G2I3C4O5" \
                                           + mensaje
                    self.clientes_conectados[amigo].send(notificacion_mensaje.encode('utf-8'))

            elif data_dec.startswith("LISTA_ARCHIVOS"):
                usuario = data_dec.split(" ")[1]
                arbol = self.database_arboles[usuario]
                arbol_ser = pickle.dumps(arbol)
                cliente.send(arbol_ser)

            elif data_dec.startswith("QUIT"):
                usuario = data_dec.split(" ")[1]
                cliente.send("QUIT".encode('utf-8'))
                del self.clientes_conectados[usuario]
                self.conexiones.remove(cliente)

    def agregar_archivo(self, usuario, padre, filename, data_archivo):
        if padre == "__ROOT__":
            # Se revisa pre existencia del archivo.
            for i in range(len(self.database_archivos[usuario])):
                if self.database_archivos[usuario][i][2] == filename:
                    del self.database_archivos[usuario][i]

                    tiempo = str(datetime.now()).split(".")[0]
                    path_log = padre + "\\" + filename
                    log_historial = '{0} - REMOVED  "{1}" by {2}'.format(tiempo, path_log, usuario)

                    self.database_historiales[usuario].append(log_historial)
                    with open("database/database_historiales.txt", "w") as historiales:
                        json.dump(self.database_historiales, historiales)

                    break

            for i in range(len(self.database_arboles[usuario])):
                if self.database_arboles[usuario][i][2] == filename:
                    del self.database_arboles[usuario][i]
                    break

            self.database_archivos[usuario].append(("file", padre, filename, data_archivo))
            self.database_arboles[usuario].append(("file", padre, filename, None))


        else:

            def llegar_a_padre_arbol(lista, nombre_archivo, ruta_padre):
                for (tipo, padre, nombre, contenido) in lista:
                    if tipo == "folder" and nombre == ruta_padre[0] and len(ruta_padre) == 1:
                        contenido.append(("file", ruta_padre[0], nombre_archivo, []))
                        break
                    elif tipo == "folder" and nombre == ruta_padre[0] and len(ruta_padre) > 1:
                        llegar_a_padre_arbol(contenido, nombre_archivo, ruta_padre[1:])
                        break

            def llegar_a_padre_archivos(lista, nombre_archivo, ruta_padre, data_archivo):
                for (tipo, padre, nombre, contenido) in lista:
                    if tipo == "folder" and nombre == ruta_padre[0] and len(ruta_padre) == 1:
                        contenido.append(("file", ruta_padre[0], nombre_archivo, data_archivo))
                        break
                    elif tipo == "folder" and nombre == ruta_padre[0] and len(ruta_padre) > 1:
                        llegar_a_padre_archivos(contenido, nombre_archivo, ruta_padre[1:], data_archivo)
                        break

            ruta_padre = padre.split("\\")[1:]
            llegar_a_padre_arbol(self.database_arboles[usuario], filename, ruta_padre)
            llegar_a_padre_archivos(self.database_archivos[usuario], filename, ruta_padre, data_archivo)

        with open("database/database_archivos.txt", "wb") as database_file:
            pickle.dump(self.database_archivos, database_file)

        with open("database/database_arboles.txt", "wb") as database_tree_file:
            pickle.dump(self.database_arboles, database_tree_file)

        tiempo = str(datetime.now()).split(".")[0]
        path_log = padre + "\\" + filename
        log_historial = '{0} - ADDED    "{1}" by {2}'.format(tiempo, path_log, usuario)

        self.database_historiales[usuario].append(log_historial)
        with open("database/database_historiales.txt", "w") as historiales:
            json.dump(self.database_historiales, historiales)

    def agregar_carpeta(self, usuario, padre, foldername):
        if padre == "__ROOT__":
            # Se revisa pre existencia de la carpeta.
            for i in range(len(self.database_archivos[usuario])):
                if self.database_archivos[usuario][i][2] == foldername:
                    del self.database_archivos[usuario][i]
                    break

            for i in range(len(self.database_arboles[usuario])):
                if self.database_arboles[usuario][i][2] == foldername:
                    del self.database_arboles[usuario][i]

                    tiempo = str(datetime.now()).split(".")[0]
                    path_log = padre + "\\" + foldername
                    log_historial = '{0} - REMOVED  "{1}" by {2}'.format(tiempo, path_log, usuario)

                    self.database_historiales[usuario].append(log_historial)
                    with open("database/database_historiales.txt", "w") as historiales:
                        json.dump(self.database_historiales, historiales)

                    break

            self.database_archivos[usuario].append(("folder", padre, foldername, []))
            with open("database/database_archivos.txt", "wb") as database_file:
                pickle.dump(self.database_archivos, database_file)

            self.database_arboles[usuario].append(("folder", padre, foldername, []))
            with open("database/database_arboles.txt", "wb") as database_tree_file:
                pickle.dump(self.database_arboles, database_tree_file)

        else:

            def llegar_a_padre(self, lista, nombre_carpeta, ruta_padre, ruta_padre2):
                for (tipo, padre, nombre, contenido) in lista:
                    if tipo == "folder" and nombre == ruta_padre[0] and len(ruta_padre) == 1:
                        for (t, p, n, c) in contenido:
                            print(n)
                            if t == "folder" and n == nombre_carpeta:
                                print("Ya estaba, borrada.")
                                tiempo = str(datetime.now()).split(".")[0]
                                path_log = "\\".join(ruta_padre2) + "\\" + foldername
                                log_historial = '{0} - REMOVED  "{1}" by {2}'.format(tiempo, path_log, usuario)

                                self.database_historiales[usuario].append(log_historial)
                                with open("database/database_historiales.txt", "w") as historiales:
                                    json.dump(self.database_historiales, historiales)
                        print("Agregada.")
                        contenido.append(("folder", ruta_padre[0], nombre_carpeta, []))
                        break
                    elif tipo == "folder" and nombre == ruta_padre[0] and len(ruta_padre) > 1:
                        llegar_a_padre(self, contenido, nombre_carpeta, ruta_padre[1:], ruta_padre2)
                        break

            ruta_padre = padre.split("\\")[1:]
            llegar_a_padre(self, self.database_archivos[usuario], foldername, ruta_padre, ruta_padre)
            llegar_a_padre(self, self.database_arboles[usuario], foldername, ruta_padre, ruta_padre)

        tiempo = str(datetime.now()).split(".")[0]
        path_log = padre + "\\" + foldername
        log_historial = '{0} - ADDED    "{1}" by {2}'.format(tiempo, path_log, usuario)

        self.database_historiales[usuario].append(log_historial)
        with open("database/database_historiales.txt", "w") as historiales:
            json.dump(self.database_historiales, historiales)

    def encontrar_archivo(self, usuario, nombre_archivo, ruta_hijo):

        def obtener_data_hijo(lista, nombre_archivo, ruta_hijo):
            for (tipo, padre, nombre, contenido) in lista:
                if len(ruta_hijo) == 1 and tipo == "file" and nombre == nombre_archivo:
                    return contenido
                elif len(ruta_hijo) > 1 and tipo == "folder" and nombre == ruta_hijo[0]:
                    return obtener_data_hijo(contenido, nombre_archivo, ruta_hijo[1:])
            return "ERROR"

        ruta_hijo = ruta_hijo.split("\\")
        data_archivo = obtener_data_hijo(self.database_archivos[usuario], nombre_archivo, ruta_hijo)

        return data_archivo

    def eliminar_archivo(self, usuario, nombre_archivo, ruta_hijo):

        def obtener_data_hijo(lista, nombre_archivo, ruta_hijo):
            for (tipo, padre, nombre, contenido) in lista:
                if len(ruta_hijo) == 1 and tipo == "file" and nombre == nombre_archivo:
                    lista.remove((tipo, padre, nombre, contenido))
                    return "OK"
                elif len(ruta_hijo) > 1 and tipo == "folder" and nombre == ruta_hijo[0]:
                    return obtener_data_hijo(contenido, nombre_archivo, ruta_hijo[1:])
            return "ERROR"

        ruta_hijo = ruta_hijo.split("\\")
        data_archivo1 = obtener_data_hijo(self.database_archivos[usuario], nombre_archivo, ruta_hijo)
        data_archivo2 = obtener_data_hijo(self.database_arboles[usuario], nombre_archivo, ruta_hijo)

        with open("database/database_archivos.txt", "wb") as database_file:
            pickle.dump(self.database_archivos, database_file)

        with open("database/database_arboles.txt", "wb") as database_tree_file:
            pickle.dump(self.database_arboles, database_tree_file)

        return data_archivo1

    def eliminar_carpeta(self, usuario, nombre_carpeta, ruta_hijo):

        def obtener_data_hijo(lista, nombre_carpeta, ruta_hijo):
            for (tipo, padre, nombre, contenido) in lista:
                if len(ruta_hijo) == 1 and tipo == "folder" and nombre == nombre_carpeta:
                    lista.remove((tipo, padre, nombre, contenido))
                    return "OK"
                elif len(ruta_hijo) > 1 and tipo == "folder" and nombre == ruta_hijo[0]:
                    return obtener_data_hijo(contenido, nombre_carpeta, ruta_hijo[1:])
            return "ERROR"

        ruta_hijo = ruta_hijo.split("\\")
        data_carpeta1 = obtener_data_hijo(self.database_archivos[usuario], nombre_carpeta, ruta_hijo)
        data_carpeta2 = obtener_data_hijo(self.database_arboles[usuario], nombre_carpeta, ruta_hijo)

        with open("database/database_archivos.txt", "wb") as database_file:
            pickle.dump(self.database_archivos, database_file)

        with open("database/database_arboles.txt", "wb") as database_tree_file:
            pickle.dump(self.database_arboles, database_tree_file)

        return data_carpeta1

    def renombrar_archivo(self, usuario, nombre_archivo, ruta_hijo, nuevo_nombre):
        def obtener_data_hijo(lista, nombre_archivo, ruta_hijo, nuevo_name):
            for (tipo, padre, nombre, contenido) in lista:
                if len(ruta_hijo) == 1 and tipo == "file" and nombre == nombre_archivo:
                    aux_padre = padre
                    aux_cont = contenido
                    lista.remove((tipo, padre, nombre, contenido))
                    lista.append(("file", aux_padre, nuevo_name, aux_cont))
                    return "OK"
                elif len(ruta_hijo) > 1 and tipo == "folder" and nombre == ruta_hijo[0]:
                    return obtener_data_hijo(contenido, nombre_archivo, ruta_hijo[1:], nuevo_name)
            return "ERROR"

        ruta_hijo = ruta_hijo.split("\\")
        data_archivo1 = obtener_data_hijo(self.database_archivos[usuario], nombre_archivo, ruta_hijo, nuevo_nombre)
        data_archivo2 = obtener_data_hijo(self.database_arboles[usuario], nombre_archivo, ruta_hijo, nuevo_nombre)

        with open("database/database_archivos.txt", "wb") as database_file:
            pickle.dump(self.database_archivos, database_file)

        with open("database/database_arboles.txt", "wb") as database_tree_file:
            pickle.dump(self.database_arboles, database_tree_file)

        return data_archivo1

    def renombrar_carpeta(self, usuario, nombre_carpeta, ruta_hijo, nuevo_nombre):

        def obtener_data_hijo(lista, nombre_carpeta, ruta_hijo, nuevo_name):
            for (tipo, padre, nombre, contenido) in lista:
                if len(ruta_hijo) == 1 and tipo == "folder" and nombre == nombre_carpeta:

                    aux_padre = padre
                    aux_cont = contenido
                    lista.remove((tipo, padre, nombre, contenido))
                    lista.append(("folder", aux_padre, nuevo_name, aux_cont))

                    return "OK"
                elif len(ruta_hijo) > 1 and tipo == "folder" and nombre == ruta_hijo[0]:
                    return obtener_data_hijo(contenido, nombre_carpeta, ruta_hijo[1:], nuevo_name)
            return "ERROR"

        ruta_hijo = ruta_hijo.split("\\")
        data_carpeta1 = obtener_data_hijo(self.database_archivos[usuario], nombre_carpeta, ruta_hijo, nuevo_nombre)
        data_carpeta2 = obtener_data_hijo(self.database_arboles[usuario], nombre_carpeta, ruta_hijo, nuevo_nombre)

        with open("database/database_archivos.txt", "wb") as database_file:
            pickle.dump(self.database_archivos, database_file)

        with open("database/database_arboles.txt", "wb") as database_tree_file:
            pickle.dump(self.database_arboles, database_tree_file)

        return data_carpeta1

    def encontrar_carpeta(self, usuario, nombre_carpeta, ruta_llegar):

        def obtener_data_carpeta(lista, nombre_carpeta, ruta_llegar):
            for (tipo, padre, nombre, contenido) in lista:
                if len(ruta_llegar) == 1 and tipo == "folder" and nombre == nombre_carpeta:
                    return (tipo, padre, nombre, contenido)
                elif len(ruta_llegar) > 1 and tipo == "folder" and nombre == ruta_llegar[0]:
                    return obtener_data_carpeta(contenido, nombre_carpeta, ruta_llegar[1:])
            return "ERROR"

        data_carpeta = obtener_data_carpeta(self.database_archivos[usuario], nombre_carpeta, ruta_llegar)
        return data_carpeta

    def enviar_carpeta(self, usuario, carpeta):

        with open("data_carpeta_{}.txt".format(usuario), "wb+") as data_carpeta_file:
            pickle.dump(carpeta, data_carpeta_file)

        with open("data_carpeta_{}.txt".format(usuario), "rb") as data_carpeta_file:
            data_enviar_carpeta = data_carpeta_file.read()

        os.remove("data_carpeta_{}.txt".format(usuario))

        return data_enviar_carpeta

    def verificar_ingreso(self, usuario, clave_ing):
        if usuario in self.database_usuarios.keys():
            salt_usuario = self.database_usuarios[usuario][0]
            clave_hash_usuario = self.database_usuarios[usuario][1]

            clave_ing_enc = (clave_ing + salt_usuario).encode()
            clave_ing_hash = hashlib.sha1(clave_ing_enc).hexdigest()

            if clave_ing_hash == clave_hash_usuario:
                return True
        return False

    def verificar_registro(self, usuario_reg, clave_reg):
        if usuario_reg in self.database_usuarios.keys():
            return False
        return True

    def agregar_amigo(self, usuario, amigo):
        self.database_amistades[usuario].append(amigo)
        self.database_amistades[amigo].append(usuario)
        with open("database/database_amistades.txt", "w") as act:
            json.dump(self.database_amistades, act)

        amistad = sorted([usuario, amigo])
        chat_name = "{0}-{1}".format(amistad[0], amistad[1])
        self.database_chats.update({chat_name: []})
        with open("database/database_chats.txt", "w") as chats:
            json.dump(self.database_chats, chats)

    def registrar(self, usuario, clave):
        # Se hashea la clave.
        salt, clave_hash = hashear(clave)
        # Se escribe el usuario nuevo en el archivo database_usuarios.txt.
        with open("database/database_usuarios.txt", "a") as database_file:
            database_file.write("{0}\t{1}\t{2}\n".format(usuario, salt, clave_hash))
        # Y se agrega al diccionario database_usuarios.
        self.database_usuarios.update({usuario: (salt, clave_hash)})

        # Se agrega la lista de amigos.
        self.database_amistades.update({usuario: []})
        with open("database/database_amistades.txt", "w") as new_friend_db:
            json.dump(self.database_amistades, new_friend_db)

        # Se agrega su base de datos de archivos
        self.database_archivos.update({usuario: []})
        with open("database/database_archivos.txt", "wb") as new_files_db:
            pickle.dump(self.database_archivos, new_files_db)
        # y arbol.
        self.database_arboles.update({usuario: []})
        with open("database/database_arboles.txt", "wb") as new_trees_db:
            pickle.dump(self.database_arboles, new_trees_db)
        # y historial.
        self.database_historiales.update({usuario: []})
        with open("database/database_historiales.txt", "wb") as new_hist_db:
            pickle.dump(self.database_historiales, new_hist_db)
