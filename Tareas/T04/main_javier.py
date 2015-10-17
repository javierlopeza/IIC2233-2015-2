# -*- encoding: utf-8 -*-
from PyQt4 import QtGui
from Simulacion import Simulacion

app = QtGui.QApplication([])
simulacion = Simulacion(app)
app.exec()
