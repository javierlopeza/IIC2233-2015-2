import sistema

print("PUERTO MI PC:", sistema.puerto_inicio())
print("PUERTO BUMMER:", sistema.puerto_final())

for i in range(10000):
    if sistema.preguntar_puerto_actual()[1]:
        print()
        print("PILLADO")
        print(sistema.preguntar_puerto_actual())
        print(sistema.preguntar_puerto_robot())
        break
    else:
        sistema.hacer_conexion(0)
sistema.hacer_conexion(0)
print(sistema.preguntar_puerto_actual())
print(sistema.preguntar_puerto_robot())
print(sistema.preguntar_puerto_robot())