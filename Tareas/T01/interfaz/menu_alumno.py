class MenuAlumno:
    def __init__(self, sistema, alumno):
        self.opciones_alumno = {
            "1": self.agregar_curso,
            "2": self.botar_curso,
            "3": self.horario,
            "4": self.calendario,
            "5": self.mostrar_permisos_especiales,
            "6": self.cerrar_sesion
        }
        self.sesion_abierta = True
        self.alumno_in = alumno
        self.sistema = sistema

    def run(self):
        while self.sesion_abierta:
            print("""----------------------------------------\n
    BUMMER UC - MENU ALUMNO - SESION INICIADA: {0} ({1})\n
    1: Agregar Curso
    2: Botar Curso
    3: Generar Horario
    4: Generar Calendario
    5: Revisar Permisos Especiales
    6: Cerrar Sesion
                """.format(self.alumno_in.nombre, self.alumno_in.usuario))
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones_alumno.get(eleccion)
            if accion:
                accion()
            else:
                print("\n--- {0} no es una opcion valida ---\n".format(eleccion))

    def agregar_curso(self):
        #self.alumno_in.inscribir_ramo()
        print("agregar curso")

    def botar_curso(self):
        #self.alumno_in.botar_ramo()
        print("botar curso")

    def horario(self):
        self.alumno_in.generar_horario()

    def calendario(self):
        #self.alumno_in
        print("generar calendario")

    def mostrar_permisos_especiales(self):
        self.alumno_in.mostrar_permisos()

    def cerrar_sesion(self):
        self.sesion_abierta = False
        print("     --- SESION FINALIZADA ---\n")
