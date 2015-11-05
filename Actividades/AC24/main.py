import socket
import threading
from gato import Gato, sys


class Service:
    def __init__(self, gato):
        self.gato = gato
        self.s = None

    def escuchar(self):
        data_dec = '-1,-1'
        while True:
            data = self.s.recv(1024)
            data_dec = data.decode('ascii')
            if ',' in data_dec:
                break

        pos0 = data_dec.split(",")[0]
        pos1 = data_dec.split(",")[1]
        posicion = [int(pos0), int(pos1)]

        self.gato.editar_posicion(posicion)
        self.gato.revisar_ganador()
        print(self.gato)


class Cliente(Service):
    def __init__(self, gato):
        super().__init__(gato)
        self.host = '127.0.0.2'
        self.port = 3500
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.host, self.port))
        except socket.error:
            print("Error al conectar.")
            sys.exit()

    def enviar(self, mensaje):
        self.s.send(mensaje.encode('ascii'))
        self.gato.revisar_ganador()
        print(self.gato)


class Servidor(Service):
    def __init__(self, gato):
        super().__init__(gato)
        self.host = '127.0.0.2'
        self.port = 3500
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        self.cliente = None

    def aceptar(self):
        cliente, address = self.s.accept()
        self.cliente = cliente
        thread_cliente = threading.Thread(target=self.escuchar, args=(cliente,))
        thread_cliente.daemon = True
        thread_cliente.start()

    def enviar(self, mensaje):
        self.cliente.send(mensaje.encode('ascii'))
        self.gato.revisar_ganador()
        print(self.gato)


if __name__ == "__main__":
    juego = Gato()

    pick = input("Ingrese X si quiere ser servidor o O si desea ser cliente: ")
    if pick == "X":
        server = Servidor(juego)
        server.aceptar()
        while True:
            mensaje = input("Jugador {0} debe ingresar la posicion en que desea jugar".format(server.gato.turno))
            server.enviar(mensaje)
            juego.turno = "O"

    elif pick == "O":
        client = Cliente(juego)
        escuchador = threading.Thread(target=client.escuchar)
        escuchador.daemon = True
        escuchador.start()
        while True:
            mensajes = input("Jugador {0} debe ingresar la posicion en que desea jugar".format(client.gato.turno))
            client.enviar(mensajes)
            juego.turno = "X"
