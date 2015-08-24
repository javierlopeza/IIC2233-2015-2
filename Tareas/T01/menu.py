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
        print("""----------------------------------------\n
BUMMER UC - MENU PRINCIPAL:\n
1: Iniciar Sesion
2: Buscar Curso
3: Salir
            """)

    def mas_datos(self, curso):
        print("""\
Equivalencias: {}
Prerrequisitos: {}
Se dicta en ingles?: {}
Requiere aprobacion especial?: {}
Es retirable?: {}
Evaluaciones:\
""".format(curso.equivalencias_show, curso.pre_requisitos_show, curso.eng, curso.apr, curso.retiro))
        for ev in curso.evaluaciones:
            print(ev)
        print("\n")



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
        busqueda_valida = False
        barra_divisora = "----------------------------------------\n"
        sigla_busqueda = input("\nIngrese sigla del curso a buscar: ")
        sigla_busqueda = sigla_busqueda.upper()
        for curso in self.lista_cursos:
            if curso.sigla == sigla_busqueda:
                busqueda_valida = True
                print(curso)
                print(barra_divisora)
        if busqueda_valida:
            quiere_datos = input("Desea mas informacion acerca de los cursos? [SI/NO]: ")
            quiere_datos = quiere_datos.upper()
            if quiere_datos == "SI":
                for curso in self.lista_cursos:
                    if curso.sigla == sigla_busqueda:
                        print(curso)
                        self.mas_datos(curso)
                        print(barra_divisora)
        else:
            print("\n--- La sigla {} no existe ---\n".format(sigla_busqueda))

    def salir(self):
        print("Hasta la proxima!")
        sys.exit(0)


if __name__ == "__main__":
    InterfazBummerUC().run()

