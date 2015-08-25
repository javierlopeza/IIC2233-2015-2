from readfiles.readfile_personas import cargar_personas
from readfiles.readfile_cursos_completos import cargar_cursos


def cargar_sistema():
    print("Cargando sistema...\n")
    personas = cargar_personas()
    lista_alumnos = personas[0]
    lista_profesores = personas[1]
    lista_cursos = cargar_cursos()
    return lista_alumnos, lista_profesores, lista_cursos
