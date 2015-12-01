# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui, uic
import dropbox
from MainWindow import MainWindow

ventana = uic.loadUiType("login_window.ui")


class LoginWindow(ventana[0], ventana[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.IngresarButton.clicked.connect(self.ingresar_clicked)

    def ingresar_clicked(self):
        token_ingresado = self.TokenText.text()
        if not token_ingresado:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       'Por favor ingrese su token.',
                                       QtGui.QMessageBox.Ok)
        else:
            try:
                dbx = dropbox.Dropbox(token_ingresado)
                dbx.users_get_current_account()

            except:
                QtGui.QMessageBox.critical(None,
                                           'ERROR',
                                           'No ha sido posible conectarse.',
                                           QtGui.QMessageBox.Ok)

            else:
                self.close()
                self.main_window = MainWindow(dbx)
                self.main_window.show()
