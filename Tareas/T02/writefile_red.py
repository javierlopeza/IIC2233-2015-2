def writefile_red(red_bummer):

    archivo_red = open("red.txt", "w")
    for p in range(len(red_bummer.puertos)):
        escribir_puerto = "PUERTO {0}\n".format(red_bummer.puertos[p].ide)
        archivo_red.write(escribir_puerto)
    for p in range(len(red_bummer.puertos)):
        for c in range(len(red_bummer.puertos[p].conexiones)):
            puerto_base = red_bummer.puertos[p].conexiones[c].puerto_base
            for d in range(len(red_bummer.puertos[p].conexiones[c].puertos_destino)):
                puerto_destino = \
                    red_bummer.puertos[p].conexiones[c].puertos_destino[d]
                tipo_conexion = red_bummer.puertos[p].conexiones[c].tipo
                escribir_conexion = "CONEXION {0} {1} {2}\n".format(
                    puerto_base,
                    puerto_destino,
                    tipo_conexion)
                archivo_red.write(escribir_conexion)
    archivo_red.close()
    print("\n--- SE HA GENERADO EL ARCHIVO red.txt ---\n")
