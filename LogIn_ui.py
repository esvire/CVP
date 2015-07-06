# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cowboy/PycharmProjects/CVP/LogIn.ui'
#
# Created: Wed May 27 00:33:33 2015
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
        Dialog.resize(400, 300)
        self.btnIngresar = QtGui.QPushButton(Dialog)
        self.btnIngresar.setGeometry(QtCore.QRect(230, 220, 98, 27))
        self.btnIngresar.setObjectName(_fromUtf8("btnIngresar"))
        self.txtUser = QtGui.QLineEdit(Dialog)
        self.txtUser.setGeometry(QtCore.QRect(220, 130, 113, 27))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.txtClave = QtGui.QLineEdit(Dialog)
        self.txtClave.setGeometry(QtCore.QRect(220, 170, 113, 27))
        self.txtClave.setObjectName(_fromUtf8("txtClave"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 140, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 40, 171, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 80, 101, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 220, 161, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btnIngresar.setText(_translate("Dialog", "Ingresar", None))
        self.label.setText(_translate("Dialog", "Documento Usuario", None))
        self.label_2.setText(_translate("Dialog", "Contraseña", None))
        self.label_3.setText(_translate("Dialog", "PARQUEADERO MARBEY", None))
        self.label_4.setText(_translate("Dialog", "inicio de sesión", None))
        self.commandLinkButton.setText(_translate("Dialog", "Recordar Contraseña", None))

