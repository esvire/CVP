# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecuperarClave.ui'
#
# Created: Sat Aug  1 20:14:30 2015
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

class Ui_RecuperacionClave(object):
    def setupUi(self, RecuperacionClave):
        RecuperacionClave.setObjectName(_fromUtf8("RecuperacionClave"))
        RecuperacionClave.resize(485, 606)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        RecuperacionClave.setFont(font)
        self.label = QtGui.QLabel(RecuperacionClave)
        self.label.setGeometry(QtCore.QRect(30, 30, 421, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(RecuperacionClave)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 301, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget = QtGui.QWidget(RecuperacionClave)
        self.widget.setGeometry(QtCore.QRect(50, 130, 370, 387))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtDocumento = QtGui.QLineEdit(self.widget)
        self.txtDocumento.setMinimumSize(QtCore.QSize(120, 35))
        self.txtDocumento.setMaximumSize(QtCore.QSize(120, 30))
        self.txtDocumento.setToolTip(_fromUtf8(""))
        self.txtDocumento.setObjectName(_fromUtf8("txtDocumento"))
        self.horizontalLayout.addWidget(self.txtDocumento)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnConsultarDoc = QtGui.QPushButton(self.widget)
        self.btnConsultarDoc.setMinimumSize(QtCore.QSize(120, 30))
        self.btnConsultarDoc.setObjectName(_fromUtf8("btnConsultarDoc"))
        self.horizontalLayout.addWidget(self.btnConsultarDoc)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(190, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textPregunta = QtGui.QTextEdit(self.widget)
        self.textPregunta.setMinimumSize(QtCore.QSize(300, 80))
        self.textPregunta.setMaximumSize(QtCore.QSize(500, 80))
        self.textPregunta.setToolTip(_fromUtf8(""))
        self.textPregunta.setObjectName(_fromUtf8("textPregunta"))
        self.verticalLayout.addWidget(self.textPregunta)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(98, 30))
        self.label_4.setMaximumSize(QtCore.QSize(100, 30))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(190, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.txtRespuesta = QtGui.QLineEdit(self.widget)
        self.txtRespuesta.setMinimumSize(QtCore.QSize(300, 35))
        self.txtRespuesta.setToolTip(_fromUtf8(""))
        self.txtRespuesta.setObjectName(_fromUtf8("txtRespuesta"))
        self.verticalLayout.addWidget(self.txtRespuesta)
        self.widget1 = QtGui.QWidget(RecuperacionClave)
        self.widget1.setGeometry(QtCore.QRect(50, 540, 371, 38))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btnConsultar = QtGui.QPushButton(self.widget1)
        self.btnConsultar.setMinimumSize(QtCore.QSize(120, 30))
        self.btnConsultar.setObjectName(_fromUtf8("btnConsultar"))
        self.horizontalLayout_4.addWidget(self.btnConsultar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.btnCancelar = QtGui.QPushButton(self.widget1)
        self.btnCancelar.setMinimumSize(QtCore.QSize(120, 30))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_4.addWidget(self.btnCancelar)

        self.retranslateUi(RecuperacionClave)
        QtCore.QMetaObject.connectSlotsByName(RecuperacionClave)
        RecuperacionClave.setTabOrder(self.txtDocumento, self.btnConsultarDoc)
        RecuperacionClave.setTabOrder(self.btnConsultarDoc, self.textPregunta)
        RecuperacionClave.setTabOrder(self.textPregunta, self.txtRespuesta)
        RecuperacionClave.setTabOrder(self.txtRespuesta, self.btnConsultar)
        RecuperacionClave.setTabOrder(self.btnConsultar, self.btnCancelar)

    def retranslateUi(self, RecuperacionClave):
        RecuperacionClave.setWindowTitle(_translate("RecuperacionClave", "Recuperación de contraseña", None))
        self.label.setText(_translate("RecuperacionClave", "Recuperación de contraseña", None))
        self.label_2.setText(_translate("RecuperacionClave", "Ingrese el documento registrado", None))
        self.btnConsultarDoc.setText(_translate("RecuperacionClave", "Consultar", None))
        self.label_3.setText(_translate("RecuperacionClave", "Pregunta :", None))
        self.label_4.setText(_translate("RecuperacionClave", "Respuesta:", None))
        self.btnConsultar.setText(_translate("RecuperacionClave", "Consultar", None))
        self.btnCancelar.setText(_translate("RecuperacionClave", "Cancelar", None))

