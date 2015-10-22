# NOMBRES
# Osvaldo Torres    15202380
# Javier Lopez      14632128


from PyQt4 import QtGui, uic
from calc_financiero import calcular_jub

form = uic.loadUiType("hexa.ui")


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.logo_argentum.setPixmap(QtGui.QPixmap("logo_argentum.png"))
        self.logo_hexa.setPixmap(QtGui.QPixmap("logo_hexa.png"))
        self.logo_hexa.setScaledContents(True)

        self.ingreso_mensual.textChanged.connect(self.calcular)
        self.porcentaje_cotizacion.textChanged.connect(self.calcular)
        self.edad_actual.textChanged.connect(self.calcular)
        self.edad_jubilacion.textChanged.connect(self.calcular)
        self.esperanza_de_vida.textChanged.connect(self.calcular)
        self.fondo_elegido.currentIndexChanged.connect(self.calcular)
        # Completar la creación de la interfaz #

    def calcular(self):
        ingreso = self.ingreso_mensual.text()
        cotiza = self.porcentaje_cotizacion.text()
        edad = self.edad_actual.text()
        edad_j = self.edad_jubilacion.text()
        esp_vida = self.esperanza_de_vida.text()
        fondo_elegido = self.fondo_elegido.itemText(self.fondo_elegido.currentIndex())

        if ingreso == '':
            ingreso = 0
        else:
            ingreso = int(ingreso)
        if cotiza == '':
            cotiza = 0
        else:
            cotiza = int(cotiza)
        if edad == '':
            edad = 0
        else:
            edad = int(edad)
        if edad_j == '':
            edad_j = 0
        else:
            edad_j = int(edad_j)
        if esp_vida == '':
            esp_vida = 0
        else:
            esp_vida = int(esp_vida)

        aporte_mensual = ingreso * cotiza / 100
        self.aporte.setText(str(aporte_mensual))

        self.years_pension.setText(str(esp_vida - edad_j))

        rango = calcular_jub(ingreso, cotiza, edad, edad_j, esp_vida, fondo_elegido)

        if 'Error' not in rango:
            self.rango_pension.setText(rango)
        """ Completar esta función para calcular los cambios de los datos
        en tiempo real según el input del usuario. """


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
