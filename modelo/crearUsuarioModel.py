__author__ = 'paladin'
from PyQt4.QtSql import *
from PyQt4.QtGui import *
from vista.vtnCrearUsuario import *


def crearConexion():
    return True

class crearUsuario(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_vtnCrearUsuario()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnCrear, QtCore.SIGNAL("clicked()"), self.insertUsuario)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.cerrarVentana)

    def cerrarVentana(self):
        self.close()

    def validarDocumento(doc = str):
        sql= "CALL validarUnicoDocumento("+doc+")"
        consulta = QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        if resultado.value(0) == doc:
            return False
        else:
            return True

    def insertUsuario(self):

        if crearConexion() == False:
            QMessageBox.Warning(self, "Error", "MUY RARO!!!!!",  self.QMessageBox.Discard)
        else:

            nombre = self.ui.txtNombre.text()
            apellido = self.ui.txtApellido.text()
            documento = self.ui.txtDocumento.text()
            clave = self.ui.txtClave.text()
            conClave = self.ui.txtConClave.text()
            telefono = self.ui.txtTelefono.text()
            direccion = self.ui.txtDireccion.text()
            pregunta = self.ui.txtPregunta.text()
            respuesta = self.ui.txtRespuesta.text()

            db = QSqlDatabase.addDatabase("QMYSQL")
            db.setHostName("localhost")
            db.setDatabaseName("db_CVP")
            db.setUserName("root")
            db.setPassword("12345")
            db.open()
            print(db.lastError().text())

            repiteDoc = crearUsuario.validarDocumento(documento)

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
            elif repiteDoc == False:
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
                sql = "INSERT INTO tbl_usuario(nombre, apellido, documento, direccion, telefono, clave, pregunta, respuesta, tbl_rol_id_rol) VALUES (:nombre, :apellido, :documento, :direccion, :telefono, :clave, :pregunta, :respuesta,  2)"
                consulta = QSqlQuery()
                consulta.prepare(sql)
                consulta.bindValue(":nombre", nombre)
                consulta.bindValue(":apellido", apellido)
                consulta.bindValue(":documento", documento)
                consulta.bindValue(":telefono", telefono)
                consulta.bindValue(":direccion", direccion)
                consulta.bindValue(":clave", clave)
                consulta.bindValue(":pregunta", pregunta)
                consulta.bindValue(":respuesta", respuesta)

                if consulta.exec_() == True:
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

                    QMessageBox.information(self,"Correcto", "Operario Registrado con exito!")
                    db.close()

                else:
                    QMessageBox.information(self, "Error", "no guardor"+db.lastErro().text())
                    print("fallo la insercion")
                    db.close()

