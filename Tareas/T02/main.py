import sistema
from ListaLigada import ListaLigada

print(sistema.posibles_conexiones())

print("PUERTO MI PC:", sistema.puerto_inicio())
print("PUERTO BUMMER:", sistema.puerto_final())

for i in range(2):
    print(sistema.preguntar_puerto_actual())
    print(sistema.posibles_conexiones())
    if sistema.preguntar_puerto_actual()[0] == sistema.puerto_final():
        print('Llegaste a Bummer!', sistema.preguntar_puerto_actual())
        break
    else:
        sistema.hacer_conexion(1)

