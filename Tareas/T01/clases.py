from interfaz.metodos_profesores.dar_permiso import dar_permiso
from interfaz.metodos_profesores.quitar_permiso import quitar_permiso
from interfaz.metodos_alumnos.generar_horario import generar_horario
from interfaz.metodos_alumnos.generar_calendario import generar_calendario
from interfaz.metodos_alumnos.botar_curso import botar_curso
from interfaz.metodos_alumnos.inscribir_curso import inscribir_curso
from interfaz.metodos_alumnos.aprobo_curso import aprobo_curso

class Persona:
    def __init__(self,
                 nombre="",
                 usuario="",
                 clave="",
                 alumno="",
                 idolos=[],
                 cursos_aprobados=[],
                 **kwargs
                 ):
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.alumno = alumno
        self.idolos = idolos
        self.cursos_aprobados = cursos_aprobados


class Alumno(Persona):
    def __init__(self,
                 horario_inscripcion="",
                 cursos_por_tomar=[],
                 grupo_bummer=0,
                 **kwargs):
        super().__init__(**kwargs)
        self.horario_inscripcion = horario_inscripcion
        self.cursos_por_tomar = cursos_por_tomar
        self.grupo_bummer = grupo_bummer
        self.maximo_creditos_permitidos =\
            ((55 + 2*(6 - self.grupo_bummer))//5)*5
        self.alumno = "SI"
        self.permisos_especiales = []

    def __repr__(self):
        printear = "Nombre alumno: {0}\nUsuario: {1}\n".format(
            self.nombre,
            self.usuario
        )
        printear += "Clave: {0}\nHorario de inscripcion: {1}\nMaximo creditos permitidos: {2}\n".format(
            self.clave,
            self.horario_inscripcion,
            self.maximo_creditos_permitidos
        )
        printear += "Cursos por tomar:\n"
        for curso in self.cursos_por_tomar:
            printear += "- " + curso + "\n"
        printear += "Cursos aprobados:\n"
        for curso in self.cursos_aprobados:
            printear += "- " + curso + "\n"
        printear += "Lista de idolos:\n"
        for idolo in self.idolos:
            printear += "- " + idolo + "\n"
        return printear

    def mostrar_datos_personales(self):
        print(self)

    def inscribir_curso(self, menu_alumno):
        inscribir_curso(menu_alumno)

    def botar_curso(self, menu_alumno):
        botar_curso(menu_alumno)

    def mostrar_permisos(self):
        if len(self.permisos_especiales) != 0:
            print("\nUsted tiene permisos especiales para los siguientes cursos:")
            for curso_permiso in self.permisos_especiales:
                print('- {}, Seccion {}'.format(curso_permiso.curso, curso_permiso.seccion))
        else:
            print("\n--- Usted no tiene permisos especiales registrados. ---")

    def generar_horario(self):
        print(generar_horario(self.cursos_por_tomar)[0])
        print("       --- Horario de clases guardado en 'horario.txt' en el directorio principal 'T01'---\n")

    def generar_calendario(self):
        generar_calendario(self.cursos_por_tomar)

    def aprobo_curso(self, menu_alumno, sigla_curso):
        return aprobo_curso(menu_alumno, sigla_curso)


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
            printear_profesores += profe.nombre+", "
        printear_profesores = printear_profesores[:-2]
        if printear_profesores == "":
            printear_profesores = "Sin Profesor"
        printear = "\
Nombre curso: {}\n\
NRC: {}\n\
Sigla: {}\n\
Seccion: {}\n\
Catedra: {} -> Sala: {}\n\
Ayudantia: {} -> Sala: {}\n\
Laboratorio: {} -> Sala: {}\n\
Profesor(es): {}\n\
Campus: {}\n\
Creditos: {}\n\
Vacantes Ofrecidas: {}\n\
Vacantes Ocupadas: {}\n\
Vacantes Disponibles: {}".format(
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
Equivalencias: {}
Prerrequisitos: {}
Se dicta en ingles?: {}
Requiere aprobacion especial?: {}
Es retirable?: {}
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
        printear = "{}: el dia {} a las {} horas.".format(
            self.nombre,
            self.dia,
            self.hora
            )
        return printear