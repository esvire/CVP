# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AjustesDeCLiente.ui'
#
# Created: Sun Aug 23 20:53:54 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AjusteDeClientes(object):
    def setupUi(self, AjusteDeClientes):
        AjusteDeClientes.setObjectName(_fromUtf8("AjusteDeClientes"))
        AjusteDeClientes.resize(431, 485)
        AjusteDeClientes.setMinimumSize(QtCore.QSize(431, 485))
        AjusteDeClientes.setMaximumSize(QtCore.QSize(430, 485))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../cvp_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AjusteDeClientes.setWindowIcon(icon)
        self.btnCerrar = QtGui.QPushButton(AjusteDeClientes)
        self.btnCerrar.setGeometry(QtCore.QRect(100, 340, 100, 30))
        self.btnCerrar.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.btnCerrar.setFont(font)
        self.btnCerrar.setObjectName(_fromUtf8("btnCerrar"))
        self.label = QtGui.QLabel(AjusteDeClientes)
        self.label.setGeometry(QtCore.QRect(80, 10, 251, 40))
        self.label.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnActualizarCliente = QtGui.QPushButton(AjusteDeClientes)
        self.btnActualizarCliente.setGeometry(QtCore.QRect(210, 340, 100, 30))
        self.btnActualizarCliente.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.btnActualizarCliente.setFont(font)
        self.btnActualizarCliente.setObjectName(_fromUtf8("btnActualizarCliente"))
        self.label_6 = QtGui.QLabel(AjusteDeClientes)
        self.label_6.setGeometry(QtCore.QRect(90, 50, 260, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(260, 30))
        self.label_6.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.widget = QtGui.QWidget(AjusteDeClientes)
        self.widget.setGeometry(QtCore.QRect(10, 90, 406, 227))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnConsultaDocumento = QtGui.QPushButton(self.widget)
        self.btnConsultaDocumento.setMinimumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.btnConsultaDocumento.setFont(font)
        self.btnConsultaDocumento.setObjectName(_fromUtf8("btnConsultaDocumento"))
        self.horizontalLayout_5.addWidget(self.btnConsultaDocumento)
        spacerItem = QtGui.QSpacerItem(115, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.txtBuscarDocumento = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.txtBuscarDocumento.sizePolicy().hasHeightForWidth())
        self.txtBuscarDocumento.setSizePolicy(sizePolicy)
        self.txtBuscarDocumento.setMinimumSize(QtCore.QSize(150, 30))
        self.txtBuscarDocumento.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtBuscarDocumento.setFont(font)
        self.txtBuscarDocumento.setText(_fromUtf8(""))
        self.txtBuscarDocumento.setObjectName(_fromUtf8("txtBuscarDocumento"))
        self.horizontalLayout_5.addWidget(self.txtBuscarDocumento)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(110, 30))
        self.label_2.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.txtNombre = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.txtNombre.sizePolicy().hasHeightForWidth())
        self.txtNombre.setSizePolicy(sizePolicy)
        self.txtNombre.setMinimumSize(QtCore.QSize(150, 30))
        self.txtNombre.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtNombre.setFont(font)
        self.txtNombre.setText(_fromUtf8(""))
        self.txtNombre.setObjectName(_fromUtf8("txtNombre"))
        self.horizontalLayout.addWidget(self.txtNombre)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(110, 30))
        self.label_3.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.txtApellido = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.txtApellido.sizePolicy().hasHeightForWidth())
        self.txtApellido.setSizePolicy(sizePolicy)
        self.txtApellido.setMinimumSize(QtCore.QSize(150, 30))
        self.txtApellido.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtApellido.setFont(font)
        self.txtApellido.setText(_fromUtf8(""))
        self.txtApellido.setObjectName(_fromUtf8("txtApellido"))
        self.horizontalLayout_2.addWidget(self.txtApellido)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(110, 30))
        self.label_4.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem3 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.txtTlefono = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.txtTlefono.sizePolicy().hasHeightForWidth())
        self.txtTlefono.setSizePolicy(sizePolicy)
        self.txtTlefono.setMinimumSize(QtCore.QSize(150, 30))
        self.txtTlefono.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtTlefono.setFont(font)
        self.txtTlefono.setText(_fromUtf8(""))
        self.txtTlefono.setObjectName(_fromUtf8("txtTlefono"))
        self.horizontalLayout_3.addWidget(self.txtTlefono)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(125, 30))
        self.label_5.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem4 = QtGui.QSpacerItem(110, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.txtDireccion = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.txtDireccion.sizePolicy().hasHeightForWidth())
        self.txtDireccion.setSizePolicy(sizePolicy)
        self.txtDireccion.setMinimumSize(QtCore.QSize(150, 30))
        self.txtDireccion.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtDireccion.setFont(font)
        self.txtDireccion.setText(_fromUtf8(""))
        self.txtDireccion.setObjectName(_fromUtf8("txtDireccion"))
        self.horizontalLayout_4.addWidget(self.txtDireccion)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(120, 30))
        self.label_7.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem5 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.comboEstado = QtGui.QComboBox(self.widget)
        self.comboEstado.setMinimumSize(QtCore.QSize(150, 0))
        self.comboEstado.setObjectName(_fromUtf8("comboEstado"))
        self.comboEstado.addItem(_fromUtf8(""))
        self.comboEstado.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboEstado)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(AjusteDeClientes)
        QtCore.QMetaObject.connectSlotsByName(AjusteDeClientes)

    def retranslateUi(self, AjusteDeClientes):
        AjusteDeClientes.setWindowTitle(_translate("AjusteDeClientes", "Ajustes de clientes", None))
        self.btnCerrar.setToolTip(_translate("AjusteDeClientes", "Cerrar ventana", None))
        self.btnCerrar.setText(_translate("AjusteDeClientes", "&Cerrar", None))
        self.btnCerrar.setShortcut(_translate("AjusteDeClientes", "Ctrl+C", None))
        self.label.setText(_translate("AjusteDeClientes", "Ajustes de clientes", None))
        self.btnActualizarCliente.setToolTip(_translate("AjusteDeClientes", "Actualizar datos del Cliente", None))
        self.btnActualizarCliente.setText(_translate("AjusteDeClientes", "&Actualizar", None))
        self.btnActualizarCliente.setShortcut(_translate("AjusteDeClientes", "Ctrl+A", None))
        self.label_6.setText(_translate("AjusteDeClientes", "Buscar cliente por documento", None))
        self.btnConsultaDocumento.setToolTip(_translate("AjusteDeClientes", "Consultar Cliente", None))
        self.btnConsultaDocumento.setText(_translate("AjusteDeClientes", "Buscar", None))
        self.btnConsultaDocumento.setShortcut(_translate("AjusteDeClientes", "Return", None))
        self.txtBuscarDocumento.setToolTip(_translate("AjusteDeClientes", "Ingrese Documento del Cliente", None))
        self.label_2.setText(_translate("AjusteDeClientes", "Nombre", None))
        self.txtNombre.setToolTip(_translate("AjusteDeClientes", "Ingrese Nombre del Cliente", None))
        self.label_3.setText(_translate("AjusteDeClientes", "Apellidos", None))
        self.txtApellido.setToolTip(_translate("AjusteDeClientes", "Ingrese Apellidos del Cliente", None))
        self.label_4.setText(_translate("AjusteDeClientes", "Teléfono", None))
        self.txtTlefono.setToolTip(_translate("AjusteDeClientes", "Ingrese Teléfono del Cliente", None))
        self.label_5.setText(_translate("AjusteDeClientes", "Documento", None))
        self.txtDireccion.setToolTip(_translate("AjusteDeClientes", "Ingrese Dirección del Cliente", None))
        self.label_7.setText(_translate("AjusteDeClientes", "Estado", None))
        self.comboEstado.setToolTip(_translate("AjusteDeClientes", "Estado del cliente", None))
        self.comboEstado.setItemText(0, _translate("AjusteDeClientes", "Inactivo", None))
        self.comboEstado.setItemText(1, _translate("AjusteDeClientes", "Activo", None))

