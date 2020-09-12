# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogInface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogInface(object):
    def setupUi(self, DialogInface):
        DialogInface.setObjectName("DialogInface")
        DialogInface.resize(432, 142)
        self.label = QtWidgets.QLabel(DialogInface)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogInface)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogInface)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_corpid = QtWidgets.QLineEdit(DialogInface)
        self.lineEdit_corpid.setGeometry(QtCore.QRect(70, 10, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_corpid.setFont(font)
        self.lineEdit_corpid.setObjectName("lineEdit_corpid")
        self.lineEdit_secret = QtWidgets.QLineEdit(DialogInface)
        self.lineEdit_secret.setGeometry(QtCore.QRect(70, 40, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_secret.setFont(font)
        self.lineEdit_secret.setObjectName("lineEdit_secret")
        self.lineEdit_agentid = QtWidgets.QLineEdit(DialogInface)
        self.lineEdit_agentid.setGeometry(QtCore.QRect(70, 70, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_agentid.setFont(font)
        self.lineEdit_agentid.setObjectName("lineEdit_agentid")
        self.btnUpdata = QtWidgets.QPushButton(DialogInface)
        self.btnUpdata.setGeometry(QtCore.QRect(330, 110, 75, 23))
        self.btnUpdata.setObjectName("btnUpdata")

        self.retranslateUi(DialogInface)
        self.btnUpdata.clicked.connect(DialogInface.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogInface)

    def retranslateUi(self, DialogInface):
        _translate = QtCore.QCoreApplication.translate
        DialogInface.setWindowTitle(_translate("DialogInface", "Dialog"))
        self.label.setText(_translate("DialogInface", "corpid:"))
        self.label_2.setText(_translate("DialogInface", "secret:"))
        self.label_3.setText(_translate("DialogInface", "agentid:"))
        self.btnUpdata.setText(_translate("DialogInface", "更新"))
