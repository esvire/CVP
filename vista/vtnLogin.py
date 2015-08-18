# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Tue Jul 28 21:25:17 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(415, 310)
        Dialog.setMinimumSize(QtCore.QSize(415, 310))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 280, 41))
        self.label.setMinimumSize(QtCore.QSize(280, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 80, 356, 196))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(130, 40))
        self.label_2.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.txtDocumento = QtGui.QLineEdit(self.widget)
        self.txtDocumento.setMinimumSize(QtCore.QSize(120, 35))
        self.txtDocumento.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtDocumento.setFont(font)
        self.txtDocumento.setText(_fromUtf8(""))
        self.txtDocumento.setObjectName(_fromUtf8("txtDocumento"))
        self.horizontalLayout.addWidget(self.txtDocumento)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(130, 40))
        self.label_3.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.txtClave = QtGui.QLineEdit(self.widget)
        self.txtClave.setMinimumSize(QtCore.QSize(120, 35))
        self.txtClave.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.txtClave.setFont(font)
        self.txtClave.setText(_fromUtf8(""))
        self.txtClave.setEchoMode(QtGui.QLineEdit.Password)
        self.txtClave.setObjectName(_fromUtf8("txtClave"))
        self.horizontalLayout_2.addWidget(self.txtClave)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(320, 50, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnRecordar = QtGui.QCommandLinkButton(self.widget)
        self.btnRecordar.setMinimumSize(QtCore.QSize(170, 40))
        self.btnRecordar.setObjectName(_fromUtf8("btnRecordar"))
        self.horizontalLayout_3.addWidget(self.btnRecordar)
        self.btnEntrar = QtGui.QPushButton(self.widget)
        self.btnEntrar.setMinimumSize(QtCore.QSize(75, 30))
        self.btnEntrar.setObjectName(_fromUtf8("btnEntrar"))
        self.horizontalLayout_3.addWidget(self.btnEntrar)
        self.btnSalir = QtGui.QPushButton(self.widget)
        self.btnSalir.setMinimumSize(QtCore.QSize(75, 30))
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.horizontalLayout_3.addWidget(self.btnSalir)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Login De Usuario", None))
        self.label.setText(_translate("Dialog", "Ingreso de usuario", None))
        self.label_2.setText(_translate("Dialog", "Documento", None))
        self.txtDocumento.setToolTip(_translate("Dialog", "<html><head/><body><p>Ingrese documento del usuario</p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "Contraseña", None))
        self.txtClave.setToolTip(_translate("Dialog", "<html><head/><body><p>Ingrese clave de usuario</p></body></html>", None))
        self.btnRecordar.setText(_translate("Dialog", "Recordar Contraseña", None))
        self.btnEntrar.setText(_translate("Dialog", "Entrar", None))
        self.btnSalir.setText(_translate("Dialog", "Salir", None))

