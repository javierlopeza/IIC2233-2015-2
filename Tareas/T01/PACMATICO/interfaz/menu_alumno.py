class MenuAlumno:
    def __init__(self, sistema, alumno):
        self.opciones_alumno = {
            "1": self.pedir_cursos,
            "2": self.revisar_cursos_obtenidos,
            "3": self.horario,
            "4": self.calendario,
            "5": self.mostrar_permisos_especiales,
            "6": self.mostrar_datos_personales,
            "0": self.cerrar_sesion
        }
        self.sesion_abierta = True
        self.alumno_in = alumno
        self.sistema = sistema

    def run(self):
        while self.sesion_abierta:
            print("""----------------------------------------\n
    PACMATICO - MENU ALUMNO - SESION INICIADA: {0} ({1})\n
    1: Pedir Cursos
    2: Revisar Cursos Obtenidos
    3: Generar Horario
    4: Generar Calendario
    5: Revisar Permisos Especiales
    6: Mostrar Datos Personales
    0: Cerrar Sesion
                """.format(self.alumno_in.nombre, self.alumno_in.usuario))
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones_alumno.get(eleccion)
            if accion:
                accion()
            else:
                print("\n--- {0} no es una opcion valida ---\n".format(
                    eleccion))

    def pedir_cursos(self):
        if self.sistema.bacanosidades_cargadas:
            self.alumno_in.pedir_cursos(self)
        else:
            print("--- Las bacanosidades no han sido cargadas al sistema todavia. Vuelva al menu principal y \
escoga la opcion de cargar bacanosidades.---")

    def revisar_cursos_obtenidos(self):
        if self.sistema.vacantes_otorgadas:
            print("\nCARGA ACADEMICA OBTENIDA: ")
            for curso in self.alumno_in.cursos_por_tomar:
                print("   -> ",curso.curso, " - ", curso.sigla, "-",curso.seccion)
        else:
            print("\n--- Todavia no se realiza la reparticion de vacantes. \nEn el menu principal \
seleccione la opcion de Dar Cursos para realizar dicha reparticion---\n")

    def botar_curso(self):
        if self.sistema.bacanosidades_cargadas:
            self.alumno_in.botar_curso(self)
        else:
            print("--- Las bacanosidades no han sido cargadas al sistema todavia. Vuelva al menu principal y \
escoga la opcion de cargar bacanosidades.---")

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
        if self.alumno_in.creditos_tomados < 30:
            print("\n     ===== ADVERTENCIA: USTED TIENE MENOS DE 30 CREDITOS INSCRITOS =====")
            print(" ===== Vuelva a ingresar para tomar el minimo de creditos permitidos =====\n")
        print("     --- SESION FINALIZADA ---\n")
