def generar_calendario(cursos_por_tomar):
    texto_evaluaciones = ""

    if not cursos_por_tomar:
        print("\n--- No tiene cursos inscritos aun.---\n")
        return False

    hay_evaluaciones = False

    for curso in cursos_por_tomar:
        texto_evaluaciones += "-> Curso: {0} - Seccion: {1}\n".format(
            curso.curso,
            curso.seccion)
        if curso.evaluaciones:
            hay_evaluaciones = True
            for evaluacion in curso.evaluaciones:
                texto_evaluaciones += "    - {0}: el dia {1} \
a las {2} horas".format(
                    evaluacion.nombre,
                    evaluacion.dia,
                    evaluacion.hora)
                texto_evaluaciones += '\n'
            texto_evaluaciones += '\n'

        else:
            texto_evaluaciones += "   --- El curso no tiene\
evaluaciones registradas. ---\n\n"

    texto_final = ''
    if hay_evaluaciones:
        texto_final += "EVALUACIONES DE CURSOS POR TOMAR\n\n"
        texto_final += texto_evaluaciones

    else:
        texto_final = "\n--- Ninguno de sus cursos tiene evaluaciones \
registradas ---"

    calendario_file = open("calendario_evaluaciones.txt", "w")
    calendario_file.write(texto_final)
    print(texto_final)
    print("--- Calendario de evaluaciones guardado en \
'calendario_evaluaciones.txt' en el directorio donde esta 'main.py' ---")
