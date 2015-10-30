from PyQt4 import QtCore, QtGui, uic
from SSClass import SSMilitar, SSZombie
from angulo_triangulo import angulo_triangulo
from vector_unitario import vector_unitario
from time import sleep
import os

form = uic.loadUiType("gui_basica.ui")


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cargar_spritesheet()
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
        self.MilitarLabel.setPixmap(self.SSMilitar.pie_neutro)
        # Set Mouse Tracking
        self.setMouseTracking(True)
        self.ZonaJuego.setMouseTracking(True)
        self.MilitarLabel.setMouseTracking(True)
        # Atributo de direccion de frente de MilitarLabel
        self.vector_vista = [0.0, 1.0]

    def cargar_spritesheet(self):
        self.SSMilitar = SSMilitar()
        self.SSZombie = SSZombie()

    def keyPressEvent(self, QKeyEvent):
        # Evento de pausar o activar el juego apretando barra espacio.
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            if self.EstadoJuegoLabel.text() == 'Juego Activo':
                self.EstadoJuegoLabel.setText('Juego Pausado')
            else:
                self.EstadoJuegoLabel.setText('Juego Activo')
        # TODO: Evento de avanzar al militar al presionar W,S,A,D.
        elif QKeyEvent.key() == QtCore.Qt.Key_W:
            dx = self.vector_vista[0]
            dy = self.vector_vista[1]
            self.moveMilitar(dx, dy)
        elif QKeyEvent.key() == QtCore.Qt.Key_S:
            dx = self.vector_vista[0]
            dy = -self.vector_vista[1]
            self.moveMilitar(dx, dy)
            self.moveMilitar(dx, dy)
        elif QKeyEvent.key() == QtCore.Qt.Key_A:
            dx = -self.vector_vista[1]
            dy = self.vector_vista[0]
            self.moveMilitar(dx, dy)
            self.moveMilitar(dx, dy)
        elif QKeyEvent.key() == QtCore.Qt.Key_D:
            dx = self.vector_vista[1]
            dy = -self.vector_vista[0]
            self.moveMilitar(dx, dy)
            self.moveMilitar(dx, dy)
            self.moveMilitar(dx, dy)

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

    def moveMilitar(self, dx, dy):
        # TODO: que vaya en direccion de acercarse al puntero del mouse.
        x = self.MilitarLabel.x()
        y = self.MilitarLabel.y()
        self.MilitarLabel.move(x + dx, y - dy)

    def rotarMilitar(self, angulo):
        nuevo_pixmap = self.SSMilitar.pie_neutro
        self.MilitarLabel.setPixmap(nuevo_pixmap.transformed(QtGui.QTransform().rotate(angulo)))

    def mouseMoveEvent(self, QMouseEvent):
        x_militar = self.MilitarLabel.x()
        y_militar = self.MilitarLabel.y()
        self.x_mouse = (QMouseEvent.x() - 10) - x_militar
        self.y_mouse = -((QMouseEvent.y() - 130) - y_militar)
        angulo = angulo_triangulo([0, 0], [0, 1], [self.x_mouse, self.y_mouse])
        self.rotarMilitar(angulo)
        self.vector_vista = vector_unitario([0, 0], [self.x_mouse, self.y_mouse])
        print(self.vector_vista)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
