import sys
from cargar_datos import cargar_sistema


class InterfazBummerUC:

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

    def display_menu(self):
        print("""BUMMER UC - MENU PRINCIPAL:\n
1: Iniciar Sesion
2: Buscar Curso
3: Salir
            """)

    def display_menu_datos(self):
        print("""
1: Equivalencias
2: Prerrequisitos
3: Dictado en ingles
4: Requiere aprobacion especial
5: Evaluaciones
6:
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
        print("iniciar sesion aqui")

    def buscar_curso(self):
        barra_divisora = "----------------------------------------\n"
        sigla_busqueda = input("\nIngrese sigla del curso a buscar: ")
        sigla_busqueda = sigla_busqueda.upper()
        print("\n"+barra_divisora+"\n")
        for curso in self.lista_cursos:
            if curso.sigla == sigla_busqueda:
                print(curso)
                print(barra_divisora)
        '''
        mas_datos = input("\nDesea mas informacion acerca de los cursos? [SI/NO]: ")
        mas_datos = mas_datos.upper()
        if mas_datos == "SI":
            for curso in self.lista_cursos:
                if curso.sigla == sigla_busqueda:
                    print(curso.mas_datos)
                    print(barra_divisora)
        '''

    def salir(self):
        print("Hasta la proxima!")
        sys.exit(0)


if __name__ == "__main__":
    InterfazBummerUC().run()

