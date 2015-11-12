import socket
import threading
import sys
import os


class Interfaz:
    def show_menu(self):
        print("""
1. Mostrar por enviar
2. Agregar archivos
3. Quitar archivos
4. Enviar archivos
5. Terminar comunicacion
""")

    def elegir_opcion(self):
        eleccion = input("Ingrese su opcion (1 a 6): ")
        while not eleccion.isdecimal() or (int(eleccion) < 1 or int(eleccion) > 7):
            eleccion = input("Ingrese una opcion valida (1 a 6): ")
        return int(eleccion)


class Cliente:
    def __init__(self):
        self.menu = Interfaz()
        self.usuario = "Cliente"
        self.host = socket.gethostname()
        self.port = 800
        self.archivos_por_enviar = []
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s_cliente.connect((self.host, self.port))
            escuchador = threading.Thread(target=self.escuchar, args=())
            escuchador.daemon = True
            escuchador.start()
        except socket.error:
            print("Error al conectar.")
            sys.exit()

    def escuchar(self):
        while True:
            data = self.s_cliente.recv(1024)
            data_str = data.decode('utf-8', errors="ignore")
            datos = data_str.split("separadorespecial")

            nombre_archivo = datos[0]
            contenido_archivo = datos[1].encode('utf-8')

            with open("./Cliente_{0}".format(nombre_archivo),'wb+') as f:
                f.write(contenido_archivo)

            print("Archivo Recibido y Descargado: {}".format(nombre_archivo))


    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            print("\nARCHIVOS POR ENVIAR")
            for archivo in self.archivos_por_enviar:
                print(archivo[0])
        elif opcion == 2:
            carpeta_archivos = os.listdir("Archivos")
            print("\nARCHIVOS DISPONIBLES")
            cont = 1
            for archivo in carpeta_archivos:
                print("{0}: {1}".format(cont, archivo))
                cont += 1
            eleccion = input("Ingrese el numero de archivo que quiere agregar: ")
            while not eleccion.isdecimal() or (int(eleccion) < 1 or int(eleccion) > len(carpeta_archivos)):
                eleccion = input("Ingrese el numero de archivo que quiere agregar: ")
            eleccion = int(eleccion) - 1
            nombre_archivo_agregado = carpeta_archivos[eleccion]
            path_archivo = './Archivos/{}'.format(nombre_archivo_agregado)
            with open(path_archivo, 'rb') as f:
                bytes_archivo = f.read()
                nuevo_por_enviar = [nombre_archivo_agregado, bytes_archivo]
                self.archivos_por_enviar.append(nuevo_por_enviar)
            print("Archivo Agregado!")

        elif opcion == 3:
            print("\nARCHIVOS POR ENVIAR")
            cont = 1
            for archivo in self.archivos_por_enviar:
                print("{0}: {1}".format(cont, archivo[0]))
                cont += 1
            eleccion = input("Ingrese el numero de archivo que quiere eliminar: ")
            while not eleccion.isdecimal() or (int(eleccion) < 1 or int(eleccion) > len(self.archivos_por_enviar)):
                eleccion = input("Ingrese el numero de archivo que quiere eliminar: ")
            eleccion = int(eleccion) - 1
            self.archivos_por_enviar.remove(eleccion)
            print("Archivo Eliminado!")

        elif opcion == 4:
            print("\nARCHIVOS QUE SE ENVIARAN")
            for archivo in self.archivos_por_enviar:
                print(archivo[0])
            for archivo in self.archivos_por_enviar:
                data = archivo[0].encode("utf-8") + "separadorespecial".encode('utf-8') + archivo[1]
                self.s_cliente.send(data)
            print("{} archivos enviados.".format(len(self.archivos_por_enviar)))
            self.archivos_por_enviar.clear()
            print("Lista archivos por enviar vaciada.")

        elif opcion == 5:
            self.s_cliente.close()
            sys.exit()



class Servidor:
    def __init__(self):
        self.menu = Interfaz()
        self.usuario = "Servidor"
        self.host = socket.gethostname()
        self.port = 800
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor.bind((self.host, self.port))
        self.s_servidor.listen(1)
        self.cliente = None
        self.aceptar()
        self.archivos_por_enviar = []

    def escuchar(self):
        while True:
            data = self.cliente.recv(1024)
            data_str = data.decode('utf-8', errors="ignore")
            datos = data_str.split("separadorespecial")

            nombre_archivo = datos[0]
            contenido_archivo = datos[1].encode("utf-8")

            with open("./Servidor_{0}".format(nombre_archivo),'wb+') as f:
                f.write(contenido_archivo)

            print("Archivo Recibido y Descargado: {}".format(nombre_archivo))

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        self.cliente = cliente_nuevo
        thread_cliente = threading.Thread(target=self.escuchar, args=())
        thread_cliente.daemon = True
        thread_cliente.start()

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            print("\nARCHIVOS POR ENVIAR")
            for archivo in self.archivos_por_enviar:
                print(archivo[0])
        elif opcion == 2:
            carpeta_archivos = os.listdir("Archivos")
            print("\nARCHIVOS DISPONIBLES")
            cont = 1
            for archivo in carpeta_archivos:
                print("{0}: {1}".format(cont, archivo))
                cont += 1
            eleccion = input("Ingrese el numero de archivo que quiere agregar: ")
            while not eleccion.isdecimal() or (int(eleccion) < 1 or int(eleccion) > len(carpeta_archivos)):
                eleccion = input("Ingrese el numero de archivo que quiere agregar: ")
            eleccion = int(eleccion) - 1
            nombre_archivo_agregado = carpeta_archivos[eleccion]
            path_archivo = './Archivos/{}'.format(nombre_archivo_agregado)
            with open(path_archivo, 'rb') as f:
                bytes_archivo = f.read()
                nuevo_por_enviar = [nombre_archivo_agregado, bytes_archivo]
                self.archivos_por_enviar.append(nuevo_por_enviar)
            print("Archivo Agregado!")

        elif opcion == 3:
            print("\nARCHIVOS POR ENVIAR")
            cont = 1
            for archivo in self.archivos_por_enviar:
                print("{0}: {1}".format(cont, archivo[0]))
                cont += 1
            eleccion = input("Ingrese el numero de archivo que quiere eliminar: ")
            while not eleccion.isdecimal() or (int(eleccion) < 1 or int(eleccion) > len(self.archivos_por_enviar)):
                eleccion = input("Ingrese el numero de archivo que quiere eliminar: ")
            eleccion = int(eleccion) - 1
            self.archivos_por_enviar.remove(eleccion)
            print("Archivo Eliminado!")

        elif opcion == 4:
            print("\nARCHIVOS QUE SE ENVIARAN")
            for archivo in self.archivos_por_enviar:
                print(archivo[0])
            for archivo in self.archivos_por_enviar:
                data_enviar = archivo[0].encode("utf-8") + "separadorespecial".encode('utf-8') + archivo[1]
                self.cliente.send(data_enviar)
            print("{} archivos enviados.".format(len(self.archivos_por_enviar)))
            self.archivos_por_enviar.clear()
            print("Lista archivos por enviar vaciada.")

        elif opcion == 5:
            self.s_servidor.close()
            sys.exit()

if __name__ == "__main__":

    eleccion = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if eleccion == "S":
        server = Servidor()
        while True:
            server.menu.show_menu()
            opcion = server.menu.elegir_opcion()
            server.ejecutar_opcion(opcion)

    elif eleccion == "C":
        cliente = Cliente()
        while True:
            cliente.menu.show_menu()
            opcion = cliente.menu.elegir_opcion()
            cliente.ejecutar_opcion(opcion)
