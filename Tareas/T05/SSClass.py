from PyQt4 import QtGui


class SSMilitar:
    def __init__(self):
        self.pie_neutro = QtGui.QPixmap('assets/movs_militar/pie_neutro42T.png')
        self.pie_izquierdo = QtGui.QPixmap('assets/movs_militar/pie_izquierdo42T.png')
        self.pie_derecho = QtGui.QPixmap('assets/movs_militar/pie_derecho42T.png')
        self.en_uso = self.pie_neutro
        self.toca = 0
        self.factor = 1

    @property
    def actualizar_ss(self):
        self.toca += self.factor
        if self.toca != 0:
            if self.toca == 6:
                self.en_uso = self.pie_derecho
                self.factor = -1
            elif self.toca == -6:
                self.en_uso = self.pie_izquierdo
                self.factor = 1
        else:
            self.en_uso = self.pie_neutro
        return self.en_uso


class SSZombie:
    def __init__(self):
        self.pie_neutro = QtGui.QPixmap('assets/movs_zombie/pie_neutro42T.png')
        self.pie_izquierdo = QtGui.QPixmap('assets/movs_zombie/pie_izquierdo42T.png')
        self.pie_derecho = QtGui.QPixmap('assets/movs_zombie/pie_derecho42T.png')
        self.en_uso = self.pie_neutro
        self.toca = 0
        self.factor = 1

    @property
    def actualizar_ss(self):
        self.toca += self.factor
        if self.toca != 0:
            if self.toca == 8:
                self.en_uso = self.pie_derecho
                self.factor = -1
            elif self.toca == -8:
                self.en_uso = self.pie_izquierdo
                self.factor = 1
        else:
            self.en_uso = self.pie_neutro
        return self.en_uso
