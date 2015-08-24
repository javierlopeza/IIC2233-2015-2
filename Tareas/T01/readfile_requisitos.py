def cargar_requisitos(lista_cursos):
    requisitos_file = open("requisitos.txt").readlines()
    for i in range(len(requisitos_file)):
        if requisitos_file[i] == '  {\n':
            sigla_curso = requisitos_file[i + 2][14:-3]
            equivalencias = requisitos_file[i + 1][15:-4]
            if equivalencias == 'o tien':
            	equivalencias = ['No tiene']
            else:
            	equivalencias = equivalencias.split(' o ')
            print(equivalencias)
            
    return lista_cursos