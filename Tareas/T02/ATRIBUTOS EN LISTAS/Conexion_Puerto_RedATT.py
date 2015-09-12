from ListaLigadaTestATT import ListaLigadaATT


class Conexion:
    """
    Clase que construye una estructura simulando una conexion
    que sale de puerto_base y lleva a cualquier de los puertos_destino.
    """

    def __init__(self, puerto_base):
        self.puerto_base = puerto_base
        self.puertos_destino = ListaLigadaATT()
        self.pasadas = 0
        self.tipo = None

    def usar(self, ide):
        if self.pasadas < 1:
            self.pasadas += 1
            self.puertos_destino.append(ide)

    def clasificar(self):
        primer_destino = self.puertos_destino[0]
        segundo_destino = self.puertos_destino[1]

        # Se verifica si la conexion
        # solo ha llevado a 1 puerto (CONEXION NORMAL)
        conexion_normal = True
        anterior = primer_destino
        for a in range(1, len(self.puertos_destino)):
            siguiente = self.puertos_destino[a]
            if anterior != siguiente:
                conexion_normal = False
                break
            anterior = siguiente
        if conexion_normal:
            self.tipo = 'NORMAL'

        # Se verifica si la conexion ha llevado
        # a mas de 2 puertos diferentes (CONEXION ALEATORIA)
        conexion_random = False
        if not conexion_normal:
            for b in range(2, len(self.puertos_destino)):
                if self.puertos_destino[b] != primer_destino:
                    if self.puertos_destino[b] != segundo_destino:
                        if primer_destino != segundo_destino:
                            conexion_random = True
                            self.tipo = 'RANDOM'
                            break
                        else:
                            segundo_destino = self.puertos_destino[b]

        # Si no es Normal ni Random de 3 puertos, puede ser:
        # Alternante o Random de 2 puertos
        # --> Aqui se hace una suposicion explicada detalladamente en el README (1).
        conexion_alternante = False
        if not conexion_normal:
            if not conexion_random:
                for c in range(len(self.puertos_destino) - 7):
                    conexion_alternante = True
                    uno = self.puertos_destino[c]
                    dos = self.puertos_destino[c + 1]
                    if uno != dos:
                        for e1 in range(0, 9, 2):
                            if self.puertos_destino[c + e1] != uno:
                                conexion_alternante = False
                        for e2 in range(1, 9, 2):
                            if self.puertos_destino[c + e2] != dos:
                                conexion_alternante = False
                    else:
                        conexion_alternante = False
                    if conexion_alternante:
                        self.tipo = 'ALTERNANTE'
                        break
        if not conexion_alternante:
            self.tipo = 'RANDOM'


class Puerto:
    """ Clase que construye una estructura simulando un puerto
    para ser agregado a una red.
    """

    def __init__(self, ide, posibles_conexiones):
        self.ide = ide
        self.posibles_conexiones = posibles_conexiones
        self.conexiones = ListaLigadaATT()
        self.agregar_conexiones()
        self.conexion_siguiente = 0

    def agregar_conexiones(self):
        for c in range(self.posibles_conexiones):
            nueva_conexion = Conexion(self.ide)
            self.conexiones.append(nueva_conexion)

    def conectar(self, sistema):
        indice_conexion = self.conexion_siguiente
        # Uso la siguiente conexion sin pasadas, o la siguiente_conexion que le toca al Puerto.
        hay_cero = False
        for s_p in range(len(self.conexiones)):
            if self.conexiones[s_p].pasadas == 0:
                hay_cero = True
                indice_conexion = s_p
                sistema.hacer_conexion(s_p)
                break
        if not hay_cero:
            sistema.hacer_conexion(indice_conexion)
            # Cambio el valor de la proxima conexion a la siguiente.
            if self.conexion_siguiente + 1 == self.posibles_conexiones:
                self.conexion_siguiente = 0
            else:
                self.conexion_siguiente += 1

        # Si el robot no me pillo continuo:
        if not sistema.preguntar_puerto_actual()[1]:
            # A la conexion usada le agrego una pasada y el puerto al que llego.
            ide_puerto_llegada = sistema.preguntar_puerto_actual()[0]
            self.conexiones[indice_conexion].usar(ide_puerto_llegada)
        #else:
            #print("PILLADO POR EL ROBOT")

import datetime

class Red:
    """ Clase que construye una estructura simulando una red.
    """

    def __init__(self):
        self.puertos = ListaLigadaATT()

    def revisar_completitud(self):
        faltantes = 0
        for p in range(len(self.puertos)):
            for c in range(len(self.puertos[p].conexiones)):
                rest_s = 1 - self.puertos[p].conexiones[c].pasadas
                faltantes += rest_s
                #if self.puertos[p].conexiones[c].pasadas < 20:
                #    return False
        #return True
        print(faltantes, end="\r")
        return faltantes

    def agregar_puerto(self, ide_nuevo_puerto, posibles_conexiones_nuevo_puerto):
        """ Primero verifica si el puerto ya ha sido agregado a la Red que se esta construyendo.
        Si el puerto no se encuentra en la Red, entonces lo agrega.
        """
        if not self.tiene_puerto(ide_nuevo_puerto):
            nuevo_puerto = Puerto(ide_nuevo_puerto, posibles_conexiones_nuevo_puerto)
            self.puertos.append(nuevo_puerto)

    def tiene_puerto(self, ide_puerto):
        for p in range(len(self.puertos)):
            if self.puertos[p].ide == ide_puerto:
                return True
        return False

    def puerto(self, ide):
        """ ide corresponde al ide del puerto que se quiere encontrar en la red ya construida.
        Retorna el puerto con tal ide.
        """
        for p in range(len(self.puertos)):
            if self.puertos[p].ide == ide:
                return self.puertos[p]
