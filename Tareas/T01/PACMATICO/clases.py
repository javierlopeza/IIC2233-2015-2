from interfaz.metodos_profesores.dar_permiso import dar_permiso
from interfaz.metodos_profesores.quitar_permiso import quitar_permiso
from interfaz.metodos_alumnos.generar_horario import generar_horario
from interfaz.metodos_alumnos.generar_calendario import generar_calendario
from interfaz.metodos_alumnos.botar_curso import botar_curso
from interfaz.metodos_alumnos.pedir_cursos import pedir_cursos
from interfaz.metodos_alumnos.aprobo_curso import aprobo_curso
from interfaz.metodos_alumnos.tiene_permiso_especial import tiene_permiso_especial
from interfaz.metodos_alumnos.redistribuir_puntaje import redistribuir_puntaje


class Persona:
    def __init__(self,
                 nombre="",
                 usuario="",
                 clave="",
                 alumno="",
                 idolos=[],
                 cursos_aprobados=[],
                 followers=[],
                 **kwargs
                 ):
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.alumno = alumno
        self.idolos = idolos
        self.cursos_aprobados = cursos_aprobados
        self.followers = []


class Alumno(Persona):
    def __init__(self,
                 cursos_por_tomar=[],
                 **kwargs):
        super().__init__(**kwargs)
        self.cursos_por_tomar = cursos_por_tomar
        self.cursos_pedidos = []
        self.bacanosipuntos = 0
        self.puntos_recibidos = 0
        self.bacanosidad_relativa = 0
        self.puntos_efectivos = 0,
        self.alumno = "SI"
        self.permisos_especiales = []
        self.idolos_instanciados = False

    def __str__(self):
        printear = "Nombre alumno: {0}\nUsuario: {1}\nClave: {2}\n".format(
            self.nombre,
            self.usuario,
            self.clave
        )
        printear += "Cursos aprobados:\n"
        for curso in self.cursos_aprobados:
            printear += "- " + curso + "\n"
        printear += "Lista de idolos:\n"
        if not self.idolos_instanciados:
            for idolo in self.idolos:
                printear += "- " + idolo + "\n"
        elif self.idolos_instanciados:
            for idolo in self.idolos:
                printear += "- " + idolo.nombre + "\n"
        printear += "Bacanosidad Relativa: {0}\n".format(
            self.bacanosidad_relativa
        )
        printear += "Cursos por tomar:\n"
        for curso in self.cursos_por_tomar:
            printear += "- " + curso.sigla + "-" + curso.seccion + "\n"

        return printear

    def __repr__(self):
        printear = "{0} -> BR:{1}".format(self.nombre, self.bacanosidad_relativa)
        return printear

    def mostrar_datos_personales(self):
        print(self)

    def pedir_cursos(self, menu_alumno):
        pedir_cursos(menu_alumno)

    def botar_curso(self, menu_alumno):
        botar_curso(menu_alumno)

    def mostrar_permisos(self):
        if len(self.permisos_especiales) != 0:
            print("\nUsted tiene permisos especiales para \
los siguientes cursos:")
            for curso_permiso in self.permisos_especiales:
                print('- {}, Seccion {}'.format(
                    curso_permiso.curso,
                    curso_permiso.seccion))
        else:
            print("\n--- Usted no tiene permisos especiales registrados. ---")

    def generar_horario(self):
        print(generar_horario(self.cursos_por_tomar))
        print("       --- Horario de clases guardado en 'horario.txt' \
en el directorio principal donde esta 'main.py'---\n")

    def generar_calendario(self):
        generar_calendario(self.cursos_por_tomar)

    def aprobo_curso(self, menu_alumno, sigla_curso):
        return aprobo_curso(menu_alumno, sigla_curso)

    def tiene_permiso_especial(self, menu_alumno, curso):
        return tiene_permiso_especial(menu_alumno, curso)

    @property
    def creditos_tomados(self):
        creditos = 0
        for curso_tomado in self.cursos_por_tomar:
            creditos += int(curso_tomado.creditos)
        return creditos

    @property
    def puntaje_pacmatico(self):
        puntaje_pacmatico = (1 + (float(self.bacanosidad_relativa) / 4) + (self.creditos_tomados / 4000)) * 800
        return puntaje_pacmatico

    def redistribuir_puntaje(self):
        redistribuir_puntaje(self.cursos_pedidos, self.puntaje_pacmatico)


