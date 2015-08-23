personas_file = open("personas.txt").readlines()
#print(personas_file[3000:3100])
n = 0
for i in range(len(personas_file)):
	if personas_file[i]=='  {\n':
		if  personas_file[i+1]=='    "idolos": [],\n' and personas_file[i+4]=='    "ramos_pre": [],\n':
			nombre = personas_file[i+2][15:-3]
			clave = personas_file[i+3][14:-3]
			alumno = personas_file[i+5][15:-3]
			usuario = personas_file[i+6][16:-2]
			idolos = []
			ramos_pre = []
			#Instanciar Persona (Alumno/Profesor)

		else:
			for j in range(i,len(personas_file)):
				if personas_file[j]=='    ],\n':
					pre_idolos = personas_file[i+2:j]
					idolos = []
					pre_idolos[-1] = pre_idolos[-1]+","
					for idolo in pre_idolos:
						idolos.append(idolo[7:-3])
					break
			for k in range(i+5+len(idolos),len(personas_file)):
				if personas_file[k]=='    ],\n':
					pre_ramos_pre = personas_file[i+6+len(idolos):k]
					ramos_pre = []
					pre_ramos_pre[-1] = pre_ramos_pre[-1]+","
					for ramo in pre_ramos_pre:
						ramos_pre.append(ramo[7:-3])
					break
			nombre = personas_file[i+3+len(idolos)][15:-3]
			clave = personas_file[i+4+len(idolos)][14:-3]
			alumno = personas_file[i+7+len(idolos)+len(ramos_pre)][15:-3]
			usuario = personas_file[i+8+len(idolos)+len(ramos_pre)][16:-2]
			print(nombre)
			print(clave)
			print(alumno)
			print(usuario)
			#Instanciar Persona (Alumno/Profesor)
#print(n)
		

