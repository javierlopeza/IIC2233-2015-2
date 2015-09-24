class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

gato = Animal('gato')
perro = Animal('perro')

gato2 = gato

gato2.nombre = 'le cambie'
print(gato.nombre)

lista = [gato, perro]

lista2 = []
lista2.append(lista[0])

lista2[0].nombre = 'raton'

damage = float('infinity')

def mi_funcion_loca(a,b):
    return a+b

a = mi_funcion_loca

print(a.__name__)

d = {'hola': [45,5], 'javier': [45,9], 'caca': [78,78]}

for data in d:
    a = d[data][0]
    b = d[data][1]
    d.update({data: a/b})

print(d)

if not []:
    print('hola12345654321')