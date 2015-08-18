__author__ = 'paladin'
import sys
from vista.vtnServicioDeAlquiler import *
from PyQt4.QtCore import *
from PyQt4.QtGui import  *

import datetime
from conector import *
#from loginModel import *
from modelo.crearUsuarioModel import crearUsuario
from modelo.perfilUsuario import perfilDeUsuario
from modelo.ajustesModel import ajustesDeParqueadero

class servicioDeAlqioler(QtGui.QMainWindow):
    def __init__(self, id_USR,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.usr = id_USR
        self._rol_ = str
        self._nombre_ = str
        self.nombreDeParqueadero()
        self.listarUsuario()

        self.ui.actionPerfil.connect(self.ui.actionAjustes,SIGNAL("triggered()"), self.abrirAjustesParqueadero)
        QtCore.QObject.connect(self.ui.actionCrearUsuario, QtCore.SIGNAL("triggered()"), self.abrirCrearUsuario)
        QtCore.QObject.connect(self.ui.actionPerfil, QtCore.SIGNAL("triggered()"), self.abrirPerfil)

    def abrirPerfil(self):
        self.PerfilUsr =perfilDeUsuario(self.usr)
        self.PerfilUsr.show()

    def abrirCrearUsuario(self):
        if self._rol_ == "administrador":
            self.crearUsr = crearUsuario()
            self.crearUsr.show()
        else:
            QtGui.QMessageBox.information(self,"Acceso Denegado", "No tienes el permiso para ingresar a esta configuración!")
        return

    def listarUsuario(self):
        db = conexion()
        db.abrirConexio()
        sql = "CALL listarUnUsuario("+str(self.usr)+")"
        consulta = QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        self._nombre_ = str(resultado.value("nombre"))
        self._rol_ = str(resultado.value("tipoRol"))
        db.cerrarConexion()
        self.ui.labeNombreUsuario.setText(self._nombre_)
        self.ui.labelRol.setText(self._rol_)
        return

    def nombreDeParqueadero(self):
        db = conexion()
        db.abrirConexio()
        sql = "call listarElParquedero()"
        consulta = QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        self.ui.labelParqueadero.setText(str(resultado.value(1)))
        db.cerrarConexion()
        return

    def abrirAjustesParqueadero(self):
        if self._rol_ == "administrador":
            self.ajusteGenerales = ajustesDeParqueadero()
            self.ajusteGenerales.show()
        else:
            QtGui.QMessageBox.information(self,"Acceso Denegado", "No tienes el permiso para ingresar a esta configuración!")
        return

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    aplicacion= servicioDeAlqioler()
    aplicacion.show()
    sys.exit(app.exec_())
