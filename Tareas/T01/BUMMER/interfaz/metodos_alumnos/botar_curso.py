from interfaz.metodos_alumnos.pertenece_horario import pertenece_horario
from interfaz.metodos_alumnos.hora_valida import hora_valida


def botar_curso(menu_alumno, acceso_profesor=False):
    hora = input("\nIngrese la hora actual [HH:MM]:")

    horario_correcto = False

    if hora_valida(hora) or acceso_profesor:

        if pertenece_horario(hora, menu_alumno.alumno_in.horario_inscripcion) or acceso_profesor:
            horario_correcto = True

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

    if not hora_valida(hora):
        print("\n--- La hora ingresada no respeta el formato valido. ---\n")

    elif not horario_correcto:
        print("\n--- No esta autorizado para botar cursos en este horario. ---\n")
