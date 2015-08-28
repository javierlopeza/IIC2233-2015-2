import sys
from cargar_datos import cargar_sistema
from inicio_sesion import iniciar_sesion
from interfaz.menu_alumno import MenuAlumno
from interfaz.menu_profesor import MenuProfesor
from bacanosidad.cargar_followers import cargar_followers
from bacanosidad.cargar_bacanosipuntos import cargar_bacanosipuntos
from bacanosidad.ordenar_bacanosidad import ordenar_bacanosidad


class Pacmatico:
    def __init__(self):
        self.datos = cargar_sistema()
        self.lista_alumnos = self.datos[0]
        self.lista_profesores = self.datos[1]
        self.lista_cursos = self.datos[2]
        self.bacanosidades_cargadas = self.datos[3]
        self.opciones = {
            "1": self.iniciar_sesion,
            "2": self.buscar_curso,
            "3": self.cargar_bacanosidad,
            "4": self.dar_cursos,
            "0": self.salir
        }

    @staticmethod
    def display_menu():
        print("----------------------------------------\n\n"
              "PACMATICO - MENU PRINCIPAL:\n\n"
              "1: Iniciar Sesion\n"
              "2: Buscar Curso\n"
              "3: Cargar Bacanosidad de los Alumnos\n"
              "4: Dar Cursos\n"
              "0: Salir\n"
              "            ")

    def run(self):
        while True:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones.get(eleccion)
            if accion:
                accion()
            else:
                print("\n--- {0} no es una opcion valida ---\n".format(
                    eleccion))

    def iniciar_sesion(self):
        print("""
1: Ingreso Alumnos
2: Ingreso Profesores
""")
        modo_ingreso = input("Ingrese la opcion correspondiente \
al inicio de sesion que requiere: ")

        if modo_ingreso == "1":
            es_alumno = "SI"
            print("\nInicio de Sesion Alumnos")
            usuario = input("USUARIO: ")
            clave = input("CLAVE: ")
            alumno = iniciar_sesion(
                usuario,
                clave,
                self.lista_alumnos,
                self.lista_profesores,
                es_alumno)
            if alumno:
                MenuAlumno(self, alumno).run()

        elif modo_ingreso == "2":
            es_alumno = "NO"
            print("\nInicio de Sesion Profesores")
            usuario = input("USUARIO: ")
            clave = input("CLAVE: ")
            profesor = iniciar_sesion(
                usuario,
                clave,
                self.lista_alumnos,
                self.lista_profesores,
                es_alumno)
            if profesor:
                MenuProfesor(self, profesor).run()

        else:
            print("--- La opcion {} no es valida ---\n".format(modo_ingreso))

    def buscar_curso(self):
        busqueda_valida = False
        barra_divisora = "----------------------------------------"
        sigla_busqueda = input("\nIngrese sigla del curso a buscar: ")
        print("\n")
        sigla_busqueda = sigla_busqueda.upper()

        for curso in self.lista_cursos:
            if curso.sigla == sigla_busqueda:
                busqueda_valida = True
                print(curso)
                print(barra_divisora)
        print("\n")

        if busqueda_valida:
            quiere_datos = input("Desea ver toda la informacion \
acerca de las secciones del curso? [SI/NO]: ")
            quiere_datos = quiere_datos.upper()
            if quiere_datos == "SI":
                print("\n")
                for curso in self.lista_cursos:
                    if curso.sigla == sigla_busqueda:
                        print(curso)
                        curso.mas_datos()
                        print(barra_divisora)

        else:
            print("--- La sigla {} no existe ---\n".format(sigla_busqueda))

    def cargar_bacanosidad(self):
        self.lista_alumnos = cargar_followers(self.lista_alumnos)
        self.lista_alumnos = cargar_bacanosipuntos(self.lista_alumnos)
        self.lista_alumnos = ordenar_bacanosidad(self.lista_alumnos)
        self.bacanosidades_cargadas = True

    def dar_cursos(self):
        pass

    @staticmethod
    def salir():
        print("\n     --- PACMATICO CERRADO ---")
        sys.exit(0)
