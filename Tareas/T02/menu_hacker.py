import sys
from ListaLigada import ListaLigada
from cargar_red import cargar_red
from cargar_padres import cargar_padres
from encontrar_camino import encontrar_camino
from pares_doble_sentido import pares_doble_sentido
from rutas_dobles import rutas_doble_sentido
from ciclos_triangulares import ciclos_triangulares
from ciclos_cuadrados import ciclos_cuadrados


class Hacker:
    def __init__(self, sistema=None):
        self.sistema = sistema
        self.red_bummer = None
        self.pares_padre_destino = ListaLigada()
        self.pares_bi = ListaLigada()
        self.rutas_bi = ListaLigada()
        self.opciones = ListaLigada()
        self.cargar_opciones()

    @staticmethod
    def display_menu():
        print("----------------------------------------\n\n"
              "MENU HACKEO RED BUMMER:\n\n"
              "1: Modelar y Cargar Red\n"
              "2: Ruta a Bummer\n"
              "3: Rutas Doble Sentido\n"
              "4: Ciclos Triangulares y Cuadrados\n"
              "5: Ruta Maxima\n"
              "6: Hackear Red\n"
              "0: Salir\n"
              "            ")

    def run(self):
        while True:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones[eleccion]
            if accion:
                accion()
            else:
                print("\n--- {0} no es una opcion valida ---\n".format(
                    eleccion))

    def cargar_opciones(self):
        self.opciones.append(self.salir)
        self.opciones.append(self.cargar_red)
        self.opciones.append(self.ruta_bummer)
        self.opciones.append(self.rutas_doble_sentido)
        self.opciones.append(self.ciclos_triangulares_cuadrados)
        self.opciones.append(self.ruta_maxima)
        self.opciones.append(self.hackear_red)

    def cargar_red(self):
        self.red_bummer = cargar_red(self.sistema)

    def ruta_bummer(self):
        if self.red_bummer:

            print(" ---> BUSCANDO EL CAMINO MAS CORTO AL PUERTO DE BUMMER")

            if len(self.pares_padre_destino) == 0:
                cargar_padres(self)

            ruta_corta = encontrar_camino(self.red_bummer.arcos, 0, self.sistema.puerto_final())

            archivo_rutabummer = open("rutaABummer.txt", "w")
            archivo_rutabummer.write("CONEXION 0")
            for p in range(1, len(ruta_corta) - 1):
                puerto = ruta_corta[p]
                archivo_rutabummer.write(' {0}\nCONEXION {1}'.format(puerto))
            archivo_rutabummer.write(' {0}'.format(self.sistema.puerto_final()))
            archivo_rutabummer.close()
            print("\n--- ARCHIVO GENERADO rutaABummer.txt ---\n")
        else:
            print("\n--- ERROR: LA RED NO ESTA CARGADA ---\n")

    def rutas_doble_sentido(self):
        if self.red_bummer:

            print(" ---> BUSCANDO RUTAS DOBLE SENTIDO")

            if len(self.pares_padre_destino) == 0:
                cargar_padres(self)

            self.pares_bi = pares_doble_sentido(self.pares_padre_destino)

            self.rutas_bi = rutas_doble_sentido(self.pares_bi)

            archivo_doblesentido = open("rutasDobleSentido.txt", "w")
            for pb in range(len(self.pares_bi)):
                escribir = "PAR {0} {1}\n".format(self.pares_bi[pb][0], self.pares_bi[pb][1])
                archivo_doblesentido.write(escribir)
            for rb in range(len(self.rutas_bi)):
                if self.rutas_bi[rb]:
                    escribir = "RUTA "
                    for p in range(len(self.rutas_bi[rb])):
                        escribir += "{0} ".format(self.rutas_bi[rb][p])
                    escribir += "\n"
                    archivo_doblesentido.write(escribir)

            archivo_doblesentido.close()

            print("\n--- ARCHIVO GENERADO rutasDobleSentido.txt ---\n")

        else:
            print("\n--- ERROR: LA RED NO ESTA CARGADA ---\n")

    def ciclos_triangulares_cuadrados(self):
        if self.red_bummer:

            print(" ---> BUSCANDO CICLOS TRIANGULARES Y CUADRADOS")

            if len(self.pares_padre_destino) == 0:
                cargar_padres(self)

            ciclos_tri = ciclos_triangulares(self.pares_padre_destino)
            archivo_ciclos = open("ciclos.txt", "w")
            for c in range(len(ciclos_tri)):
                escribir = "{0} {1} {2}\n".format(
                    ciclos_tri[c][0],
                    ciclos_tri[c][1],
                    ciclos_tri[c][2]
                )
                archivo_ciclos.write(escribir)

            ciclos_cuad = ciclos_cuadrados(self.pares_padre_destino)
            for c in range(len(ciclos_cuad)):
                escribir = "{0} {1} {2} {3}\n".format(
                    ciclos_cuad[c][0],
                    ciclos_cuad[c][1],
                    ciclos_cuad[c][2],
                    ciclos_cuad[c][3]
                )
                archivo_ciclos.write(escribir)

            archivo_ciclos.close()

            print("\n--- ARCHIVO GENERADO ciclos.txt ---\n")

        else:
            print("\n--- ERROR: LA RED NO ESTA CARGADA ---\n")

    def ruta_maxima(self):
        pass

    def hackear_red(self):
        pass

    @staticmethod
    def salir():
        print("\n     --- HACKEO RED BUMMER CERRADO ---")
        sys.exit(0)
