from encontrar_caminos import encontrar_caminos
import datetime

class Grafo:
    def __init__(self, arcos):
        self.arcos = arcos

    def ruta_corta(self, inicio, final):
        return encontrar_caminos(self.arcos, inicio, final)
