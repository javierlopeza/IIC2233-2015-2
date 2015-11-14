# coding=utf-8
import socket
import threading
import sys
import os
from time import sleep


class Juego:
    def __init__(self):
        self.historia = ""

    def comprobar_agregado_bien(self, dicho):
        lista_palabras = dicho.split(" ")
        print(1, dicho)
        print(2, self.historia)


        if not self.historia and len(lista_palabras) == 3:
            return True
        try:
            if " ".join(lista_palabras[:-3]) == self.historia:
                return True
        except:
            return False

class Cliente:
    def __init__(self, usuario):
        self.juego = Juego()

        self.usuario = usuario
        self.host = socket.gethostname()
        self.port = 80
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s_cliente.connect((self.host, self.port))
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            recibidor.start()
        except socket.error:
            print("Error al conectar.")

    def recibir_mensajes(self):
        while True:
            data = self.s_cliente.recv(1024)
            mensaje = data.decode("utf-8")
            print(mensaje)
            self.juego.historia += mensaje
            sleep(20)
            os.system('cls')

    def enviar(self, mensaje):
        self.s_cliente.send(mensaje.encode("utf-8"))


class Servidor:
    def __init__(self, usuario):
        self.juego = Juego()

        self.usuario = usuario
        self.host = socket.gethostname()
        self.port = 80
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor.bind((self.host, self.port))
        self.s_servidor.listen(1)
        self.cliente = None
        self.aceptar()

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        self.cliente = cliente_nuevo
        thread_cliente = threading.Thread(target=self.recibir_mensajes, args=())
        thread_cliente.daemon = True
        thread_cliente.start()

    def recibir_mensajes(self):
        while True:
            data = self.cliente.recv(1024)
            mensaje = data.decode("utf-8")
            print(mensaje)
            self.juego.historia += mensaje
            sleep(20)
            os.system('cls')

    def enviar(self, mensaje):
        self.cliente.send(mensaje.encode("utf-8"))


if __name__ == '__main__':

    pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if pick == "S":
        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre)
        while True:
            texto = input()
            if server.juego.comprobar_agregado_bien(texto):
                server.juego.historia += texto
                server.enviar(texto)
            else:
                print("No es valido lo dicho, has perdido.")

    elif pick == "C":
        nombre = input("Ingrese el nombre del usuario: ")
        client = Cliente(nombre)
        while True:
            texto = input()
            if client.juego.comprobar_agregado_bien(texto):
                client.juego.historia += texto
                client.enviar(texto)
            else:
                print("No es valido lo dicho, has perdido.")
