
class MenuAlumno:
    def __init__(self, sistema, alumno):
        self.opciones_alumno = {
            "1": self.pedir_curso,
            "2": self.borrar_curso,
            "3": self.redistribuir_puntos,
            "4": self.revisar_cursos_obtenidos,
            "5": self.horario,
            "6": self.calendario,
            "7": self.mostrar_permisos_especiales,
            "8": self.mostrar_datos_personales,
            "0": self.cerrar_sesion
        }
        self.sesion_abierta = True
        self.alumno_in = alumno
        self.sistema = sistema

    def run(self):
        while self.sesion_abierta:
            print("""----------------------------------------\n
    PACMATICO - MENU ALUMNO - SESION INICIADA: {0} ({1})\n
    1: Pedir Curso
    2: Borrar Curso Pedido
    3: Redistribuir Puntos de Cursos Pedidos
    4: Revisar Cursos Obtenidos
    5: Generar Horario
    6: Generar Calendario
    7: Revisar Permisos Especiales
    8: Mostrar Datos Personales
    0: Cerrar Sesion
                """.format(self.alumno_in.nombre, self.alumno_in.usuario))
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones_alumno.get(eleccion)
            if accion:
                accion()
            else:
                print("\n--- {0} no es una opcion valida ---\n".format(
                    eleccion))

    def pedir_curso(self):
        if self.sistema.bacanosidades_cargadas:
            self.alumno_in.pedir_curso(self)
        else:
            print("--- Las bacanosidades no han sido cargadas al sistema todavia. Vuelva al menu principal y \
escoga la opcion de cargar bacanosidades.---")

    def borrar_curso(self):
        pass

    def revisar_cursos_obtenidos(self):
        pass

    def redistribuir_puntos(self):
        pass

    def inscribir_curso(self):
        if self.sistema.bacanosidades_cargadas:
            self.alumno_in.inscribir_curso(self)
        else:
            print("--- Las bacanosidades no han sido cargadas al sistema todavia. Vuelva al menu principal y \
escoga la opcion de cargar bacanosidades.---")

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
