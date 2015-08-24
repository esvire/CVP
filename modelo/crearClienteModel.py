__author__ = 'paladin'
import sys
from vista.vtnCrearCliente import *
from conector import *

class crearCliente(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_crearCliente()
        self.ui.setupUi(self)
        self.coneccion = conexion()

        QtCore.QObject.connect(self.ui.btnCrearCliente, QtCore.SIGNAL("clicked()"), self.insertarCliente)
        QtCore.QObject.connect(self.ui.btnCerrar, QtCore.SIGNAL("clicked()"), self.cerrarVentana)

    def cerrarVentana(self):
        self.close()
        return

    def esNumero(self, valor = str):
        es_Numero = any(char.isdigit() for char in valor)
        return es_Numero

    def insertarCliente(self):
        nombres = str(self.ui.txtNombre.text())
        apellidos = str(self.ui.txtApellido.text())
        documento = str(self.ui.txtDireccion.text())
        telefono = str(self.ui.txtTlefono.text())

        self.coneccion.abrirConexio()
        sqlUno = "call listarUnCliente('"+documento+"')"
        consultaUno = QSqlQueryModel()
        consultaUno.setQuery(sqlUno)
        respuestaUno = consultaUno.record(0)
        documentoRepetido = str(respuestaUno.value(3))
        print("Document0:"+documentoRepetido)
        self.coneccion.cerrarConexion()

        if nombres == "":
            QtGui.QMessageBox.information(self, "Campo faltante", "Ingrese nombre(s) del cliente.")
            return
        elif self.esNumero(nombres):
            QtGui.QMessageBox.information(self, "Campo Incorrecto", "Ingrese solo letras en nombre del cliente.")
            return
        elif apellidos == "":
            QtGui.QMessageBox.information(self, "Campo faltante", "Ingrese apellidos del cliente.")
            return
        elif self.esNumero(apellidos):
            QtGui.QMessageBox.information(self, "Campo Incorrecto", "Ingrese solo letras en apellido del cliente.")
            return
        elif telefono == "":
            QtGui.QMessageBox.information(self, "Campo faltante", "Ingrese teléfon del cliente.")
            return
        elif documento == "":
            QtGui.QMessageBox.information(self, "Campo faltante", "Ingrese número de documneto del cliente.")
            return
        elif documento == documentoRepetido :
            QtGui.QMessageBox.information(self, "Campo Incorrecto", "El numero de documento ya se encuentra registrado en el sistema.")
            return
        else:
            self.coneccion.abrirConexio()
            sql = "call crearCliente(:nombre, :apellido, :documento, :telefono)"
            inserccion = QSqlQuery()
            inserccion.prepare(sql)
            inserccion.bindValue(":nombre", nombres)
            inserccion.bindValue(":apellido", apellidos)
            inserccion.bindValue(":documento", documento)
            inserccion.bindValue(":telefono", telefono)
            aceptar = QtGui.QMessageBox.question(self, "Aceptar los cambios",
                                            "Realmente desea crear el cliente con nombre: "+nombres+"",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.No)
            if aceptar == QtGui.QMessageBox.Yes:
                try:
                    if inserccion.exec_():
                        QtGui.QMessageBox.information(self,"Correcto", "Datos del cliente "+nombres+" ingresados con exito!")
                        self.coneccion.cerrarConexion()
                    else:
                        QtGui.QMessageBox.information(self,"Error", "No se insertaron los datos del cliente!!!")
                        print("Error: "+inserccion.lastError().text())
                        self.coneccion.cerrarConexion()
                except:
                    print("Error: " + inserccion.lastError().text())
            else:
                print("Alerta: no se preciono el boton yes")


