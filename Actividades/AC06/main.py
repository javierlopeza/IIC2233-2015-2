import sys


class Paciente:
    def __init__(self, ide, year, mes, dia, color, hora, motivo):
        self.ide = ide
        self.year = year
        self.mes = mes
        self.dia = dia
        self.color = color
        self.hora = hora
        self.motivo = motivo

    def __str__(self):
        return "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(ide,year,mes,dia,color,hora,motivo)

class Reporte:
    def __init__(self):
        self.lista_pacientes = []
        self.i = 0
        self.ide = self.nuevo_ide(0)

    def __iter__(self):
        return self.lista_pacientes

    def agregar_pacientes(self):
        archivo = open("Reporte.txt")
        for l in archivo.readlines():
            datos = l.split("\t")
            year = datos[0]
            mes = datos[1]
            dia = datos[2]
            color = datos[3]
            hora = datos[4]
            motivo = datos[5]
            ide = next(self.ide)
            nuevo_paciente = Paciente(ide,year,mes,dia,color,hora,motivo)
            self.lista_pacientes.append(nuevo_paciente)

    def retornar_linea(self):
        archivo_reporte = open("Reporte.txt")
        for linea in archivo_reporte:
            yield linea

    def color(self, color_pedido):
        lista_color = [p for p in self.lista_pacientes if p.color == color_pedido ]
        return lista_color

    def nuevo_ide(self, n):
        while True:
            yield self.ide
            n += 1

r = Reporte
while (len(r.color('azul'))) != 10:
    r.agregar_pacientes