__author__ = 'paladin'
import sys
from conector import *

sys.path.append('../vista')
from vista.vtnCrearVehiculo import *
from modelo.ajustesModel import *


class crearTipoDeVehiculo(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CrearTipoVehiculo()
        self.ui.setupUi(self)
        self.conector = conexion()
        QtCore.QObject.connect(self.ui.btnCerrar, QtCore.SIGNAL("clicked()"), self.cerrarVentana)
        QtCore.QObject.connect(self.ui.btnCrearVh, QtCore.SIGNAL("clicked()"), self.insertarTipoDeVehiculo)

    def cerrarVentana(self):
        # self.ajusteGenerales = ajustesDeParqueadero()
        # self.ajusteGenerales.show()
        self.close()
        return

    def insertarTipoDeVehiculo(self):
        nombreVhl = str(self.ui.txtNombreVh.text())
        fraccion = int(self.ui.spinFraccion.text())
        hora = int(self.ui.spinHora.text())
        dia = int(self.ui.spinDia.text())
        mes = int(self.ui.spinMes.text())
        especial = int(self.ui.spinEspecial.text())
        numeroCeldas = int(self.ui.spinCeldas.text())

        if nombreVhl == "":
            QtGui.QMessageBox.information(self, "Campo faltante", "Ingrese nombre del tipo de vehículo.")
            return

        if numeroCeldas <= 0:
            QtGui.QMessageBox.information(self, "Campo faltante", "Ingrese numero de celdas superior a 0!")
            return

        self.conector.abrirConexio()

        sqluno = "call validarTipoDeVehiculo('" + nombreVhl + "')"
        query = QSqlQueryModel()
        query.setQuery(sqluno)
        resultado = query.record(0)

        if nombreVhl == str(resultado.value(0)):
            QtGui.QMessageBox.information(self, "Registro Duplicado",
                                          "El tipo de vehiculo '" + nombreVhl + "' ya existe !")
            return
        else:
            sql = "call insertarTipoDeVehiculo(:nombre, :fraccion, :hora, :dia, :mes, :especial, :nCeldas)"
            inserccion = QSqlQuery()
            inserccion.prepare(sql)
            inserccion.bindValue(":nombre", nombreVhl)
            inserccion.bindValue(":fraccion", fraccion)
            inserccion.bindValue(":hora", hora)
            inserccion.bindValue(":dia", dia)
            inserccion.bindValue(":mes", mes)
            inserccion.bindValue(":especial", especial)
            inserccion.bindValue(":nCeldas", numeroCeldas)

        if inserccion.exec_():
            QtGui.QMessageBox.information(self, "Crear Tipo Vehículo",
                                          "Tipo de vehículo creado con éxito. (reinicie el programa para visualizar los cambios en la ventana principal)")
        else:
            QtGui.QMessageBox.information(self, "Crear Tipo Vehículo", "Error En La Base de Datos!!!")
