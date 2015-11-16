import socket
import hashlib
from cargar_database_usuarios import cargar_database_usuarios
from cargar_database_amistades import cargar_database_amistades
from hashear import hashear
import threading
import json


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
        self.clientes_conectados = []
        # Thread Aceptador
        thread_aceptador = threading.Thread(target=self.aceptar())
        thread_aceptador.setDaemon(True)
        thread_aceptador.start()

    def cargar_database(self):
        self.database_usuarios = cargar_database_usuarios()
        self.database_amistades = cargar_database_amistades()

    def aceptar(self):
        print("SERVIDOR ACTIVO...")
        while True:
            cliente_nuevo, address = self.socket_servidor.accept()
            self.clientes_conectados.append(cliente_nuevo)
            thread_cliente = threading.Thread(target=self.recibir_data, args=(cliente_nuevo,))
            thread_cliente.daemon = True
            thread_cliente.start()

    def recibir_data(self, cliente):
        while cliente in self.clientes_conectados:
            data = cliente.recv(1024)
            data_dec = data.decode('utf-8')
            if data_dec.startswith("INGRESO"):
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

            elif data_dec.startswith("QUIT"):
                cliente.send("QUIT".encode('utf-8'))
                self.clientes_conectados.remove(cliente)


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
        with open("database/database_amistades.txt", "w") as new:
            json.dump(self.database_amistades, new)