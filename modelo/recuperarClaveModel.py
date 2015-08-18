__author__ = 'paladin'
import sys
#from PyQt4.QtSql import *
from vista.vtnRecuperarClave import *
from conector import *
class recuperarClave(QtGui.QDialog):
    _doc= str
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_RecuperacionClave()
        self.ui.setupUi(self)
        self.conectar = conexion()
        QtCore.QObject.connect(self.ui.btnCancelar, QtCore.SIGNAL("clicked()"), self.cerrarVentana)
        QtCore.QObject.connect(self.ui.btnConsultarDoc, QtCore.SIGNAL("clicked()"), self.consultarPregunta)
        QtCore.QObject.connect(self.ui.btnConsultar, QtCore.SIGNAL("clicked()"), self.validarRespusta)

    def cerrarVentana(self):
        self.close()

    def consultarPregunta(self):
        doc = str(self.ui.txtDocumento.text())
        self._doc=doc
        self.conectar.abrirConexio()
        sql = "CALL listarUnaPregunta("+doc+")"
        consulta =QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        pregunta= str(resultado.value(0))
        if pregunta == None:
            QtGui.QMessageBox.information(self, "Campo Vacío", "Ingrese Un documento")
            vacio=""
            self.conectar.cerrarConexion()
        else:
            self.ui.textPregunta.setText(pregunta)
            self.conectar.cerrarConexion()

    def validarRespusta(self):
        self.res = str(self.ui.txtRespuesta.text())
        doc = self._doc
        sql2 = "CALL listarUnaRespuestas("+doc+")"
        self.conectar.abrirConexio()
        consulta2 = QSqlQueryModel()
        consulta2.setQuery(sql2)
        resultado2 = consulta2.record(0)
        clave = str(resultado2.value(1))
        self.respuesta = str(resultado2.value(0))

        if doc == "":
            QtGui.QMessageBox.information(self, "Error De ingreso", "Primero consulte una cédula  correcta")
            self.conectar.cerrarConexion()
            return

        if self.respuesta == None:
            QtGui.QMessageBox.information(self, "Campo Vacío", "Ingrese Una Respuesta")
            print("doc es: "+self.doc)
            print("la clave es: "+clave)
            print("la res es: "+self.respuesta)
            self.conectar.cerrarConexion()
            return
        elif self.respuesta == self.res:
             QtGui.QMessageBox.information(self, "Respuesta correcta", "Su Contraseña es: " + clave)
             self.conectar.cerrarConexion()
             self.close()
        else:
            print("la clave es: "+clave)
            print("la res es: "+self.respuesta)
            print("doc es: "+doc)
            QtGui.QMessageBox.information(self, "Error De ingreso", "La respuesta es incorrecta")
            self.conectar.cerrarConexion()
            return

