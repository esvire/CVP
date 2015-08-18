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
        self.listarPaequeadero()
        self.listarVehiculos()
        QtCore.QObject.connect(self.ui.btnActualizarPar, QtCore.SIGNAL("clicked()"), self.modificarParqueadero)
        QtCore.QObject.connect(self.ui.btnNuevoVehiculo, QtCore.SIGNAL("clicked()"), self.abrirCrearTipoDeVehiculo)
        self.ui.comboBox.activated[str].connect(self.mostrarUnTipoDeVehiculo)

    def listarPaequeadero(self):
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
        #self.ui.comboBox.addItem("ubumtu")
        #self.ui.comboBox.addItem("fedora")
        #self.ui.comboBox.addItem("debian")3105334060
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
        sqlDos = "call celdasPorVehiculo('"+str(text)+"')"
        consultaDos = QSqlQueryModel()
        consultaDos.setQuery(sqlDos)
        respuestaDos = consultaDos.record(0)
        self.ui.spinCeldas.setValue(int(respuestaDos.value(0)))


    def modificarParqueadero(self):
        nombre = str(self.ui.txtNombrePar.text())
        nit = str(self.ui.txtNitPar.text())
        telefono = str(self.ui.txtTlefono.text())
        direccion = str(self.ui.txtDireccion.text())

        if nombre == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese apellido")
            return

        if nit == None:
            QtGui.QMessageBox.information(self,"Campo Vacío", "Ingrese nit")
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


