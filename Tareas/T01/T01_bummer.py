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

class Profesor(Persona):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		'''
		nombre = self.nombre                            REVISAR TEMA DE QUE LOS PROFESORES
		self.nombre = self.apellido   	   <<<<<-----   EN CURSOS SALEN COMO apellido nombre   
		self.apellido = nombre                          EN PERSONAS SALEN COMO nombre apellido
		'''

class Horario():
	def __init__(self, hora_cat="", sala_cat="", hora_ayud="", sala_ayud="", hora_lab="", sala_lab="",**kwargs):
		self.hora_cat = hora_cat
		self.sala_cat = sala_cat
		self.hora_ayud = hora_ayud
		self.sala_ayud = sala_ayud
		self.hora_lab = hora_lab
		self.sala_lab = sala_lab

class Curso(Horario):
	def __init__(self, sigla="", profesor="", lista_de_alumnos=[], seccion=0, campus="", evaluaciones=[], requisitos=[], capacidad_maxima=0, **kwargs):
		super().__init__(**kwargs)
		self.sigla = sigla
		self.profesor = Profesor(nombre_apellido=profesor, usuario="", clave="", alumno="", idolos=[], cursos_aprobados=[])
		self.lista_de_alumnos = lista_de_alumnos
		self.horario = Horario(hora_cat="", sala_cat="", hora_ayud="", sala_ayud="", hora_lab="", sala_lab="")
		self.seccion = seccion
		self.campus = campus
		self.evaluaciones = evaluaciones
		self.requisitos = requisitos
		self.capacidad_maxima = capacidad_maxima

class Evaluacion():
	def __init__(self, nombre="", hora="", dia="", curso=""):
		self.nombre = nombre
		self.hora = hora
		self.dia = dia
		self.curso = curso


javier = Alumno(nombre_apellido="Javier Lopez", usuario="jilopez8", clave="jla123", alumno="SI", idolos=["Juan Perez","Jose Gonzalez"], cursos_aprobados=["IIC1103","MAT1620"])
print(javier.clave)
progra = Curso(sigla="IIC1103", profesor="Bellido Jesus", lista_de_alumnos=["a1","a2"], seccion=2, campus="San Joaquin", evaluaciones=[], requisitos=[], capacidad_maxima=100, hora_cat="L-W-V:3", sala_cat="CS-101", hora_ayud="", sala_ayud="", hora_lab="", sala_lab="") 
print(progra.hora_cat)