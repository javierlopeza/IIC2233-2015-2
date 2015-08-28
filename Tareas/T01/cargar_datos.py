from readfiles.readfile_personas import cargar_personas
from readfiles.readfile_cursos_completos import cargar_cursos
from readfiles.readfile_bacanosidad import readfile_bacanosidad
import os.path


def cargar_sistema():
    print("Cargando sistema...\n")
    personas = cargar_personas()
    lista_alumnos = personas[0]
    lista_profesores = personas[1]
    lista_cursos = cargar_cursos()
    if os.path.isfile('bacanosidad.txt'):
        lista_alumnos = readfile_bacanosidad(lista_alumnos)
        print('--- Se encontro un archivo "bacanosidad.txt" y se cargaron las bacanosidades \
relativas de los alumnos al sistema ---')
        bacanosidades_cargadas = True
    else:
        print('--- No se encontro ningun archivo "bacanosidad.txt" \npor lo que no se han cargado las \
bacanosidades de \nlos alumnos y no se podran inscribir ramos sin haberse cargado. \n\nPara cargarlas, escoga la \
opcion indicada en el Menu Principal ---')
        bacanosidades_cargadas = False

    return lista_alumnos, lista_profesores, lista_cursos, bacanosidades_cargadas
