import sys
from cargar_datos import cargar_sistema
from inicio_sesion import iniciar_sesion


class BummerUC:
    def __init__(self):
        self.datos = cargar_sistema()
        self.lista_alumnos = self.datos[0]
        self.lista_profesores = self.datos[1]
        self.lista_cursos = self.datos[2]
        self.opciones = {
            "1": self.iniciar_sesion,
            "2": self.buscar_curso,
            "3": self.salir,
        }

    @staticmethod
    def display_menu():
        print("""----------------------------------------\n
BUMMER UC - MENU PRINCIPAL:\n
1: Iniciar Sesion
2: Buscar Curso
3: Salir
            """)

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
        modo_ingreso = input("Ingrese la opcion correspondiente al inicio de sesion que requiere: ")
        if modo_ingreso == "1":
            es_alumno = "SI"
            print("\nInicio de Sesion Alumnos")
            usuario = input("USUARIO: ")
            clave = input("CLAVE: ")
            iniciar_sesion(usuario,
                           clave,
                           self.lista_alumnos,
                           self.lista_profesores,
                           es_alumno)
        elif modo_ingreso == "2":
            es_alumno = "NO"
            print("\nInicio de Sesion Profesores")
            usuario = input("USUARIO: ")
            clave = input("CLAVE: ")
            iniciar_sesion(usuario,
                           clave,
                           self.lista_alumnos,
                           self.lista_profesores,
                           es_alumno)
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
            quiere_datos = input("Desea ver toda la informacion\
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

    @staticmethod
    def salir():
        print("\n     --- BUMMER UC CERRADO ---")
        sys.exit(0)


if __name__ == "__main__":
    BummerUC().run()
