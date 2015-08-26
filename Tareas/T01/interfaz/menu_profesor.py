class MenuProfesor:
    def __init__(self, sistema, profesor):
        self.opciones_profesor = {
            "1": self.autorizar_alumno,
            "2": self.desautorizar_alumno,
            "3": self.cerrar_sesion
        }
        self.sesion_abierta = True
        self.profesor_in = profesor
        self.sistema = sistema

    def run(self):
        while self.sesion_abierta:
            print("""----------------------------------------\n
    BUMMER UC - MENU PROFESOR - SESION INICIADA: {0} ({1})\n
    1: Dar permiso especial a alumno
    2: Quitar permiso especial a alumno
    3: Cerrar Sesion
                """.format(self.profesor_in.nombre, self.profesor_in.usuario))
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones_profesor.get(eleccion)
            if accion:
                accion()
            else:
                print("\n--- {0} no es una opcion valida ---\n".format(eleccion))

    def autorizar_alumno(self):
        self.profesor_in.dar_permiso(self)

    def desautorizar_alumno(self):
        self.profesor_in.quitar_permiso(self)

    def cerrar_sesion(self):
        self.sesion_abierta = False
        print("     --- SESION FINALIZADA ---\n")
