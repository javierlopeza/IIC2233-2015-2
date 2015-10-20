import sys
from PyQt4 import QtGui
from backend import Partida
import time

class Buscaminas(QtGui.QWidget):

    def __init__(self, n, minas):  # con "n" se genera una matriz de nxn
        super(Buscaminas, self).__init__()
        self.n = n
        self.minas = minas
        self.tierra = n**2 - minas
        self.partida = Partida(n, minas)
        self.termino = False
        self.clicks_exitosos = 0

        self.initUI()
        self.show()

    def initUI(self):
        self.setGeometry(50,50,300,300)
        self.label = QtGui.QLabel(':) Sobreviviendo', self)
        self.label.move(10, 275)

        grilla = QtGui.QGridLayout()
        self.setLayout(grilla)

        posicion = [(i,j) for i in range(self.n) for j in range(self.n)]

        casillas_vacias = [' ' for i in range(self.n**2)]

        self.dic_botones = {}
        for posicion, valor in zip(posicion, casillas_vacias):
            boton = QtGui.QPushButton(valor)
            boton.clicked.connect(self.buttonClickedLeft)
            self.dic_botones.update({boton: posicion})
            grilla.addWidget(boton, *posicion)
        self.setWindowTitle('Buscaminas')

    def buttonClickedLeft(self):
        if not self.termino:
            boton_clickeado = self.sender()
            posicion_clickeada = self.dic_botones[boton_clickeado]
            nuevo_label = self.apretar_boton(posicion_clickeada)
            boton_clickeado.setText(nuevo_label)
            if nuevo_label != 'X':
                self.notificar(':) Sobreviviendo')
                self.clicks_exitosos += 1
                if self.tierra == self.clicks_exitosos:
                    self.termino = True
                    self.notificar('GANO! :)')
            else:
                self.notificar('x( Exploto bomba')
                self.termino = True


    def apretar_boton(self, posicion):  # Posición como una tupla (x, y)
        "Esta funcion devuelve la cantidad de minas alrededor de un espacio"
        "No tiene ninguna relación con lo que sucederá en la UI"
        boton = self.partida.botones[posicion]
        return self.partida.clickear(boton)

    def notificar(self, mensaje):
        ":::COMPLETAR:::"
        "Debe notificar a traves de un label cuando muera o sobreviva"
        self.label.setText(mensaje)

if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        ex = Buscaminas(5, 10)
        sys.exit(app.exec_())
