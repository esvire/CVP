__author__ = 'paladin'
import sys
from PyQt4.QtSql import *
from PyQt4.QtGui import *
from vista.vtnAjustesDeOperario import *
from conector import conexion

class ajustesDeUsaurio(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AjusteDeOperario()
        self.ui.setupUi(self)
        self.coneccion = conexion()
        self.listarNombres()
        self.doc = str
        self.docAct = str
        QtCore.QObject.connect(self.ui.btnCrear, QtCore.SIGNAL("clicked()"), self.modificarUsuario)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.cerrarVentana)
        self.ui.comboNombre.activated[str].connect(self.mostrarUnUsuario)
        #self.ui.comboEstado.itemData(self.ui.comboEstado.currentIndex(), QtCore.Qt.UserRole)

    def listarNombres(self):
        self.coneccion.abrirConexio()
        sql = "call listarOperarios()"
        consulta = QSqlQuery(sql)

        while consulta.next():
            self.ui.comboNombre.addItem(str(consulta.value(3)))

        self.coneccion.cerrarConexion()
        return

    def mostrarUnUsuario(self, text):
        self.coneccion.abrirConexio()
        sql = "CALL listarUsuarioPorDocumento('"+text+"')"
        consulta = QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        self.docAct = str(resultado.value(3))
        self.ui.txtNombre.setText(str(resultado.value(1)))
        self.ui.txtApellido.setText(str(resultado.value(2)))
        self.ui.txtDocumento.setText(str(resultado.value(3)))
        self.ui.txtTelefono.setText(str(resultado.value(5)))
        self.ui.txtDireccion.setText(str(resultado.value(4)))
        self.ui.txtClave.setText(str(resultado.value(6)))
        self.ui.txtPregunta.setText(str(resultado.value(7)))
        self.ui.txtRespuesta.setText(str(resultado.value(8)))
        estado = resultado.value(9)
        if estado == 0:
            self.ui.comboEstado.setCurrentIndex(estado)
        elif estado == 1:
            self.ui.comboEstado.setCurrentIndex(estado)
        else:
            print("muy rarro!!")

    def cerrarVentana(self):
        self.close()

    def validarDocumento(self, doc = str):
        sql= "CALL validarUnicoDocumento("+doc+")"
        consulta = QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        if resultado.value(0) == doc:
            self.doc = resultado.value(0)
            return False
        else:
            return True

    def modificarUsuario(self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        documento = self.ui.txtDocumento.text()
        clave = self.ui.txtClave.text()
        conClave = self.ui.txtConClave.text()
        telefono = self.ui.txtTelefono.text()
        direccion = self.ui.txtDireccion.text()
        pregunta = self.ui.txtPregunta.text()
        respuesta = self.ui.txtRespuesta.text()
        estado = self.ui.comboEstado.currentIndex()

        self.coneccion.abrirConexio()

        repiteDoc = self.validarDocumento(documento)

        if nombre == "":
            QMessageBox.information(self,"campo faltante", "Ingrese Nombre!")
            return
        else:
            EsNumero = any(char.isdigit() for char in nombre)
            if EsNumero:
                QMessageBox.information(self,"campo Herrado", "Ingrese solo letras en campo Nombre..    hay numeros!")
                return

        if apellido == "":
            QMessageBox.information(self,"campo faltante", "Ingrese Apellido!")
            return
        else:
            EsNumero = any(char.isdigit() for char in nombre)
            if EsNumero:
                QMessageBox.information(self,"campo Herrado", "solo letras en campo Apellido..    hay numeros!")
                return

        if documento == "":
            QMessageBox.information(self,"campo faltante", "Ingrese Documento!")
            return
        elif repiteDoc == False and documento != self.doc:
            QMessageBox.information(self,"campo Herrado", "El documento ya esta registrado en la base de datos")
            return
        else:
            noEsNumero = any(char.isdigit() for char in nombre)
            if noEsNumero:
                QMessageBox.information(self,"campo Herrado", "solo numeros en el campo Documento..    hay letras!")
                return

        if telefono == "":
            QMessageBox.information(self,"campo faltante", "Ingrese Teléfono!")
            return
        else:
            esNumero = any(char.isdigit() for char in nombre)
            if esNumero :
                QMessageBox.information(self,"campo Herrado", "solo Numeros en el campo Teléfono..    hay letras!")
                return

        if direccion == "":
            QMessageBox.information(self,"campo faltante", "Ingrese Dirección!")
            return

        if clave == "":
            QMessageBox.information(self,"campo faltante", "Ingrese Contraseña!")
            return

        if pregunta == "":
            QMessageBox.information(self,"campo faltante", "Ingrese Pregunta!")
            return

        if respuesta == "":
            QMessageBox.information(self,"campo faltante", "Ingrese Respuesta!")
            return

        if clave != conClave:
            QMessageBox.information(self,"Contraseña Incorecta", "Las Dos Contraseñas deben ser iguales")
            return
        else:
            aceptar = QtGui.QMessageBox.question(self, "Aceptar los cambios",
                                            "Realmente desea modificar el Operario con nombre: "+nombre+"",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.No)
            if aceptar == QtGui.QMessageBox.Yes:
                sql = "CALL modificarUsuarioCompleto(:idActual, :nombre, :apellido, :documento, :direccion, :telefono, :clave, :pregunta, :respuesta, :estado)"
                consulta = QSqlQuery()
                consulta.prepare(sql)
                consulta.bindValue(":idActual", self.docAct)
                consulta.bindValue(":nombre", nombre)
                consulta.bindValue(":apellido", apellido)
                consulta.bindValue(":documento", documento)
                consulta.bindValue(":telefono", telefono)
                consulta.bindValue(":direccion", direccion)
                consulta.bindValue(":clave", clave)
                consulta.bindValue(":pregunta", pregunta)
                consulta.bindValue(":respuesta", respuesta)
                consulta.bindValue(":estado", estado)

                if consulta.exec_():
                    print("bien... Guardo")
                    self.ui.txtNombre.setText("")
                    self.ui.txtApellido.setText("")
                    self.ui.txtDocumento.setText("")
                    self.ui.txtClave.setText("")
                    self.ui.txtDireccion.setText("")
                    self.ui.txtTelefono.setText("")
                    self.ui.txtRespuesta.setText("")
                    self.ui.txtPregunta.setText("")
                    self.ui.txtConClave.setText("")

                    QMessageBox.information(self,"Correcto", "Operario Modificado con exito!")
                    self.coneccion.cerrarConexion()

                else:
                    QMessageBox.information(self, "Error", "no guardor"+consulta.lastError().text())
                    print("fallo la insercion")
                    self.coneccion.cerrarConexion()