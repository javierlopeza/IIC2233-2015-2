# -*- coding: utf-8 -*-

from DrobPoxCliente import DrobPoxCliente
import socket

if __name__ == '__main__':
    HOST = socket.gethostname()
    PORT = 4010
    cliente = DrobPoxCliente(HOST, PORT)
    cliente.run()
