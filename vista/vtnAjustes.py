# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ajustes.ui'
#
# Created: Wed Aug 12 23:43:42 2015
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

class Ui_Ajustes(object):
    def setupUi(self, Ajustes):
        Ajustes.setObjectName(_fromUtf8("Ajustes"))
        Ajustes.resize(565, 410)
        Ajustes.setMinimumSize(QtCore.QSize(565, 410))
        Ajustes.setMaximumSize(QtCore.QSize(565, 410))
        self.tabWidget = QtGui.QTabWidget(Ajustes)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 541, 381))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabPar = QtGui.QWidget()
        self.tabPar.setObjectName(_fromUtf8("tabPar"))
        self.label = QtGui.QLabel(self.tabPar)
        self.label.setGeometry(QtCore.QRect(80, 30, 400, 40))
        self.label.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(self.tabPar)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 140, 394, 32))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
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
        spacerItem = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.txtNitPar = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.txtNitPar.sizePolicy().hasHeightForWidth())
        self.txtNitPar.setSizePolicy(sizePolicy)
        self.txtNitPar.setMinimumSize(QtCore.QSize(150, 30))
        self.txtNitPar.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtNitPar.setFont(font)
        self.txtNitPar.setText(_fromUtf8(""))
        self.txtNitPar.setObjectName(_fromUtf8("txtNitPar"))
        self.horizontalLayout_2.addWidget(self.txtNitPar)
        self.layoutWidget_2 = QtGui.QWidget(self.tabPar)
        self.layoutWidget_2.setGeometry(QtCore.QRect(80, 190, 394, 32))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget_2)
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
        spacerItem1 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.txtTlefono = QtGui.QLineEdit(self.layoutWidget_2)
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
        self.layoutWidget_3 = QtGui.QWidget(self.tabPar)
        self.layoutWidget_3.setGeometry(QtCore.QRect(80, 240, 394, 32))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(110, 30))
        self.label_5.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.txtDireccion = QtGui.QLineEdit(self.layoutWidget_3)
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
        self.btnActualizarPar = QtGui.QPushButton(self.tabPar)
        self.btnActualizarPar.setGeometry(QtCore.QRect(200, 290, 120, 30))
        self.btnActualizarPar.setMinimumSize(QtCore.QSize(120, 30))
        self.btnActualizarPar.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.btnActualizarPar.setFont(font)
        self.btnActualizarPar.setObjectName(_fromUtf8("btnActualizarPar"))
        self.layoutWidget1 = QtGui.QWidget(self.tabPar)
        self.layoutWidget1.setGeometry(QtCore.QRect(81, 90, 394, 32))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
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
        spacerItem3 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.txtNombrePar = QtGui.QLineEdit(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.txtNombrePar.sizePolicy().hasHeightForWidth())
        self.txtNombrePar.setSizePolicy(sizePolicy)
        self.txtNombrePar.setMinimumSize(QtCore.QSize(150, 30))
        self.txtNombrePar.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtNombrePar.setFont(font)
        self.txtNombrePar.setText(_fromUtf8(""))
        self.txtNombrePar.setObjectName(_fromUtf8("txtNombrePar"))
        self.horizontalLayout.addWidget(self.txtNombrePar)
        self.tabWidget.addTab(self.tabPar, _fromUtf8(""))
        self.tabVheiculo = QtGui.QWidget()
        self.tabVheiculo.setObjectName(_fromUtf8("tabVheiculo"))
        self.comboBox = QtGui.QComboBox(self.tabVheiculo)
        self.comboBox.setGeometry(QtCore.QRect(10, 120, 120, 35))
        self.comboBox.setMinimumSize(QtCore.QSize(120, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_6 = QtGui.QLabel(self.tabVheiculo)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.layoutWidget_5 = QtGui.QWidget(self.tabVheiculo)
        self.layoutWidget_5.setGeometry(QtCore.QRect(150, 170, 380, 36))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_10 = QtGui.QLabel(self.layoutWidget_5)
        self.label_10.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.spinHora = QtGui.QSpinBox(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.spinHora.setFont(font)
        self.spinHora.setMaximum(999999)
        self.spinHora.setObjectName(_fromUtf8("spinHora"))
        self.horizontalLayout_10.addWidget(self.spinHora)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_15 = QtGui.QLabel(self.layoutWidget_5)
        self.label_15.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_12.addWidget(self.label_15)
        self.spinEspecial = QtGui.QSpinBox(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.spinEspecial.setFont(font)
        self.spinEspecial.setMaximum(999999)
        self.spinEspecial.setObjectName(_fromUtf8("spinEspecial"))
        self.horizontalLayout_12.addWidget(self.spinEspecial)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_12)
        self.layoutWidget_7 = QtGui.QWidget(self.tabVheiculo)
        self.layoutWidget_7.setGeometry(QtCore.QRect(150, 220, 380, 36))
        self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_11 = QtGui.QLabel(self.layoutWidget_7)
        self.label_11.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_14.addWidget(self.label_11)
        self.spinDia = QtGui.QSpinBox(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.spinDia.setFont(font)
        self.spinDia.setMaximum(999999)
        self.spinDia.setObjectName(_fromUtf8("spinDia"))
        self.horizontalLayout_14.addWidget(self.spinDia)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_16 = QtGui.QLabel(self.layoutWidget_7)
        self.label_16.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_15.addWidget(self.label_16)
        self.spinCeldas = QtGui.QSpinBox(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.spinCeldas.setFont(font)
        self.spinCeldas.setMaximum(999999)
        self.spinCeldas.setObjectName(_fromUtf8("spinCeldas"))
        self.horizontalLayout_15.addWidget(self.spinCeldas)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_15)
        self.btnActualizarVehiculo = QtGui.QPushButton(self.tabVheiculo)
        self.btnActualizarVehiculo.setGeometry(QtCore.QRect(10, 170, 120, 30))
        self.btnActualizarVehiculo.setMinimumSize(QtCore.QSize(120, 30))
        self.btnActualizarVehiculo.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.btnActualizarVehiculo.setFont(font)
        self.btnActualizarVehiculo.setObjectName(_fromUtf8("btnActualizarVehiculo"))
        self.btnNuevoVehiculo = QtGui.QPushButton(self.tabVheiculo)
        self.btnNuevoVehiculo.setGeometry(QtCore.QRect(10, 220, 120, 30))
        self.btnNuevoVehiculo.setMinimumSize(QtCore.QSize(120, 30))
        self.btnNuevoVehiculo.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.btnNuevoVehiculo.setFont(font)
        self.btnNuevoVehiculo.setObjectName(_fromUtf8("btnNuevoVehiculo"))
        self.label_7 = QtGui.QLabel(self.tabVheiculo)
        self.label_7.setGeometry(QtCore.QRect(30, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tabVheiculo)
        self.label_8.setGeometry(QtCore.QRect(250, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.labelTipoVehiculo = QtGui.QLabel(self.tabVheiculo)
        self.labelTipoVehiculo.setGeometry(QtCore.QRect(290, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.labelTipoVehiculo.setFont(font)
        self.labelTipoVehiculo.setObjectName(_fromUtf8("labelTipoVehiculo"))
        self.layoutWidget2 = QtGui.QWidget(self.tabVheiculo)
        self.layoutWidget2.setGeometry(QtCore.QRect(150, 120, 380, 36))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_9 = QtGui.QLabel(self.layoutWidget2)
        self.label_9.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.spinFraccion = QtGui.QSpinBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.spinFraccion.setFont(font)
        self.spinFraccion.setToolTip(_fromUtf8(""))
        self.spinFraccion.setMaximum(999999)
        self.spinFraccion.setObjectName(_fromUtf8("spinFraccion"))
        self.horizontalLayout_6.addWidget(self.spinFraccion)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_14 = QtGui.QLabel(self.layoutWidget2)
        self.label_14.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_11.addWidget(self.label_14)
        self.spinMes = QtGui.QSpinBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.spinMes.setFont(font)
        self.spinMes.setMaximum(999999)
        self.spinMes.setObjectName(_fromUtf8("spinMes"))
        self.horizontalLayout_11.addWidget(self.spinMes)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tabVheiculo, _fromUtf8(""))
        self.tabRegimen = QtGui.QWidget()
        self.tabRegimen.setObjectName(_fromUtf8("tabRegimen"))
        self.label_18 = QtGui.QLabel(self.tabRegimen)
        self.label_18.setGeometry(QtCore.QRect(80, 30, 360, 40))
        self.label_18.setMinimumSize(QtCore.QSize(360, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.layoutWidget3 = QtGui.QWidget(self.tabRegimen)
        self.layoutWidget3.setGeometry(QtCore.QRect(90, 90, 112, 68))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_21 = QtGui.QLabel(self.layoutWidget3)
        self.label_21.setMinimumSize(QtCore.QSize(110, 30))
        self.label_21.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout.addWidget(self.label_21)
        self.dateInicio = QtGui.QDateEdit(self.layoutWidget3)
        self.dateInicio.setMinimumSize(QtCore.QSize(100, 30))
        self.dateInicio.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.dateInicio.setFont(font)
        self.dateInicio.setObjectName(_fromUtf8("dateInicio"))
        self.verticalLayout.addWidget(self.dateInicio)
        self.layoutWidget_12 = QtGui.QWidget(self.tabRegimen)
        self.layoutWidget_12.setGeometry(QtCore.QRect(310, 90, 112, 68))
        self.layoutWidget_12.setObjectName(_fromUtf8("layoutWidget_12"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_22 = QtGui.QLabel(self.layoutWidget_12)
        self.label_22.setMinimumSize(QtCore.QSize(110, 30))
        self.label_22.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_2.addWidget(self.label_22)
        self.dateFinal = QtGui.QDateEdit(self.layoutWidget_12)
        self.dateFinal.setMinimumSize(QtCore.QSize(100, 30))
        self.dateFinal.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.dateFinal.setFont(font)
        self.dateFinal.setObjectName(_fromUtf8("dateFinal"))
        self.verticalLayout_2.addWidget(self.dateFinal)
        self.btnCrearRe = QtGui.QPushButton(self.tabRegimen)
        self.btnCrearRe.setGeometry(QtCore.QRect(200, 280, 85, 27))
        self.btnCrearRe.setObjectName(_fromUtf8("btnCrearRe"))
        self.layoutWidget4 = QtGui.QWidget(self.tabRegimen)
        self.layoutWidget4.setGeometry(QtCore.QRect(70, 200, 148, 32))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_19 = QtGui.QLabel(self.layoutWidget4)
        self.label_19.setMinimumSize(QtCore.QSize(70, 30))
        self.label_19.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_7.addWidget(self.label_19)
        self.spinNInicio = QtGui.QSpinBox(self.layoutWidget4)
        self.spinNInicio.setMinimumSize(QtCore.QSize(70, 30))
        self.spinNInicio.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.spinNInicio.setFont(font)
        self.spinNInicio.setObjectName(_fromUtf8("spinNInicio"))
        self.horizontalLayout_7.addWidget(self.spinNInicio)
        self.layoutWidget5 = QtGui.QWidget(self.tabRegimen)
        self.layoutWidget5.setGeometry(QtCore.QRect(290, 200, 148, 32))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_20 = QtGui.QLabel(self.layoutWidget5)
        self.label_20.setMinimumSize(QtCore.QSize(70, 30))
        self.label_20.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_8.addWidget(self.label_20)
        self.spinNFinal = QtGui.QSpinBox(self.layoutWidget5)
        self.spinNFinal.setMinimumSize(QtCore.QSize(70, 30))
        self.spinNFinal.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.spinNFinal.setFont(font)
        self.spinNFinal.setObjectName(_fromUtf8("spinNFinal"))
        self.horizontalLayout_8.addWidget(self.spinNFinal)
        self.tabWidget.addTab(self.tabRegimen, _fromUtf8(""))

        self.retranslateUi(Ajustes)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Ajustes)

    def retranslateUi(self, Ajustes):
        Ajustes.setWindowTitle(_translate("Ajustes", "Ajustes Generales ", None))
        self.label.setText(_translate("Ajustes", "Configuración De Parqueader", None))
        self.label_3.setText(_translate("Ajustes", "NIT", None))
        self.txtNitPar.setToolTip(_translate("Ajustes", "Inserte NIT actual del parqueadero", None))
        self.label_4.setText(_translate("Ajustes", "Teléfono", None))
        self.txtTlefono.setToolTip(_translate("Ajustes", "Inserte Teléfono actual del parqueadero", None))
        self.label_5.setText(_translate("Ajustes", "Dirección", None))
        self.txtDireccion.setToolTip(_translate("Ajustes", "Inserte Dirección actual del parqueadero", None))
        self.btnActualizarPar.setText(_translate("Ajustes", "Actualizar", None))
        self.label_2.setText(_translate("Ajustes", "Nombre", None))
        self.txtNombrePar.setToolTip(_translate("Ajustes", "Inserte nombre actual del parqueadero", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPar), _translate("Ajustes", "Paequeadero", None))
        self.label_6.setText(_translate("Ajustes", "tipo de vehículos", None))
        self.label_10.setText(_translate("Ajustes", "Hora", None))
        self.spinHora.setToolTip(_translate("Ajustes", "Ingrese valor de la Hora", None))
        self.label_15.setText(_translate("Ajustes", "Epecial", None))
        self.spinEspecial.setToolTip(_translate("Ajustes", "Ingrese valor hora especial", None))
        self.label_11.setText(_translate("Ajustes", "Día", None))
        self.spinDia.setToolTip(_translate("Ajustes", "Ingrese valor del Día", None))
        self.label_16.setText(_translate("Ajustes", "# Celdas", None))
        self.btnActualizarVehiculo.setToolTip(_translate("Ajustes", "Botón para almacenar los cambios del vehículo.", None))
        self.btnActualizarVehiculo.setText(_translate("Ajustes", "&Actualizar", None))
        self.btnActualizarVehiculo.setShortcut(_translate("Ajustes", "Ctrl+A", None))
        self.btnNuevoVehiculo.setToolTip(_translate("Ajustes", "Botón para crear un tipo vehículo", None))
        self.btnNuevoVehiculo.setText(_translate("Ajustes", "&Nuevo", None))
        self.btnNuevoVehiculo.setShortcut(_translate("Ajustes", "Ctrl+N", None))
        self.label_7.setText(_translate("Ajustes", "Seleccione", None))
        self.label_8.setText(_translate("Ajustes", "Tipo de Vehículo", None))
        self.labelTipoVehiculo.setText(_translate("Ajustes", "Vehículo", None))
        self.label_9.setText(_translate("Ajustes", "Fracción", None))
        self.label_14.setText(_translate("Ajustes", "Mes", None))
        self.spinMes.setToolTip(_translate("Ajustes", "Ingrese valor del Mes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVheiculo), _translate("Ajustes", "Tipo Vehículo", None))
        self.label_18.setText(_translate("Ajustes", "Configuración De Regimen", None))
        self.label_21.setText(_translate("Ajustes", "Fecha Inicio", None))
        self.label_22.setText(_translate("Ajustes", "Fecha Final", None))
        self.btnCrearRe.setText(_translate("Ajustes", "Crear", None))
        self.label_19.setText(_translate("Ajustes", "# Inicio", None))
        self.label_20.setText(_translate("Ajustes", "# Final", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRegimen), _translate("Ajustes", "Regimen", None))

