from PyQt4 import QtGui


class SSMilitar:
    def __init__(self):
        self.pie_neutro = QtGui.QPixmap('assets/movs_militar/pie_neutro42T.png')
        self.pie_izquierdo = QtGui.QPixmap('assets/movs_militar/pie_izquierdo42T.png')
        self.pie_derecho = QtGui.QPixmap('assets/movs_militar/pie_derecho42T.png')
        self.en_uso = self.pie_neutro
        self.toca = 'derecho'

    @property
    def actualizar_ss(self):
        if self.en_uso is self.pie_neutro:
            if self.toca == 'derecho':
                self.en_uso = self.pie_derecho
                self.toca = 'izquierdo'
            elif self.toca == 'izquierdo':
                self.en_uso = self.pie_izquierdo
                self.toca = 'derecho'
        else:
            self.en_uso = self.pie_neutro
        return self.en_uso


class SSZombie:
    def __init__(self):
        self.pie_neutro = QtGui.QPixmap('assets/movs_zombie/pie_neutro42R.png')
        self.pie_izquierdo = QtGui.QPixmap('assets/movs_zombie/pie_izquierdo42R.png')
        self.pie_derecho = QtGui.QPixmap('assets/movs_zombie/pie_derecho42R.png')

    @property
    def actualizar_ss(self):
        if self.en_uso is self.pie_neutro:
            if self.toca == 'derecho':
                self.en_uso = self.pie_derecho
                self.toca = 'izquierdo'
            elif self.toca == 'izquierdo':
                self.en_uso = self.pie_izquierdo
                self.toca = 'derecho'
        else:
            self.en_uso = self.pie_neutro
        return self.en_uso
