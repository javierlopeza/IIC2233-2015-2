class MenuAlumno:
    def __init__(self, sistema, alumno):
        self.opciones_alumno = {
            "1": self.inscribir_curso,
            "2": self.botar_curso,
            "3": self.horario,
            "4": self.calendario,
            "5": self.mostrar_permisos_especiales,
            "6": self.mostrar_datos_personales,
            "7": self.cerrar_sesion
        }
        self.sesion_abierta = True
        self.alumno_in = alumno
        self.sistema = sistema

    def run(self):
        while self.sesion_abierta:
            print("""----------------------------------------\n
    BUMMER UC - MENU ALUMNO - SESION INICIADA: {0} ({1})\n
    1: Inscribir Curso
    2: Botar Curso
    3: Generar Horario
    4: Generar Calendario
    5: Revisar Permisos Especiales
    6: Mostrar Datos Personales
    7: Cerrar Sesion
                """.format(self.alumno_in.nombre, self.alumno_in.usuario))
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones_alumno.get(eleccion)
            if accion:
                accion()
            else:
                print("\n--- {0} no es una opcion valida ---\n".format(
                    eleccion))

    def inscribir_curso(self):
        self.alumno_in.inscribir_curso(self)

    def botar_curso(self):
        self.alumno_in.botar_curso(self)

    def horario(self):
        self.alumno_in.generar_horario()

    def calendario(self):
        self.alumno_in.generar_calendario()

    def mostrar_permisos_especiales(self):
        self.alumno_in.mostrar_permisos()

    def mostrar_datos_personales(self):
        self.alumno_in.mostrar_datos_personales()

    def cerrar_sesion(self):
        self.sesion_abierta = False
        print("     --- SESION FINALIZADA ---\n")