class Profesor(Persona):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alumno = "NO"

    def __repr__(self):
        printear = "Nombre profesor: {}\nUsuario: {}\nClave: {}".format(
            self.nombre,
            self.usuario,
            self.clave
        )
        return printear

    def dar_permiso(self, menu_profesor):
        dar_permiso(menu_profesor)

    def quitar_permiso(self, menu_profesor):
        quitar_permiso(menu_profesor)


class Horario:
    def __init__(self,
                 hora_cat="",
                 sala_cat="",
                 hora_ayud="",
                 sala_ayud="",
                 hora_lab="",
                 sala_lab="",
                 **kwargs
                 ):
        self.hora_cat = hora_cat
        self.sala_cat = sala_cat
        self.hora_ayud = hora_ayud
        self.sala_ayud = sala_ayud
        self.hora_lab = hora_lab
        self.sala_lab = sala_lab


class Curso(Horario):
    def __init__(self,
                 nombre="",
                 sigla="",
                 nrc=0,
                 retiro="",
                 eng="",
                 aprobacion_especial="",
                 lista_profesor=[],
                 lista_de_alumnos=[],
                 seccion=0,
                 campus="",
                 creditos=0,
                 evaluaciones=[],
                 pre_requisitos_show=[],
                 pre_requisitos=[],
                 equivalencias_show=[],
                 equivalencias=[],
                 ocupados=0,
                 disponibles=0,
                 ofrecidos=0,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.curso = nombre
        self.sigla = sigla
        self.nrc = nrc
        self.retiro = retiro
        self.eng = eng
        self.apr = aprobacion_especial
        self.lista_profesor = lista_profesor
        self.lista_de_alumnos = lista_de_alumnos
        self.seccion = seccion
        self.campus = campus
        self.creditos = creditos
        self.evaluaciones = evaluaciones
        self.pre_requisitos_show = pre_requisitos_show
        self.pre_requisitos = pre_requisitos
        self.equivalencias_show = equivalencias_show
        self.equivalencias = equivalencias
        self.ocupados = ocupados
        self.disponibles = disponibles
        self.ofrecidos = ofrecidos

    def __repr__(self):
        printear_profesores = ""
        for profe in self.lista_profesor:
            printear_profesores += profe.nombre + ", "
        printear_profesores = printear_profesores[:-2]
        if printear_profesores == "":
            printear_profesores = "Sin Profesor"
        printear = "\
Nombre curso: {0}\n\
NRC: {1}\n\
Sigla: {2}\n\
Seccion: {3}\n\
Catedra: {4} -> Sala: {5}\n\
Ayudantia: {6} -> Sala: {7}\n\
Laboratorio: {8} -> Sala: {9}\n\
Profesor(es): {10}\n\
Campus: {11}\n\
Creditos: {12}\n\
Vacantes Ofrecidas: {13}\n\
Vacantes Ocupadas: {14}\n\
Vacantes Disponibles: {15}".format(
            self.curso,
            self.nrc,
            self.sigla,
            self.seccion,
            self.hora_cat,
            self.sala_cat,
            self.hora_ayud,
            self.sala_ayud,
            self.hora_lab,
            self.sala_lab,
            printear_profesores,
            self.campus,
            self.creditos,
            self.ofrecidos,
            self.ocupados,
            self.disponibles
        )
        return printear

    def mas_datos(self):
        print("""\
Equivalencias: {0}
Prerrequisitos: {1}
Se dicta en ingles?: {2}
Requiere aprobacion especial?: {3}
Es retirable?: {4}
Evaluaciones:\
""".format(self.equivalencias_show, self.pre_requisitos_show, self.eng, self.apr, self.retiro))
        for ev in self.evaluaciones:
            print(ev)


class Evaluacion:
    def __init__(self, nombre="", hora="", dia="", curso="", seccion=0):
        self.nombre = nombre
        self.hora = hora
        self.dia = dia
        self.curso = curso
        self.seccion = seccion

    def __repr__(self):
        printear = "{0}: el dia {1} a las {2} horas.".format(
            self.nombre,
            self.dia,
            self.hora
        )
        return printear
