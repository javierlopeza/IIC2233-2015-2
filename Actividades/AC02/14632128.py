class Audifono():
	def __init__(self, min_f, max_f, impedencia, int_max):
		self.min_f = min_f
		self.max_f = max_f
		self.impedencia = impedencia
		self.int_max = int_max
	def escuchar(self, cancion):
		frase = "La cancion "+cancion+" esta siendo reproducida desde un audifono."
		print(frase)

class OverEar(Audifono):
	def __init__(self, min_f, max_f, impedencia, int_max, p_aislacion):
		super().__init__(min_f, max_f, impedencia, int_max)
		self.p_aislacion = p_aislacion

class Intraaurales(Audifono):
	def __init__(self, min_f, max_f, impedencia, int_max, p_incomodidad):
		super().__init__(min_f, max_f, impedencia, int_max)
		self.p_incomodidad = p_incomodidad

class Inalambrico(Audifono):
	def __init__(self, min_f, max_f, impedencia, int_max, rango_max):
		super().__init__(min_f, max_f, impedencia, int_max)
		self.rango_max = rango_max
	def escuchar(self, cancion):
		frase = "La cancion "+cancion+" esta siendo reproducida desde un audifono Inalambrico."
		print(frase)

class Bluetooth(Inalambrico):
	def __init__(self, min_f, max_f, impedencia, int_max, rango_max, identificador):
		super().__init__(min_f, max_f, impedencia, int_max, rango_max)
		self.identificador = identificador
	def escuchar(self, cancion):
		frase = "La cancion "+cancion+" esta siendo reproducida desde un audifono con Bluetooth."
		print(frase)

class Reproductor():
	def __init__(self):
		pass
	def conectar_audifono(self, audifono, distancia): 
	#1. El argumento distancia corresponde a la distancia a la 
	#	que se encuentra el audifono del reproductor.
	#2. El metodo conectar_audifono asume que el audifono que
	#	recibe como argumento es inalambrico.
		if distancia <= audifono.rango_max:
			print("Conexion Exitosa.")
		else:
			print("Error al conectar el audifono.")

audifono = Audifono(0,10,100,120) #Instancio un Audifono.
aud_inalambrico = Inalambrico(0,10,100,120,50) #Instancio un Audifono Inalambrico.
aud_bt = Bluetooth(0,10,100,120,50,123) #Instancio un Audifono Inalambrico Bluetooth.

audifono.escuchar("Yellow Submarine") #Reproduzco la cancion Yellow Submarine con el Audifono instanciado anteriormente.
aud_inalambrico.escuchar("We Will Rock You") #Reproduzco la cancion We Will Rock You con el Audifono Inalambrico instanciado anteriormente.
aud_bt.escuchar("Thriller") #Reproduzco la cancion Thriller con el Audifono Inalambrico Bluetooth instanciado anteriormente.

reproductor = Reproductor() #Instancio un Reproductor.

reproductor.conectar_audifono(aud_bt, 51) 
#El Audifono Inalambrico Bluetooth se encuentra 
#a una distancia mayor del rango_max que permite conectarse, 
#por lo que no se conecta y produce el error.

reproductor.conectar_audifono(aud_bt, 40)
#El Audifono Inalambrico Bluetooth se encuentra 
#a una distancia menor o igual del rango_max que permite conectarse, 
#por lo que se conecta exitosamente.
