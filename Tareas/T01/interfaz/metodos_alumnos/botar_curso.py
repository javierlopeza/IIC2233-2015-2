def botar_curso(menu_alumno):
    nrc_a_botar = input("\nIngrese el NRC del curso que quiere botar: ")
    tiene_curso = False
    for curso in menu_alumno.alumno_in.cursos_por_tomar:
        if curso.nrc == nrc_a_botar:
            tiene_curso = True
            curso.disponibles += 1
            curso.ocupados -= 1
            curso.lista_de_alumnos.remove(menu_alumno.alumno_in)
            menu_alumno.alumno_in.cursos_por_tomar.remove(curso)
            print("Curso {0} (Seccion {1}) eliminado.".format(curso.nombre, curso.seccion))
            break
    if not tiene_curso:
        print("\n--- Usted no tiene inscrito un curso con NRC: {0} ---".format(nrc_a_botar))