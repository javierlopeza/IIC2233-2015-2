def clasificar_conexiones(red_bummer):
    for p in range(len(red_bummer.puertos)):
        for c in range(len(red_bummer.puertos[p].conexiones)):
            red_bummer.puertos[p].conexiones[c].clasificar()
