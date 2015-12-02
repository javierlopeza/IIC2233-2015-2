# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
from MainWindow import MainWindow

ventana = uic.loadUiType("login_window.ui")


class LoginWindow(ventana[0], ventana[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        icono = QtGui.QIcon(QtGui.QPixmap('assets/logo.png'))
        self.setWindowIcon(icono)

        self.IngresarButton.clicked.connect(self.ingresar_clicked)

        self.auth_flow = DropboxOAuth2FlowNoRedirect("7st46mxndppni46", "iqih79vfzyjdcwq")
        authorize_url = self.auth_flow.start()

        self.webView.load(QtCore.QUrl(authorize_url))

    def ingresar_clicked(self):
        auth_code = self.TokenText.text().strip()
        if not auth_code:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       'Por favor ingrese su token.',
                                       QtGui.QMessageBox.Ok)
            return
        try:
            access_token, user_id = self.auth_flow.finish(auth_code)
        except:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       'Revise el codigo ingresado.',
                                       QtGui.QMessageBox.Ok)
            return

        try:
            dbx = dropbox.Dropbox(access_token)

        except:
            QtGui.QMessageBox.critical(None,
                                       'ERROR',
                                       'No ha sido posible conectarse.',
                                       QtGui.QMessageBox.Ok)

        else:
            self.close()
            self.main_window = MainWindow(dbx)
            self.main_window.show()
