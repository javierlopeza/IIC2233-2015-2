class Persona():
	def __init__(self, nombre_apellido="", usuario="", clave="", alumno="", idolos=[], cursos_aprobados=[], **kwargs):
		self.nombre = (nombre_apellido.split(" "))[0]
		self.apellido = (nombre_apellido.split(" "))[1]
		self.usuario = usuario
		self.clave = clave
		self.alumno = alumno
		self.idolos = idolos
		self.cursos_aprobados = cursos_aprobados

class Alumno(Persona):
	def __init__(self, horario_inscripcion="", cursos_por_tomar=[], **kwargs):
		super().__init__(**kwargs)
		self.horario_inscripcion = horario_inscripcion
		self.cursos_por_tomar = cursos_por_tomar
		self.alumno = "SI"
		self.permisos_especiales = []
	def inscribir_ramo(self, ramo):
		#Si cumple con todos los requisitos o tiene aprobacion especial del profesor:
		if ramo.disponibles > 0:
			# <<<<<<<<<<<<<<<---------------------- REVISAR RESTRICCIONES DE REQUISITOS, TOPES DE HORARIO, ETC...
			ramo.disponibles -= 1
			ramo.ocupados +=1
			self.cursos_por_tomar.append(ramo)
	def botar_ramo(self, ramo):
		ramo.disponibles += 1
		ramo.ocupados -= 1
		self.cursos_por_tomar.remove(ramo)
	#def generar_horario(self):
	#def generar_calendario_evaluaciones(self):



class Profesor(Persona):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.alumno = "NO"
	def dar_permiso(self, alumno, ramo):



class Horario():
	def __init__(self, hora_cat="", sala_cat="", hora_ayud="", sala_ayud="", hora_lab="", sala_lab="",**kwargs):
		self.hora_cat = hora_cat
		self.sala_cat = sala_cat
		self.hora_ayud = hora_ayud
		self.sala_ayud = sala_ayud
		self.hora_lab = hora_lab
		self.sala_lab = sala_lab

class Curso(Horario):
	def __init__(self, nombre="", sigla="", nrc=0, retiro="", eng="", aprobacion_especial="", profesor="", lista_de_alumnos=[], seccion=0, campus="", creditos=0, evaluaciones=[], pre_requisitos=[], equivalencias=[], ocupados=0, disponibles=0, ofrecidos=0, **kwargs):
		super().__init__(**kwargs)
		self.curso = nombre
		self.sigla = sigla
		self.nrc = nrc
		self.retiro = retiro
		self.eng = eng
		self.apr = aprobacion_especial
		self.profesor = Profesor(nombre_apellido=profesor)
		self.lista_de_alumnos = lista_de_alumnos
		self.horario = Horario(hora_cat="", sala_cat="", hora_ayud="", sala_ayud="", hora_lab="", sala_lab="")
		self.seccion = seccion
		self.campus = campus
		self.creditos = creditos
		self.evaluaciones = evaluaciones
		self.pre_requisitos = pre_requisitos
		self.equivalencias = equivalencias
		self.ocupados = ocupados
		self.disponibles = disponibles
		self.ofrecidos = ofrecidos

class Evaluacion():
	def __init__(self, nombre="", hora="", dia="", curso="", seccion=0):
		self.nombre = nombre
		self.hora = hora
		self.dia = dia
		self.curso = curso
		self.seccion = seccion


