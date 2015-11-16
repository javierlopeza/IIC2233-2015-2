from DrobPoxServidor import DrobPoxServidor
import socket

if __name__ == '__main__':
    HOST = socket.gethostname()
    PORT = 4010
    servidor = DrobPoxServidor(HOST, PORT)
