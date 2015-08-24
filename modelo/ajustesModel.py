__author__ = 'paladin'
import  sys
from vista.vtnAjustes import *
from conector import *
from modelo.crearVehiculoModel import *

class ajustesDeParqueadero(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Ajustes()
        self.ui.setupUi(self)
        self.conector = conexion()
        self.listarParqueadero()
        self.listarVehiculos()
        QtCore.QObject.connect(self.ui.btnActualizarPar, QtCore.SIGNAL("clicked()"), self.modificarParqueadero)
        QtCore.QObject.connect(self.ui.btnNuevoVehiculo, QtCore.SIGNAL("clicked()"), self.abrirCrearTipoDeVehiculo)
        QtCore.QObject.connect(self.ui.btnActualizarVehiculo, QtCore.SIGNAL("clicked()"), self.modificarTipoDeVehiculo)
        self.ui.comboBox.activated[str].connect(self.mostrarUnTipoDeVehiculo)

    def listarParqueadero(self):
        self.conector.abrirConexio()
        sql = "call listarElParquedero()"
        consulta = QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        self.ui.txtNombrePar.setText(str(resultado.value(1)))
        self.ui.txtNitPar.setText(str(resultado.value(2)))
        self.ui.txtDireccion.setText(str(resultado.value(3)))
        self.ui.txtTlefono.setText(str(resultado.value(4)))
        self.conector.cerrarConexion()
        return

    def abrirCrearTipoDeVehiculo(self):
        self.crearTipoVhl = crearTipoDeVehiculo()
        self.crearTipoVhl.show()
        self.hide()
        return

    def listarVehiculos(self):
        self.conector.abrirConexio()
        sql = "call listarVehiculos()"
        consulta = QSqlQuery(sql)

        while consulta.next():
            self.ui.comboBox.addItem(str(consulta.value(1)))

        self.conector.cerrarConexion()
        return

    def mostrarUnTipoDeVehiculo(self, text):
        self.conector.abrirConexio()
        sql = "call listarUntipoVehiculoPorNombre('"+text+"')"
        consulta = QSqlQueryModel()
        consulta.setQuery(sql)
        resultado = consulta.record(0)
        print(str(resultado.value(1)))
        self.ui.labelTipoVehiculo.setText(str(resultado.value(1)))
        self.ui.spinFraccion.setValue(int(resultado.value(2)))
        self.ui.spinHora.setValue(int(resultado.value(3)))
        self.ui.spinDia.setValue(int(resultado.value(4)))
        self.ui.spinMes.setValue(int(resultado.value(5)))
        self.ui.spinEspecial.setValue(int(resultado.value(8)))
        if resultado.value(7) == 1:
            self.ui.comboEstado.setCurrentIndex(0)
        elif resultado.value(7) == 0:
            self.ui.comboEstado.setCurrentIndex(1)
        else:
            print("muy rarro!!")

        sqlDos = "call celdasPorVehiculo('"+str(text)+"')"
        consultaDos = QSqlQueryModel()
        consultaDos.setQuery(sqlDos)
        respuestaDos = consultaDos.record(0)
        self.ui.spinCeldas.setValue(int(respuestaDos.value(0)))

    def modificarTipoDeVehiculo(self):
        nombreVhl = str(self.ui.labelTipoVehiculo.text())
        fraccion = int(self.ui.spinFraccion.text())
        hora = int(self.ui.spinHora.text())
        dia = int(self.ui.spinDia.text())
        mes = int(self.ui.spinMes.text())
        especial = int(self.ui.spinEspecial.text())
        numeroCeldas = int(self.ui.spinCeldas.text())
        seleccion = int(self.ui.comboEstado.currentIndex())
        if seleccion == 0:
            estado = 1
        else:
            estado = 0
        self.conector.abrirConexio()
        sqlUno = "call listarUntipoVehiculoPorNombre('"+nombreVhl+"')"
        consultaUno = QSqlQueryModel()
        consultaUno.setQuery(sqlUno)
        respuestaUno = consultaUno.record(0)
        idTipoVehiculo = str(respuestaUno.value(0))
        print(idTipoVehiculo)
        print(nombreVhl)

        sqlDos = "call celdasOcupadasPorTipoDeVehiculo('"+idTipoVehiculo+"')"
        consultaDos = QSqlQueryModel()
        consultaDos.setQuery(sqlDos)
        respuestaDos = consultaDos.record(0)
        celdasOcupadas = int(respuestaDos.value(0))
        self.conector.cerrarConexion()

        if nombreVhl == "Veheículo":
            QtGui.QMessageBox.information(self,"Campos vacíos", "Seleccione un tipo de vehículo en el botón desplegable al lado izquierdo.")
            return
        elif numeroCeldas == 0:
            QtGui.QMessageBox.information(self,"Campos incorrecto", "El numero de celdas no puede ser igual a cero.")
            return
        elif fraccion == 0:
            QtGui.QMessageBox.information(self,"Campos incorrecto", "El Valor de la fracción no puede ser igual a cero.")
            return
        elif hora == 0:
            QtGui.QMessageBox.information(self,"Campos incorrecto", "El Valor de la hora no puede ser igual a cero.")
            return
        elif dia == 0:
            QtGui.QMessageBox.information(self,"Campos incorrecto", "El Valor del día no puede ser igual a cero.")
            return
        elif mes == 0:
            QtGui.QMessageBox.information(self,"Campos incorrecto", "El Valor del mes no puede ser igual a cero.")
            return
        elif especial == 0:
            QtGui.QMessageBox.information(self,"Campos incorrecto", "El Valor de la hora tarifa especial no puede ser igual a cero.")
            return
        elif celdasOcupadas > numeroCeldas:
            QtGui.QMessageBox.information(self,"Campos incorrecto", "El Numero de celdas no puede se inferior a el numero de celdas ocupadas.")
            return
        else:
            self.conector.abrirConexio()
            sql = "call modificarTipoDeVehiculo(:idTpVhl, :fraccion, :hora, :dia, :mes, :especial, :nCeldas, :estado)"
            insercion = QSqlQuery()
            insercion.prepare(sql)
            insercion.bindValue(":idTpVhl", idTipoVehiculo)
            insercion.bindValue(":nombre", nombreVhl)
            insercion.bindValue(":fraccion", fraccion)
            insercion.bindValue(":hora", hora)
            insercion.bindValue(":dia", dia)
            insercion.bindValue(":mes", mes)
            insercion.bindValue(":especial", especial)
            insercion.bindValue(":nCeldas", numeroCeldas)
            insercion.bindValue(":estado", estado)
            aceptar = QtGui.QMessageBox.question(self, "Aceptar los cambios",
                                            "Realmente desea guardar los cambios en el Tipo de Vehículo: "+nombreVhl+"",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.No)
            if aceptar == QtGui.QMessageBox.Yes:
                try:
                    if insercion.exec_():
                        QtGui.QMessageBox.information(self,"Correcto", "Datos de Tipo de Vehículo "+nombreVhl+" modificados con exito!")
                        self.conector.cerrarConexion()
                    else:
                        QtGui.QMessageBox.information(self,"Error", "No se modificaron los datos en tipo de vehiculo!!!" + insercion.lastError().text())
                        self.conector.cerrarConexion()
                except:
                    print("Error: " + insercion.lastError().text())
            else:
                print("Error: cambios no efectuados en tipo de vehículo")

        return

    def modificarParqueadero(self):
        nombre = str(self.ui.txtNombrePar.text())
        nit = str(self.ui.txtNitPar.text())
        telefono = str(self.ui.txtTlefono.text())
        direccion = str(self.ui.txtDireccion.text())

        if nombre == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese apellido")
            return

        if nit == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese NIT")
            return

        if telefono == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese telefono")
            return

        if direccion == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese direccion")
            return

        self.conector.abrirConexio()
        sql = "CALL modificarParqueadero(?,?,?,?)"
        query= QSqlQuery()
        query.prepare(sql)
        query.bindValue(0, nombre)
        query.bindValue(1, nit)
        query.bindValue(2, telefono)
        query.bindValue(3, direccion)
        aceptar = QtGui.QMessageBox.question(self, "Aceptar los cambios",
                                            "Realmente desea Guardar los Cambios en el Paqueadero",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.No)
        if aceptar == QtGui.QMessageBox.Yes:
            try:
                if query.exec_():
                    QtGui.QMessageBox.information(self,"Correcto", "Datos de usuario modificados con exito!")
                    self.conectar.cerrarConexion()
                else:
                    QtGui.QMessageBox.information(self,"Error", "No se modificaron los datos")
                    self.conectar.cerrarConexion()
            except:
                print("Error: "+ query.lastError().text())
        else:
            print("Error: cambios no aceptados")

        return


