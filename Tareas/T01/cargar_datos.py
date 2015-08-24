from readfile_personas import cargar_personas
from readfile_cursos_evaluaciones_requisitos_pre_profesores import cargar_cursos


def cargar_sistema():
    print("Cargando sistema...\n")
    personas = cargar_personas()
    lista_alumnos = personas[0]
    lista_profesores = personas[1]
    lista_cursos = cargar_cursos()
    print("Sistema cargado con:\n\
- {} alumnos\n\
- {} profesores\n\
- {} cursos con sus evaluaciones, equivalencias y prerrequisitos\n\
".format(
        len(lista_alumnos),
        len(lista_profesores),
        len(lista_cursos)
    ))
    return lista_alumnos, lista_profesores, lista_cursos
