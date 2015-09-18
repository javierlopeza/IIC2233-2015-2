import sys
from clases.ListaLigada import ListaLigada
from metodos_hacker.cargar_datos.cargar_red import cargar_red
from metodos_hacker.cargar_datos.cargar_padres import cargar_padres
from metodos_hacker.rutas.encontrar_caminos import encontrar_caminos
from metodos_hacker.doble_sentido.pares_doble_sentido import pares_doble_sentido
from metodos_hacker.doble_sentido.rutas_dobles import rutas_doble_sentido
from metodos_hacker.rutas.ruta_maxima import ruta_maxima
from metodos_hacker.ciclos.triangulos import ciclos_triangulares
from metodos_hacker.ciclos.cuadrados import cuadrados_limpios
from metodos_hacker.hackear.hackear_red import hackear_red
from copy import deepcopy


class Hacker:
    def __init__(self, sistema=None):
        self.sistema = sistema
        self.red_bummer = None
        self.pares_padre_destino = ListaLigada()
        self.rutas_a_bummer = None
        self.pares_bi = ListaLigada()
        self.rutas_bi = ListaLigada()
        self.opciones = ListaLigada()
        self.cargar_opciones()

    @staticmethod
    def display_menu():
        print("----------------------------------------\n\n"
              "MENU HACKEO RED BUMMER:\n\n"
              "1: Modelar y Cargar Red\n"
              "2: Ver Total Puertos\n"
              "3: Ruta a Bummer\n"
              "4: Rutas Doble Sentido\n"
              "5: Ciclos Triangulares y Cuadrados\n"
              "6: Ruta Maxima\n"
              "7: Hackear Red\n"
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
        self.opciones.append(self.mostrar_datos)
        self.opciones.append(self.ruta_bummer)
        self.opciones.append(self.rutas_doble_sentido)
        self.opciones.append(self.ciclos_triangulares_cuadrados)
        self.opciones.append(self.ruta_maxima)
        self.opciones.append(self.hackear_red)

    def cargar_red(self):
        self.red_bummer = cargar_red(self.sistema)

    def mostrar_datos(self):
        if self.red_bummer:
            print("""
INFORMACION DE LA RED MODELADA:
   -> Cantidad de Puertos: {0}
   -> Puerto Bummer: {1}
            """.format(len(self.red_bummer.puertos),
                       self.sistema.puerto_final()))
        else:
            print("\n--- ERROR: LA RED NO ESTA CARGADA ---\n")

    def ruta_bummer(self):
        if self.red_bummer:

            if len(self.pares_padre_destino) == 0:
                print(" ---> ANALIZANDO CONEXIONES")
                cargar_padres(self)

            if not self.rutas_a_bummer:
                print(" ---> BUSCANDO RUTAS A BUMMER")
                self.rutas_a_bummer = encontrar_caminos(
                    self.red_bummer.arcos,
                    0,
                    self.sistema.puerto_final())

            print(" ---> BUSCANDO EL CAMINO MAS CORTO A BUMMER")
            ruta_corta = self.rutas_a_bummer[0]
            for r in range(len(self.rutas_a_bummer)):
                if len(self.rutas_a_bummer[r]) < len(ruta_corta):
                    ruta_corta = self.rutas_a_bummer[r]

            print(" ---> GENERANDO ARCHIVO rutaABummer.txt")
            archivo_rutabummer = open("rutaABummer.txt", "w")
            archivo_rutabummer.write("CONEXION 0")
            for p in range(1, len(ruta_corta) - 1):
                puerto = ruta_corta[p]
                archivo_rutabummer.write(' {0}\nCONEXION {1}'.format(
                    puerto))
            archivo_rutabummer.write(' {0}'.format(
                self.sistema.puerto_final()))
            archivo_rutabummer.close()
            print("\n--- ARCHIVO GENERADO rutaABummer.txt ---\n")
        else:
            print("\n--- ERROR: LA RED NO ESTA CARGADA ---\n")

    def rutas_doble_sentido(self):
        if self.red_bummer:

            if len(self.pares_padre_destino) == 0:
                print(" ---> ANALIZANDO CONEXIONES")
                cargar_padres(self)

            print(" ---> BUSCANDO PARES BIDIRECCIONALES")
            self.pares_bi = pares_doble_sentido(self.pares_padre_destino)
            print(" ---> Porcentaje Revisado: 100%", end="\r")

            print(" ---> BUSCANDO RUTAS DOBLE SENTIDO")
            self.rutas_bi = rutas_doble_sentido(self.pares_bi)

            print(" ---> GENERANDO ARCHIVO rutasDobleSentido.txt")
            archivo_doblesentido = open("rutasDobleSentido.txt", "w")
            for pb in range(len(self.pares_bi)):
                escribir = "PAR {0} {1}\n".format(self.pares_bi[pb][0],
                                                  self.pares_bi[pb][1])
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

            if len(self.pares_padre_destino) == 0:
                print(" ---> ANALIZANDO CONEXIONES")
                cargar_padres(self)

            print(" ---> BUSCANDO CICLOS TRIANGULARES")
            ciclos_tri = ciclos_triangulares(self.red_bummer.arcos)
            print(" ---> Porcentaje Revisado: 100%", end="\r")
            archivo_ciclos = open("ciclos.txt", "w")
            for ciclo in ciclos_tri:
                escribir = "{0} {1} {2}\n".format(
                    ciclo[0],
                    ciclo[1],
                    ciclo[2]
                )
                archivo_ciclos.write(escribir)

            print(" ---> BUSCANDO CICLOS CUADRADOS")
            ciclos_cuad = cuadrados_limpios(self.red_bummer.arcos)
            print(" ---> Porcentaje Revisado: 100%", end="\r")
            for c in range(len(ciclos_cuad)):
                if ciclos_cuad[c][0] != ciclos_cuad[c][1]:
                    if ciclos_cuad[c][0] != ciclos_cuad[c][2]:
                        if ciclos_cuad[c][0] != ciclos_cuad[c][3]:
                            if ciclos_cuad[c][1] != ciclos_cuad[c][2]:
                                if ciclos_cuad[c][1] != ciclos_cuad[c][3]:
                                    if ciclos_cuad[c][2] != ciclos_cuad[c][3]:
                                        escribir = "{0} {1} {2} {3}\n".format(
                                            ciclos_cuad[c][0],
                                            ciclos_cuad[c][1],
                                            ciclos_cuad[c][2],
                                            ciclos_cuad[c][3])
                                        archivo_ciclos.write(escribir)

            archivo_ciclos.close()

            print("\n--- ARCHIVO GENERADO ciclos.txt ---\n")

        else:
            print("\n--- ERROR: LA RED NO ESTA CARGADA ---\n")

    def ruta_maxima(self):
        if self.red_bummer:

            if len(self.pares_padre_destino) == 0:
                print(" ---> ANALIZANDO CONEXIONES")
                cargar_padres(self)

            if not self.rutas_a_bummer:
                print(" ---> BUSCANDO RUTAS A BUMMER")
                self.rutas_a_bummer = encontrar_caminos(
                    self.red_bummer.arcos,
                    0,
                    self.sistema.puerto_final())

            print(" ---> BUSCANDO RUTA CON MAXIMA CAPACIDAD")
            rutamax_capacidad = ruta_maxima(
                self.red_bummer.puertos,
                self.rutas_a_bummer)

            rutamax = rutamax_capacidad[0]
            capacidadmax = rutamax_capacidad[1]

            print(" ---> GENERANDO ARCHIVO rutaMaxima.txt")
            archivo_rutamax = open("rutaMaxima.txt", "w")
            archivo_rutamax.write("CAP {0}\n".format(capacidadmax))
            for p in range(len(rutamax) - 1):
                escribir = "{0} {1}\n".format(rutamax[p], rutamax[p + 1])
                archivo_rutamax.write(escribir)
            archivo_rutamax.close()
            print("\n--- ARCHIVO GENERADO rutaMaxima.txt ---\n")

        else:
            print("\n--- ERROR: LA RED NO ESTA CARGADA ---\n")

    def hackear_red(self):
        if self.red_bummer:

            if len(self.pares_padre_destino) == 0:
                print(" ---> ANALIZANDO CONEXIONES")
                cargar_padres(self)

            # 1. Se hackea la red.
            nuevos_arcos = deepcopy(self.red_bummer.arcos)
            nuevos_arcos = hackear_red(nuevos_arcos)
            # 2. Escribimos primero todos los puertos.
            archivo_nocycle = open("noCycle.txt", "w")
            for arco in nuevos_arcos:
                puerto = arco[0]
                archivo_nocycle.write('PUERTO {0}\n'.format(puerto))
            # 3. Escribimos las conexiones.
            for arco in nuevos_arcos:
                puerto_base = arco[0]
                for conexion in arco[1]:
                    escribir = 'CONEXION {0} {1}\n'.format(puerto_base,
                                                           conexion)
                    archivo_nocycle.write(escribir)
            archivo_nocycle.close()
            print('\n::: RED BUMMER HACKEADA ::: '
                  'ARCHIVO noCycle.txt GENERADO :::\n')

        else:
            print("\n--- ERROR: LA RED NO ESTA CARGADA ---\n")

    @staticmethod
    def salir():
        print("\n     --- HACKEO RED BUMMER CERRADO ---")
        sys.exit(0)
