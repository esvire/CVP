#!/usr/bin/python
# -*- coding: utf-8 -*-

# Login de Usuario CVP
# www.pythondiario.com

import sys
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from LogIn_ui import *

class LoginForm(QtGui.QDialog):

    query = ""
    clave = ""
    nombre = ""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnIngresar, QtCore.SIGNAL('clicked()'), self.consultaDB)

    def consultaDB(self):
        #app 	= QApplication(sys.argv)
        table 	= QTableWidget()
        db 		= QSqlDatabase.addDatabase("QMYSQL")

        table.setWindowTitle("Connect to Mysql Database Example")

        db.setHostName("localhost")
        db.setDatabaseName("db_club")
        db.setUserName("root")
        db.setPassword("12345")

        if (db.open()==False):
            QMessageBox.critical(None, "Database Error", db.lastError().text())

        query = QSqlQuery("SELECT email, contraseña FROM tbl_usuario WHERE email = 'correo' AND contraseña = 'abc123'")
        #% (self.ui.txtUser.text(),  self.ui.txtClave.text())
        #table.setColumnCount(query.record().count())
        #table.setRowCount(query.size())
        #table.setGeometry(0,0,500,250)
        print clave
        print "entro"

        index = 0
        while (query.next()):

            clave = query.value(0).toString()
            nombre = query.value(1).toString()
            print clave
            print "entro"
            self.ui.label_4.setText(self,clave+" "+nombre)
            table.setItem(index,0,QTableWidgetItem(query.value(0).toString()))
            table.setItem(index,1,QTableWidgetItem(query.value(1).toString()))
            #table.setItem(index,2,QTableWidgetItem(query.value(2).toString()))
            #table.setItem(index,3,QTableWidgetItem(query.value(3).toString()))
            #table.setItem(index,4,QTableWidgetItem(query.value(4).toString()))
            index = index+1

        table.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myVentana = LoginForm()
    myVentana.show()
    sys.exit(app.exec_())


# Cargar nuestro archivo .ui
