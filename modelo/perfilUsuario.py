__author__ = 'paladin'
import sys
#from PyQt4.QtSql import *
from vista.vtnPerfilUsuario import *
from modelo.cambioSeguridaModel import *
from conector import *

_aceptaCambios = bool

class perfilDeUsuario(QtGui.QDialog):
    def __init__(self, id_usr, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_vtnAjusteUusario()
        self.ui.setupUi(self)
        self.conectar = conexion()
        self.usr = str(id_usr)
        self.listarUsuario()
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.cerrarVentana)
        QtCore.QObject.connect(self.ui.btnModificar, QtCore.SIGNAL("clicked()"), self.modificarUsuario)
        QtCore.QObject.connect(self.ui.btnCaombioClave, QtCore.SIGNAL("clicked()"), self.irCambioDeClave)

    def cerrarVentana(self):
        self.close()
        return

    def irCambioDeClave(self):
        self.cambioSeguridad = cambioSeguridad(self.usr)
        self.cambioSeguridad.show()
        return

    def listarUsuario(self):
        self.conectar.abrirConexio()
        sql = "CALL listarUnUsuario("+self.usr+")"
        consulta = QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        self.ui.txtNombre.setText(str(resultado.value("nombre")))
        self.ui.txtApellido.setText(str(resultado.value("apellido")))
        self.ui.txtTelefono.setText(str(resultado.value("telefono")))
        self.ui.txtDireccion.setText(str(resultado.value("direccion")))
        return

    def modificarUsuario(self):
        nombre = str(self.ui.txtNombre.text())
        apellido = str(self.ui.txtApellido.text())
        telefono = str(self.ui.txtTelefono.text())
        direccion = str(self.ui.txtDireccion.text())

        if nombre == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese apellido")
            return

        if apellido == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese nombre")
            return

        if telefono == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese telefono")
            return

        if direccion == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese direccion")
            return

        self.conectar.abrirConexio()
        sql = "CALL modificarUsuario(?,?,?,?,?)"
        query= QSqlQuery()
        query.prepare(sql)
        query.bindValue(0, nombre)
        query.bindValue(1, apellido)
        query.bindValue(2, telefono)
        query.bindValue(3, direccion)
        query.bindValue(4, self.usr)
        aceptar = QtGui.QMessageBox.question(self, "Aceptar los cambios",
                                            "Realmente desea Guardar los Cambios",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.No)
        if aceptar == QtGui.QMessageBox.Yes:
            try:
                if query.exec_():
                    QtGui.QMessageBox.information(self,"Correcto", "Datos de usuario modificados con exito!")
                else:
                    QtGui.QMessageBox.information(self,"Error", "No se modificaron los datos")
            except QSqlError:
                print("Error: "+ query.lastError().text())
        else:
            print("Error: cambios no aceptados")
        self.conectar.cerrarConexion()
        return

