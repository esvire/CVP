__author__ = 'paladin'
from PyQt4.QtSql import *

class conexion():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")


    def abrirConexio(self):
        self.db.setHostName("localhost")
        self.db.setDatabaseName("db_CVP")
        self.db.setUserName("root")
        self.db.setPassword("12345")
        self.db.open()
        print(self.db.lastError().text())

    def cerrarConexion(self):
        self.db.close()