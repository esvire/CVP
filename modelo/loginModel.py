__author__ = 'paladin'
import sys
from PyQt4.QtCore import *
from PyQt4.QtSql import *
import datetime
from conector import *
from vista.vtnLogin import *
from modelo.recuperarClaveModel import *
from modelo.servicioModel import *

class loginUsuario(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QObject.connect(self.ui.btnEntrar, SIGNAL("clicked()"), self.userValidation)
        QObject.connect(self.ui.btnSalir, SIGNAL("clicked()"), self.cerrarLogin)
        QObject.connect(self.ui.btnRecordar, SIGNAL("clicked()"), self.irRecuperarClave)

    def irRecuperarClave(self):
        self.vntRecuperaclave = recuperarClave()
        self.vntRecuperaclave.show()

    def cerrarLogin(self):
        self.close();

    def userValidation(self):
        documento = str(self.ui.txtDocumento.text())
        clave = self.ui.txtClave.text()

        #conectar db
        conetar = conexion()
        conetar.abrirConexio()

        sql = "select * from tbl_usuario as US" \
              " inner join tbl_rol as RO on RO.id_rol = US.tbl_rol_id_rol" \
              " where US.documento = "+documento+" and US.clave = "+clave

        consulta = QSqlQueryModel()
        #ejecuta la conexion.
        if consulta.setQuery(sql) is None:
            self.resultado = consulta.record(0)
            self.doc = self.resultado.value("documento")
            self.clv = self.resultado.value("clave")
            # Validacion de Usuario
            if self.doc==None or self.clv== None:
                QtGui. QMessageBox.information(self,"Campos Vacíos",  "Ingrese documento o contraseña")
            elif self.doc == documento and self.clv == clave:
                self.ui.txtDocumento.setText(self.resultado.value("nombre"))
                self.ventanaPrinsipal = servicioDeAlqioler(self.resultado.value("id_usuario"))
                self.ventanaPrinsipal.show()
                self.hide()
                #self.close()

            else:
                QtGui. QMessageBox.information(self,"Correcto",  "contraseña o Documento incorrectos")
            conetar.cerrarConexion()
        else:
            print("error: ")
            QtGui.QMessageBox.warning("error", "problemas de consulta")
            conetar.cerrarConexion()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    aplicacion = loginUsuario()
    aplicacion.show()
    sys.exit(app.exec_())

