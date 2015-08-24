from readfile_personas import cargar_personas
from readfile_cursos import cargar_cursos
from readfile_evaluaciones import cargar_evaluaciones
from readfile_requisitos import cargar_requisitos


def cargar_sistema():
    personas = cargar_personas()
    lista_alumnos = personas[0]
    lista_profesores = personas[1]
    lista_cursos = cargar_cursos()
    cursos_evaluaciones = cargar_evaluaciones(lista_cursos)
    lista_cursos = cargar_requisitos(lista_cursos)
    lista_cursos = cursos_evaluaciones[0]
    n_evaluaciones = cursos_evaluaciones[1]

    print("Sistema cargado con:\n\
- {} alumnos\n\
- {} profesores\n\
- {} cursos\n\
- {} evaluaciones\
        ".format(
        len(lista_alumnos),
        len(lista_profesores),
        len(lista_cursos),
        n_evaluaciones
    ))
    return lista_alumnos, lista_profesores, lista_cursos
