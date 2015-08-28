def botar_curso(menu_alumno):
    nrc_a_botar = input("\nIngrese el NRC del curso que quiere botar: ")

    tiene_curso = False

    for curso in menu_alumno.alumno_in.cursos_por_tomar:
        if curso.nrc == nrc_a_botar:
            tiene_curso = True
            curso.disponibles = str(int(curso.disponibles) + 1)
            curso.ocupados = str(int(curso.ocupados) - 1)
            curso.lista_de_alumnos.remove(menu_alumno.alumno_in)
            menu_alumno.alumno_in.cursos_por_tomar.remove(curso)
            print("\n--- Curso {0} (Seccion {1}) eliminado.---\n".format(curso.curso, curso.seccion))
            break

    if not tiene_curso:
        print("\n--- No tiene inscrito un curso con NRC: {0} ---".format(nrc_a_botar))
