from PyQt4 import QtCore, QtGui, uic
from math import atan2, degrees, acos, sqrt
from angulo_triangulo import angulo_triangulo
from time import sleep
import os

form = uic.loadUiType("gui_basica.ui")


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_base()

    def setup_base(self):
        # Set titulo ventana a Age of Zombies
        self.setWindowTitle('Age of Zombies')
        # Set icono ventana.
        pixmap = QtGui.QIcon(QtGui.QPixmap('assets/icon_aoz.png'))
        self.setWindowIcon(pixmap)
        # Color verde para la BarraSalud.
        self.BarraSaludLabel.setStyleSheet("background-color: #3DF400;")
        # Set BarraSalud ancho a 385.
        self.BarraSaludLabel.setFixedWidth(385)
        # Color blanco para ZonaJuego.
        self.ZonaJuego.setStyleSheet("background-color: #FFFFFF;")
        # Color negro para ContornoZonaJuego.
        self.ContornoZonaJuegoLabel.setStyleSheet("background-color: #000000;")
        # Agrega un militar en la mitad de ZonaJuego
        militar_pixmap = QtGui.QPixmap('assets/movs_militar/pie_neutro.png')
        self.MilitarLabel.setPixmap(militar_pixmap)
        self.MilitarLabel.setScaledContents(True)
        # Set Mouse Tracking
        self.setMouseTracking(True)
        self.ZonaJuego.setMouseTracking(True)
        self.MilitarLabel.setMouseTracking(True)
        # Atributos de posicion del mouse en ZonaJuego
        self.x_mouse = 210
        self.y_mouse = 0

    def keyPressEvent(self, QKeyEvent):
        # Evento de pausar o activar el juego apretando barra espacio.
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            if self.EstadoJuegoLabel.text() == 'Juego Activo':
                self.EstadoJuegoLabel.setText('Juego Pausado')
            else:
                self.EstadoJuegoLabel.setText('Juego Activo')

    def setSalud(self, vida):
        # Metodo que:
        #   Cambia el color y width de la BarraSalud segun la vida.
        new_width = (385 * (1 - (100 - vida) / 100))
        self.BarraSaludLabel.setFixedWidth(new_width)
        if vida < 60:  # Si la vida es menor a 15, el color de BarraSalud es amarillo.
            self.BarraSaludLabel.setStyleSheet("background-color: #ffff00;")
        if vida < 30:  # Si la vida es menor a 30, el color de BarraSalud es naranjo.
            self.BarraSaludLabel.setStyleSheet("background-color: #ff8000;")
        if vida < 15:  # Si la vida es menor a 15, el color de BarraSalud es rojo.
            self.BarraSaludLabel.setStyleSheet("background-color: #ff0000;")
        # Cambia el valor numerico de la vida.
        self.SaludLabel.setText('Salud: {}'.format(vida))

    def setMunicion(self, nueva_municion):
        self.MunicionLabel.setText('Municion: {}'.format(nueva_municion))

    def setPuntaje(self, nuevo_puntaje):
        self.PuntajeLabel.setText('Puntaje: {}'.format(nuevo_puntaje))

    def moveMilitar(self):
        # TODO
        x = self.MilitarLabel.x()
        y = self.MilitarLabel.y()

    def rotarMilitar(self, angulo):
        # TODO
        # pixmap = QtGui.QPixmap('assets/movs_militar/pie_neutro.png')
        pixmap = self.MilitarLabel.pixmap()
        nuevo_pixmap = pixmap.transformed(QtGui.QTransform().rotate(angulo))
        self.MilitarLabel.setPixmap(nuevo_pixmap)
        # self.MilitarLabel.setScaledContents(True)

    def mouseMoveEvent(self, QMouseEvent):
        # TODO
        x_militar = self.MilitarLabel.x()
        y_militar = self.MilitarLabel.y()
        x_previo = self.x_mouse
        y_previo = self.y_mouse
        self.x_mouse = QMouseEvent.x() - 10
        self.y_mouse = QMouseEvent.y() - 130
        angulo = angulo_triangulo([x_militar, y_militar], [x_previo, y_previo], [self.x_mouse, self.y_mouse])
        self.rotarMilitar(angulo)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
