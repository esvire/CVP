#!/usr/bin/python
# -*- coding: utf-8 -*-

# recuperacion de contrtaseña de Usuario CVP
# www.pythondiario.com

import sys
from LogIn_ui import *
from PyQt4 import QtCore, QtGui, uic
from Recuperacion_ui import *

class LoginForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnConsultar, QtCore.SIGNAL('clicked()'), self.mostrarDocumento)

    def mostrarDocumento(self):
        self.ui.label_3.setText("cedula: "+self.ui.txtDocumento.text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myVentana = LoginForm()
    myVentana.show()
    sys.exit(app.exec_())


# Cargar nuestro archivo .ui
