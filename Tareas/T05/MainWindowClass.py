from PyQt4 import QtCore, QtGui, uic
from SSClass import SSMilitar
from Zombie import  Zombie
from angulo_triangulo import angulo_triangulo_mouse, angulo_triangulo_zombie
from vector_unitario import vector_unitario
from random import randint, choice
import sys

ventana = uic.loadUiType("gui.ui")


class MainWindow(ventana[0], ventana[1]):
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
        # Atributo del origen del sistema de coordenadas de ZonaJuego.
        self.x0 = self.ZonaJuego.x()
        self.y0 = self.ZonaJuego.y()

        # Color negro para ContornoZonaJuego.
        self.ContornoZonaJuegoLabel.setStyleSheet("background-color: #000000;")

        # Agrega un militar en la mitad de ZonaJuego
        self.MilitarLabel.setPixmap(self.SSMilitar.pie_neutro)
        self.angulo_militar = 0
        self.vida_militar = 100

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

    def cargar_spritesheet(self):
        # Carga las imagenes de los Sprite Sheet del militar y zombie.
        self.SSMilitar = SSMilitar()

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
            municion_actual = int(self.MunicionLabel.text().split(' ')[1])
            if municion_actual:
                municion_nueva = municion_actual - 1
                self.setMunicion(municion_nueva)
                print("BOOM! Quedan {} balas.".format(municion_nueva))

    def setSalud(self):  # Vida entre 0 - 100
        # Metodo que:
        #   Cambia el width de la BarraSalud segun la vida.
        new_width = (385 * (1 - (100 - self.vida_militar) / 100))
        self.BarraSaludLabel.setFixedWidth(new_width)

        # Cambia el valor numerico de la vida.
        self.SaludLabel.setText('Salud: {}'.format(self.vida_militar))

        if self.vida_militar == 0:
            print('--- DEAD ---')
            sys.exit()

    def setMunicion(self, nueva_municion):
        # Cambia el texto de MunicionLabel, actualizandolo a nueva_municion.
        self.MunicionLabel.setText('Municion: {}'.format(nueva_municion))

    def setPuntaje(self, nuevo_puntaje):
        # Cambia el texto de PuntajeLabel, actualizandolo a nuevo_puntaje.
        self.PuntajeLabel.setText('Puntaje: {}'.format(nuevo_puntaje))

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

        if not topa_murallas and not topa_zombie:
            self.MilitarLabel.setPixmap(self.SSMilitar.actualizar_ss)
            self.rotarMilitar(self.angulo_militar)
            self.MilitarLabel.move(new_x, new_y)


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
        buscar_pos = True

        while buscar_pos:
            # Se crea una nueva posicion de partida para el nuevo zombie.
            # Esta posicion es en cualquiera de los bordes de ZonaJuego.
            position = [randint(self.x0, self.x0 + self.ZonaJuego.width() - 42),
                        randint(self.y0, self.x0 + self.ZonaJuego.height() - 42)]
            borde = randint(0, 1)
            if borde == 0:
                position[0] = choice([self.x0, self.x0 + self.ZonaJuego.width() - 42])
            elif borde == 1:
                position[1] = choice([self.y0, self.y0 + self.ZonaJuego.height() - 42])

            # Se verifica que el nuevo zombie no aparezca 'arriba' de otro personaje.
            # Se considera aparecer arriba si esta en un rango de
            # 55 pixeles de la posicion de otro personaje.
            hay_algo = False
            for r in range(-55, 55):
                verif_x = position[0] + r
                for s in range(-55, 55):
                    verif_y = position[1] + s
                    if [verif_x, verif_y] in self.pos_dict.values():
                        hay_algo = True
                        break
                if hay_algo:
                    break
            if not hay_algo:
                buscar_pos = False

        return position

    def addZombie(self, CreateZombieEvent):
        nombre_zombie = CreateZombieEvent.nombre_zombie
        start_position  = self.new_zombie_start_position(nombre_zombie)
        nuevo_zombie = Zombie(self,
                              x=start_position[0],
                              y=start_position[1],
                              name=nombre_zombie)

        self.pos_dict.update({nombre_zombie: (start_position[0] - 10, start_position[1] - 130)})
        self.lista_zombies.append(nuevo_zombie)

        nuevo_zombie.start()

        self.rotarZombies()