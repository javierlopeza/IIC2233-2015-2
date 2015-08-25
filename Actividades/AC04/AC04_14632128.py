# coding=utf-8


# Completen los métodos
# Les estamos dando un empujoncito con la lectura del input
# Al usar la clausula: "with open('sonda.txt', 'r') as f", 
# el archivo se cierra automáticamente al salir de la función.


def sonda():
    with open('sonda.txt', 'r') as f:
        minerales_encontrados = []
        for line in f:
            descubrimiento = line.split(',')
            minerales_encontrados.append(descubrimiento)
    n_consultas = int(input("Numero de consultas: "))
    while n_consultas > 0:
        coord = input("Ingrese coordenadas del material que busca:")
        coord = coord.split(',')
        encontrado = False
        for mineral in minerales_encontrados:
            if mineral[0] == coord[0] and mineral[1] == coord[1] and mineral[2] == coord[2] and mineral[3] == coord[3]:
                print(mineral[4])
                encontrado = True
        if not encontrado:
            print("No hay nada")
        n_consultas -= 1
    

def traidores():
    bufalos = []
    with open('bufalos.txt', 'r') as f:
        for line in f:
            if not(line in bufalos):
                bufalos.append(line[:-1])

    rivales = []
    with open('rivales.txt', 'r') as f:
        for line in f:
            if not(line in rivales):
                rivales.append(line[:-1])

    traidores = []
    for b in bufalos:
        if b in rivales:
            traidores.append(b)

    for t in traidores:
        print(t)


def pizzas():
    from collections import deque
    from collections import namedtuple
    Pizza = namedtuple('Pizza', 'ide')
    pila = []
    fila = deque()
    ide = 1
    n_sacadas = 0
    sing_pila = 's'
    sing_fila = 's'
    sing_sacadas = 's'
    with open('pizzas.txt', 'r') as f:
        for line in f.read().splitlines():
            if line == 'APILAR':
                nueva_pizza = Pizza(str(ide))
                ide += 1
                pila.append(nueva_pizza)
                accion = 'apilada'
                id_pizza = nueva_pizza.ide
                if len(pila) == 1:
                    sing_pila = ''
                elif len(pila) != 1:
                    sing_pila = 's'
            elif line == 'ENCOLAR':
                id_pizza = pila[-1].ide
                fila.append(pila[-1])
                pila = pila[:-1]
                accion = 'encolada'
                if len(fila) == 1:
                    sing_fila = ''
                elif len(fila) != 1:
                    sing_fila = 's'
            elif line == 'SACAR':
                id_pizza = fila[0].ide
                fila.popleft()
                accion = 'sacada'
                n_sacadas += 1
                if n_sacadas == 1:
                    sing_sacadas = ''
                elif len(pila) != 1:
                    sing_sacadas = 's'
            print('Pizza {0} {1}. {2} pizza{3} apilada{3}. {4} pizza{5} encolada{5}. {6} pizza{7} sacada{7}.'.format(
                id_pizza,
                accion,
                len(pila),
                sing_pila,
                len(fila),
                sing_fila,
                n_sacadas,
                sing_sacadas
            ))

if __name__ == '__main__':
    exit_loop = False

    functions = {"1": sonda, "2": traidores, "3": pizzas}

    while not exit_loop:
        print(""" Elegir problema:
            1. Sonda
            2. Traidores
            3. Pizzas
            Cualquier otra cosa para salir
            Respuesta: """)

        user_entry = input()

        if user_entry in functions:
            functions[user_entry]()
        else:
            exit_loop = True