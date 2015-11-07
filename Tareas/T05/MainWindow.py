from PyQt4 import QtCore, QtGui, uic
from SSClass import SSMilitar, SSBox
from Zombie import Zombie
from Bala import Bala
from Reloj import SumarPuntajeEvent
from angulo_triangulo import angulo_triangulo_mouse, angulo_triangulo_zombie
from vector_unitario import vector_unitario
from random import randint, choice
from time import sleep
import sys

ventana = uic.loadUiType("gui.ui")


class MainWindow(ventana[0], ventana[1]):
    def __init__(self, control_juego):
        super().__init__()

        # Menu Inicial
        texto, ok = QtGui.QInputDialog.getText(self, "Menu Inicial", "Ingresa tu nombre: [OK] para jugar | [Cancel] para salir")
        if ok:
            self.nombre_jugador = texto
        else:
            sys.exit()

        self.setupUi(self)
        self.setup_base()

        self.control_juego = control_juego

    def setup_base(self):
        # Set titulo ventana a Age of Zombies
        self.setWindowTitle('Age of Zombies')
        # Set icono ventana.
        pixmap = QtGui.QIcon(QtGui.QPixmap('assets/icon_aoz.png'))
        self.setWindowIcon(pixmap)

        # Atributo para el puntaje del Jugador.
        self.puntaje = 0

        # Cargar los Sprite Sheet del Militar y las Boxes.
        self.SSMilitar = SSMilitar()
        self.SSBox = SSBox()

        # Color verde para la BarraSalud.
        self.BarraSaludLabel.setStyleSheet("background-color: #3DF400;")

        # Set BarraSalud ancho a 385.
        self.BarraSaludLabel.setFixedWidth(385)

        # Color blanco para ZonaJuego.
        self.ZonaJuego.setStyleSheet("background-color: #FFFFFF;")

        # Atributo del origen del sistema de coordenadas de ZonaJuego.
        self.x0 = self.ZonaJuego.x()
        self.y0 = self.ZonaJuego.y()

        # Color negro para ContornoZonaJuego.
        self.ContornoZonaJuegoLabel.setStyleSheet("background-color: #000000;")

        # Agrega un militar en la mitad de ZonaJuego
        self.MilitarLabel.setPixmap(self.SSMilitar.pie_neutro)
        self.angulo_militar = 0
        self.vida_militar = 100
        self.municiones = 50

        # Set Mouse Tracking para ZonaJuego y MilitarLabel.
        self.setMouseTracking(True)
        self.ZonaJuego.setMouseTracking(True)
        self.MilitarLabel.setMouseTracking(True)

        # Atributo de vector_vista del militar,
        # corresponde a un vector unitario apuntando
        # en la direccion de frente del militar.
        self.vector_vista = [0.0, 1.0]

        # Diccionario con las posiciones de todos los individuos/elementos en ZonaJuego.
        self.pos_dict = {'militar': [self.MilitarLabel.x(), self.MilitarLabel.y()]}

        # Creador de ids para los zombies.
        self.zombie_id = 0

        # Lista de ZombiesLabel presentes en ZonaJuego.
        self.lista_zombies = []

        # Diccionario de las Box presentes en ZonaJuego.
        self.boxes_dict = {}

        # Diccionario de Balas en ZonaJuego
        self.balas_dict = {}

    def keyPressEvent(self, QKeyEvent):
        # Evento de pausar o activar el juego apretando barra espacio.
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            if self.EstadoJuegoLabel.text() == 'Juego Activo':
                self.EstadoJuegoLabel.setText('Juego Pausado')
            else:
                self.EstadoJuegoLabel.setText('Juego Activo')

        # Evento de avanzar al militar al presionar W, S, D y A (o las flechas),
        # segun la direccion que corresponda.
        elif QKeyEvent.key() == QtCore.Qt.Key_W or QKeyEvent.key() == QtCore.Qt.Key_Up:
            dx = self.vector_vista[0]
            dy = self.vector_vista[1]
            self.moveMilitar(dx, dy)
        elif QKeyEvent.key() == QtCore.Qt.Key_S or QKeyEvent.key() == QtCore.Qt.Key_Down:
            dx = -self.vector_vista[0]
            dy = -self.vector_vista[1]
            self.moveMilitar(dx, dy)
        elif QKeyEvent.key() == QtCore.Qt.Key_D or QKeyEvent.key() == QtCore.Qt.Key_Right:
            dx = self.vector_vista[1]
            dy = -self.vector_vista[0]
            self.moveMilitar(dx, dy)
        elif QKeyEvent.key() == QtCore.Qt.Key_A or QKeyEvent.key() == QtCore.Qt.Key_Left:
            dx = -self.vector_vista[1]
            dy = self.vector_vista[0]
            self.moveMilitar(dx, dy)

    def mouseMoveEvent(self, QMouseEvent):
        # Control del evento de mover el mouse.
        x_militar = self.MilitarLabel.x()
        y_militar = self.MilitarLabel.y()
        self.x_mouse = (QMouseEvent.x() - 10) - x_militar
        self.y_mouse = -((QMouseEvent.y() - 130) - y_militar)
        angulo = angulo_triangulo_mouse([0, 0], [0, 1], [self.x_mouse, self.y_mouse])
        self.rotarMilitar(angulo)
        self.angulo_militar = angulo
        self.vector_vista = vector_unitario([0, 0], [self.x_mouse, self.y_mouse])

    def mousePressEvent(self, QMouseEvent):
        # Control del evento de hacer click.
        if QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            # Si es que quedan municiones, disminuyen en 1:
            if self.municiones:
                self.municiones -= 1
                self.setMunicion()
                start_x = self.MilitarLabel.x() + 35
                start_y = self.MilitarLabel.y() + 150
                self.addBala(start_x, start_y, self.vector_vista)

    def setSalud(self):  # Vida entre 0 - 100
        # Metodo que:
        #   Cambia el width de la BarraSalud segun la vida.
        new_width = (385 * (1 - (100 - self.vida_militar) / 100))
        self.BarraSaludLabel.setFixedWidth(new_width)

        # Cambia el valor numerico de la vida.
        self.SaludLabel.setText('Salud: {}'.format(self.vida_militar))

        if self.vida_militar == 0:
            self.terminar_juego()

    def setMunicion(self):
        # Cambia el texto de MunicionLabel, actualizandolo a nueva_municion.
        self.MunicionLabel.setText('Municion: {}'.format(self.municiones))

    def setPuntaje(self, SumarPuntajeEvent):
        self.puntaje += SumarPuntajeEvent.dpuntaje

        # Cambia el texto de PuntajeLabel, actualizandolo a nuevo_puntaje.
        self.PuntajeLabel.setText('Puntaje: {}'.format(self.puntaje))

    def setReloj(self, ChangeTimeEvent):
        # Cambia el texto de RelojLabel, actualizandolo a nuevo_tiempo.
        self.RelojLabel.setText("Tiempo: {}".format(ChangeTimeEvent.tiempo))

    def moveMilitar(self, dx, dy):
        velocidad = 4  # Factor para variar la velocidad del militar.
        x = self.MilitarLabel.x()
        y = self.MilitarLabel.y()
        new_x = x + velocidad * dx
        new_y = y - velocidad * dy

        # Control de limites de ZonaJuego, para que el militar no salga de las murallas.
        topa_murallas = True
        if -10 <= new_x <= self.ZonaJuego.width() - 35 and -10 <= new_y <= self.ZonaJuego.height() - 35:
            topa_murallas = False

        # Control de colisiones con los Zombies.
        topa_zombie = False
        for obj in self.pos_dict:
            if obj != 'militar':
                pos_ocupada = self.pos_dict[obj]
                pos_ocup_x = pos_ocupada[0]
                pos_ocup_y = pos_ocupada[1]
                if (- 3 < pos_ocup_x - new_x < 3) and (-3 < pos_ocup_y - new_y < 3):
                    topa_zombie = True
                    break

        topa_box = False
        for box in self.boxes_dict:
            pos_box = self.boxes_dict[box]
            pos_x = pos_box[0] - 30
            pos_y = pos_box[1] - 145
            if (- 30 < pos_x - new_x < 30) and (-30 < pos_y - new_y < 30):
                topa_box = True
                break

        if not topa_murallas and not topa_zombie:
            self.MilitarLabel.setPixmap(self.SSMilitar.actualizar_ss)
            self.rotarMilitar(self.angulo_militar)
            self.MilitarLabel.move(new_x, new_y)

        if topa_box:
            box[0].setParent(None)
            if box[1] == "vida":
                self.vida_militar += box[2]
                if self.vida_militar > 100:
                    self.vida_militar = 100
                self.setSalud()
            elif box[1] == "balas":
                self.municiones += box[2]
                self.setMunicion()
            del self.boxes_dict[box]

        # Se actualiza el diccionario de posiciones.
        self.pos_dict.update({'militar': [new_x, new_y]})

        # Al mover militar que se roten todos los Zombies en direccion a el.
        self.rotarZombies()

    def rotarMilitar(self, angulo):
        # Rota el QPixmap de MilitarLabel en angulo grados sentido horario.
        nuevo_pixmap = self.SSMilitar.en_uso
        self.MilitarLabel.setPixmap(nuevo_pixmap.transformed(QtGui.QTransform().rotate(angulo)))

    def rotarZombies(self):
        # Rota los zombies en lista_zombies en direccion de mirar al militar.
        for zombie in self.lista_zombies:
            militar_x = self.MilitarLabel.x() - zombie.image.x() + 10
            militar_y = self.MilitarLabel.y() - zombie.image.y() + 130
            angulo = angulo_triangulo_zombie([0, 0],
                                             [0, 1],
                                             [militar_x, -militar_y])
            zombie.rotar(angulo)

            zombie.vector_vista = vector_unitario([0, 0], [militar_x, -militar_y])

    def moveZombie(self, MoveZombieEvent):
        MoveZombieEvent.image.setPixmap(MoveZombieEvent.nuevo)
        label = MoveZombieEvent.image
        label.move(MoveZombieEvent.x, MoveZombieEvent.y)

        self.rotarZombies()

    def new_zombie_start_position(self, nombre_zombie):
        # Para verificar que la posicion inicial no este ocupada.
        while True:
            # Se crea una nueva posicion de partida para el nuevo zombie.
            # Esta posicion es en cualquiera de los bordes de ZonaJuego.
            position = [randint(self.x0, self.x0 + self.ZonaJuego.width() - 42),
                        randint(self.y0, self.y0 + self.ZonaJuego.height() - 42)]
            borde = randint(0, 1)
            if borde == 0:
                position[0] = choice([self.x0, self.x0 + self.ZonaJuego.width() - 42])
            elif borde == 1:
                position[1] = choice([self.y0, self.y0 + self.ZonaJuego.height() - 42])

            # Se verifica que el nuevo zombie no aparezca 'arriba' de otro personaje.
            # Se considera aparecer arriba si esta en un rango de
            # 55 pixeles de la posicion de otro personaje.
            hay_algo = False
            for obj in self.pos_dict:
                pos_ocupada = self.pos_dict[obj]
                pos_ocup_x = pos_ocupada[0]
                pos_ocup_y = pos_ocupada[1]
                if (- 60 < pos_ocup_x - position[0] < 60) and (-60 < pos_ocup_y - position[1] < 60):
                    hay_algo = True
                    break

            if not hay_algo:
                return position

    def addZombie(self, CreateZombieEvent):
        nombre_zombie = CreateZombieEvent.nombre_zombie
        start_position = self.new_zombie_start_position(nombre_zombie)
        nuevo_zombie = Zombie(self,
                              x=start_position[0],
                              y=start_position[1],
                              name=nombre_zombie)

        self.pos_dict.update({nombre_zombie: (start_position[0] - 10, start_position[1] - 130)})
        self.lista_zombies.append(nuevo_zombie)

        nuevo_zombie.start()

        self.rotarZombies()

    def eliminarZombie(self, EliminarZombieEvent):
        zombie_eliminado = EliminarZombieEvent.zombie
        if zombie_eliminado:
            zombie_eliminado.image.setParent(None)
            zombie_eliminado.terminate()
            self.lista_zombies.remove(EliminarZombieEvent.zombie)

            self.setPuntaje(SumarPuntajeEvent(57 * self.control_juego.tiempo_total))

    def eliminarBala(self, EliminarBalaEvent):
        bala_eliminada = EliminarBalaEvent.bala
        if bala_eliminada:
            bala_eliminada.image.setParent(None)
            bala_eliminada.terminate()
            del self.balas_dict[bala_eliminada]

    @property
    def new_box_position(self):
        # Para verificar que la posicion no este ocupada.
        while True:
            # Se crea una nueva posicion para el Box.
            # Esta posicion es cualquiera de ZonaJuego.
            new_position = [randint(self.x0, self.x0 + self.ZonaJuego.width() - 42),
                            randint(self.y0, self.y0 + self.ZonaJuego.height() - 42)]

            # Se verifica que el nuevo Box no aparezca 'arriba' de otro personaje.
            hay_algo = False
            for obj in self.pos_dict:
                pos_ocupada = self.pos_dict[obj]
                pos_ocup_x = pos_ocupada[0]
                pos_ocup_y = pos_ocupada[1]
                if (- 60 < pos_ocup_x - new_position[0] < 60) and (-60 < pos_ocup_y - new_position[1] < 60):
                    hay_algo = True
                    break

            if not hay_algo:
                return new_position

    def addBox(self, DeliverBoxEvent):
        if DeliverBoxEvent.contenido == "vida":
            new_position = self.new_box_position
            BoxLabel = QtGui.QLabel(self)
            BoxLabel.setFixedWidth(30)
            BoxLabel.setFixedHeight(30)
            BoxLabel.setPixmap(self.SSBox.vida)
            BoxLabel.setScaledContents(True)
            BoxLabel.show()
            BoxLabel.setVisible(True)
            BoxLabel.move(new_position[0], new_position[1])

            vida_extra = randint(30, 60)
            self.boxes_dict.update({(BoxLabel, "vida", vida_extra): (new_position[0], new_position[1])})


        elif DeliverBoxEvent.contenido == "balas":
            new_position = self.new_box_position
            BoxLabel = QtGui.QLabel(self)
            BoxLabel.setFixedWidth(30)
            BoxLabel.setFixedHeight(30)
            BoxLabel.setPixmap(self.SSBox.balas)
            BoxLabel.setScaledContents(True)
            BoxLabel.show()
            BoxLabel.setVisible(True)
            BoxLabel.move(new_position[0], new_position[1])

            n_balas = randint(15, 25)
            self.boxes_dict.update({(BoxLabel, "balas", n_balas): (new_position[0], new_position[1])})

    def addBala(self, x, y, vector_direccion):
        nueva_bala = Bala(self, x, y, vector_direccion)
        nueva_bala.start()

        self.balas_dict.update({nueva_bala: None})

    def moveBala(self, MoveBalaEvent):
        label = MoveBalaEvent.image
        label.move(MoveBalaEvent.x, MoveBalaEvent.y)

    def terminar_juego(self):
        # Stop ZombieDeliver, Reloj, Helicoptero
        self.control_juego.zombie_deliver.terminate()
        self.control_juego.reloj.terminate()
        self.control_juego.helicoptero.terminate()

        print(len(self.lista_zombies))
        for zombie in self.lista_zombies:
            zombie.terminate()

        QtGui.QMessageBox.information(
            self,
            "Fin del Juego",
            "Puntaje Final: {}".format(self.puntaje)
            )
        sys.exit()