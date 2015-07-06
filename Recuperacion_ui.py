# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cowboy/PycharmProjects/CVP/Recuperacion.ui'
#
# Created: Wed May 27 02:08:30 2015
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
        Dialog.resize(400, 356)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 60, 201, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtDocumento = QtGui.QLineEdit(Dialog)
        self.txtDocumento.setGeometry(QtCore.QRect(80, 120, 113, 27))
        self.txtDocumento.setObjectName(_fromUtf8("txtDocumento"))
        self.txtRespuesta = QtGui.QLineEdit(Dialog)
        self.txtRespuesta.setGeometry(QtCore.QRect(200, 210, 113, 27))
        self.txtRespuesta.setObjectName(_fromUtf8("txtRespuesta"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 170, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 310, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnConsultar = QtGui.QPushButton(Dialog)
        self.btnConsultar.setGeometry(QtCore.QRect(220, 120, 98, 27))
        self.btnConsultar.setObjectName(_fromUtf8("btnConsultar"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 220, 71, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnComparar = QtGui.QPushButton(Dialog)
        self.btnComparar.setGeometry(QtCore.QRect(150, 260, 98, 27))
        self.btnComparar.setObjectName(_fromUtf8("btnComparar"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 201, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Escribe Documento deUsuario", None))
        self.label_2.setText(_translate("Dialog", "Pregunta", None))
        self.label_3.setText(_translate("Dialog", "CLAvE", None))
        self.btnConsultar.setText(_translate("Dialog", "consultar", None))
        self.label_4.setText(_translate("Dialog", "Respuestas", None))
        self.btnComparar.setText(_translate("Dialog", "responder", None))
        self.label_5.setText(_translate("Dialog", "Recuperacion de COntraseña", None))

