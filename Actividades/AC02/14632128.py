class Audifono():
	def __init__(self, min_f, max_f, impedencia, int_max, **kwargs):
		self.min_f = min_f
		self.max_f = max_f
		self.impedencia = impedencia
		self.int_max = int_max
	def escuchar(self, cancion):
		frase = "La cancion "+cancion+" esta siendo reproducida desde un audifono."
		print(frase)

class OverEar(Audifono):
	def __init__(self, p_aislacion, **kwargs):
		super().__init__(**kwargs)
		self.p_aislacion = p_aislacion

class Intraaurales(Audifono):
	def __init__(self, p_incomodidad, **kwargs):
		super().__init__(**kwargs)
		self.p_incomodidad = p_incomodidad

class Inalambrico(Audifono):
	def __init__(self, rango_max, **kwargs):
		super().__init__(**kwargs)
		self.rango_max = rango_max
	def escuchar(self, cancion):
		frase = "La cancion "+cancion+" esta siendo reproducida desde un audifono Inalambrico."
		print(frase)

class Bluetooth(Inalambrico):
	def __init__(self, identificador, **kwargs):
		super().__init__(**kwargs)
		self.identificador = identificador
	def escuchar(self, cancion):
		frase = "La cancion "+cancion+" esta siendo reproducida desde un audifono con Bluetooth."
		print(frase)

class Reproductor():

	def conectar_audifono(self, audifono, distancia): 
	#1. El argumento distancia corresponde a la distancia a la 
	#	que se encuentra el audifono del reproductor.
	#2. El metodo conectar_audifono asume que el audifono que
	#	recibe como argumento es inalambrico.
		if distancia <= audifono.rango_max:
			print("Conexion Exitosa.")
		else:
			print("Error al conectar el audifono.")

audifono = Audifono(min_f=0, max_f=100, impedencia=150, int_max=200) #Instancio un Audifono.
aud_inalambrico = Inalambrico(min_f=0, max_f=100, impedencia=150, int_max=200, rango_max=50) #Instancio un Audifono Inalambrico.
aud_bt = Bluetooth(min_f=0, max_f=100, impedencia=150, int_max=200, rango_max=50, identificador=123) #Instancio un Audifono Inalambrico Bluetooth.

over = OverEar(min_f=0, max_f=100, impedencia=150, int_max=200, p_aislacion=85)

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
