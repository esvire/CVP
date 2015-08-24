__author__ = 'paladin'

from vista.vtnAjustesDeCliente import *
from conector import *

class ajustesDeCliente(QtGui.QDialog):
    def __init__(self, parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AjusteDeClientes()
        self.ui.setupUi(self)
        self.coneccion = conexion()

        QtCore.QObject.connect(self.ui.btnConsultaDocumento, QtCore.SIGNAL("clicked()"), self.consultarCliente)
        QtCore.QObject.connect(self.ui.btnCerrar, QtCore.SIGNAL("clicked()"), self.cerraVentana)
        QtCore.QObject.connect(self.ui.btnActualizarCliente, QtCore.SIGNAL("clicked()"), self.modificarCliente)

    def cerraVentana(self):
        self.close()

    def consultarCliente(self):
        documento = str(self.ui.txtBuscarDocumento.text())

        if documento == "":
            QtGui.QMessageBox.information(self, "Campo faltante", "Ingrese documento del cliente.")
            return
        else:
            self.coneccion.abrirConexio()
            sql = "call listarUnCliente('"+documento+"')"
            consulta = QSqlQueryModel()
            consulta.setQuery(sql)
            resultado = consulta.record(0)

            self.ui.txtNombre.setText(str(resultado.value(1)))
            self.ui.txtApellido.setText(str(resultado.value(2)))
            self.ui.txtDireccion.setText(str(resultado.value(3)))
            self.ui.txtTlefono.setText(str(resultado.value(4)))
            estado = int(resultado.value(5))

            if estado == 0:
                self.ui.comboEstado.setCurrentIndex(estado)
            else:
                self.ui.comboEstado.setCurrentIndex(estado)

            self.coneccion.cerrarConexion()
            return

    def esNumero(self, valor = str):
        es_Numero = any(char.isdigit() for char in valor)
        return es_Numero

    def modificarCliente(self):
        nombres = str(self.ui.txtNombre.text())
        apellidos = str(self.ui.txtApellido.text())
        documento = str(self.ui.txtDireccion.text())
        telefono = str(self.ui.txtTlefono.text())
        documentoUno = str(self.ui.txtBuscarDocumento.text())
        estado = int(self.ui.comboEstado.currentIndex())

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
        elif documento == documentoRepetido and documento != documentoUno:
            QtGui.QMessageBox.information(self, "Campo Incorrecto", "El numero de documento ya se encuentra registrado en el sistema.")
            return
        else:
            self.coneccion.abrirConexio()
            sql = "call modificarCliente(:documentoUno, :nombre, :apellido, :documento, :telefono, :estado)"
            inserccion = QSqlQuery()
            inserccion.prepare(sql)
            inserccion.bindValue(":nombre", nombres)
            inserccion.bindValue(":apellido", apellidos)
            inserccion.bindValue(":documento", documento)
            inserccion.bindValue(":telefono", telefono)
            inserccion.bindValue(":documentoUno", documentoUno)
            inserccion.bindValue(":estado", estado)
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