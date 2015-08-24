from readfile_personas import cargar_personas
from readfile_cursos_evaluaciones_requisitos import cargar_cursos


def cargar_sistema():
    personas = cargar_personas()
    lista_alumnos = personas[0]
    lista_profesores = personas[1]
    lista_cursos = cargar_cursos()
    print("Sistema cargado con:\n\
- {} alumnos\n\
- {} profesores\n\
- {} cursos con evaluaciones y respectivas equivalencias\n\
        ".format(
        len(lista_alumnos),
        len(lista_profesores),
        len(lista_cursos)
    ))
    return lista_alumnos, lista_profesores, lista_cursos
