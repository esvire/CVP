__author__ = 'paladin'
from vista.vtnCambioDeSeguridad import *
from conector import *

class cambioSeguridad(QtGui.QDialog):
    def __init__(self, id_USR, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_cambioClave()
        self.ui.setupUi(self)
        self.usr = id_USR
        self.claveValida = bool
        self.coneccion = conexion()
        QtCore.QObject.connect(self.ui.btnModificarClave, QtCore.SIGNAL("clicked()"), self.modificarClave)
        QtCore.QObject.connect(self.ui.btnModificarPregunta, QtCore.SIGNAL("clicked()"), self.modificarPregunta)

    def validarClave(self, clave):
        self.coneccion.abrirConexio()
        sql1 ="CALL listarUnUsuario("+self.usr+")"
        consulta1 = QSqlQueryModel()
        consulta1.setQuery(sql1)
        resultado1 = consulta1.record(0)
        claveDB = resultado1.value("clave")
        if claveDB == clave:
            self.claveValida = True
            self.coneccion.cerrarConexion()
            return self.claveValida
        else:
            self.claveValida = False
            self.coneccion.cerrarConexion()
            return self.claveValida

    def modificarClave(self):
        claveVieja = str(self.ui.txtCLaveVieja.text())
        if claveVieja == None:
            QtGui.QMessageBox.information(self, "Campo Vacío", "ingrese Contraseña actual")
            self.ui.txtCLaveVieja.setText("")
            self.ui.txtCLaveNueva.setText("")
            self.ui.txtConCLaveNueva.setText("")
            self.coneccion.cerrarConexion()
            return

        claveNuevaUno = str(self.ui.txtCLaveNueva.text())
        claveNuevaDos = str(self.ui.txtConCLaveNueva.text())

        self.clavesIguales = bool
        if claveNuevaUno == claveNuevaDos:
            self.clavesIguales = True
        else:
            clavesIguales = False
            QtGui.QMessageBox.information(self, "Error De contraseñas", "Las contraseñas deben ser iguales!")
            self.ui.txtCLaveVieja.setText("")
            self.ui.txtCLaveNueva.setText("")
            self.ui.txtConCLaveNueva.setText("")
            self.coneccion.cerrarConexion()
            return

        self.validarClave(claveVieja)
        confirmacion = QtGui.QMessageBox.question(self, "Confirmar cambio",
                                   "Realmente desea guardar la nueva contraseña",
                                   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                   QtGui.QMessageBox.No)
        if self.claveValida and confirmacion:
            self.coneccion.abrirConexio()
            sql = "CALL modificarClave(?)"
            query = QSqlQuery()
            query.prepare(sql)
            query.bindValue(0, claveNuevaUno)
            if query.exec_() == True:
                QtGui.QMessageBox.information(self, "Modificación de contraseña", "Contraseña modificada con éxito!")
                self.ui.txtCLaveVieja.setText("")
                self.ui.txtCLaveNueva.setText("")
                self.ui.txtConCLaveNueva.setText("")
                self.coneccion.cerrarConexion()
                return
            else:
                QtGui.QMessageBox.information(self, "Modificación de contraseña", "Error al Almacenar y/o modoficar la contraseña!")
                self.ui.txtCLaveVieja.setText("")
                self.ui.txtCLaveNueva.setText("")
                self.ui.txtConCLaveNueva.setText("")
                self.coneccion.cerrarConexion()
                return
        else:
            QtGui.QMessageBox.information(self, "Modificación de contraseña", "Error al modoficar la contraseña!")
            self.ui.txtCLaveVieja.setText("")
            self.ui.txtCLaveNueva.setText("")
            self.ui.txtConCLaveNueva.setText("")
            self.coneccion.cerrarConexion()
            return

    def modificarPregunta(self):
        clave = str(self.ui.txtCLaveViejaPre.text())
        pregunta = str(self.ui.txtPregunta.text())
        respuesta = str(self.ui.txtRespuesta.text())

        if clave == "":
            QtGui.QMessageBox.warning(self, "Campo Vacío", "Ingrse contraseña")
            self.ui.txtCLaveViejaPre.setText("")
            self.ui.txtPregunta.setText("")
            self.ui.txtRespuesta.setText("")
            return
        if pregunta == "":
            QtGui.QMessageBox.warning(self, "Campo Vacío", "Ingrse pregunta")
            self.ui.txtCLaveViejaPre.setText("")
            self.ui.txtPregunta.setText("")
            self.ui.txtRespuesta.setText("")
            return
        if respuesta == "":
            QtGui.QMessageBox.warning(self, "Campo Vacío", "Ingrse respuesta")
            self.ui.txtCLaveViejaPre.setText("")
            self.ui.txtPregunta.setText("")
            self.ui.txtRespuesta.setText("")
            return

        confirmacion = QtGui.QMessageBox.question(self, "Confirmar cambio",
                                   "Realmente desea guardar la nueva contraseña",
                                   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                   QtGui.QMessageBox.No)
        self.validarClave(clave)
        if self.claveValida and confirmacion == QtGui.QMessageBox.Yes:
            self.coneccion.abrirConexio()
            sql = "CALL modificarPregunta(?,?)"
            query = QSqlQuery()
            query.prepare(sql)
            query.bindValue(0, pregunta)
            query.bindValue(1, respuesta)
            if query.exec_() == True:
                QtGui.QMessageBox.information(self, "Modificación de Pregunta", "pegunta y respuesta modificadas con éxito!")
                self.ui.txtCLaveViejaPre.setText("")
                self.ui.txtPregunta.setText("")
                self.ui.txtRespuesta.setText("")
                self.coneccion.cerrarConexion()
                return
            else:
                QtGui.QMessageBox.information(self, "Modificación de Pregunta", "Error Al insertar los cambios al sistema!")
                self.ui.txtCLaveViejaPre.setText("")
                self.ui.txtPregunta.setText("")
                self.ui.txtRespuesta.setText("")
                self.coneccion.cerrarConexion()
                return

