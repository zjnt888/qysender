# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 257)
        self.btnData = QtWidgets.QPushButton(Form)
        self.btnData.setGeometry(QtCore.QRect(200, 20, 75, 23))
        self.btnData.setObjectName("btnData")
        self.btnSend = QtWidgets.QPushButton(Form)
        self.btnSend.setGeometry(QtCore.QRect(400, 220, 75, 23))
        self.btnSend.setObjectName("btnSend")
        self.btnHelp = QtWidgets.QPushButton(Form)
        self.btnHelp.setGeometry(QtCore.QRect(400, 20, 75, 23))
        self.btnHelp.setObjectName("btnHelp")
        self.btnAbout = QtWidgets.QPushButton(Form)
        self.btnAbout.setGeometry(QtCore.QRect(480, 20, 75, 23))
        self.btnAbout.setObjectName("btnAbout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 50, 371, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 351, 131))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 161, 241))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 141, 211))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.btnInface = QtWidgets.QPushButton(Form)
        self.btnInface.setGeometry(QtCore.QRect(280, 20, 75, 23))
        self.btnInface.setObjectName("btnInface")
        self.btnExit = QtWidgets.QPushButton(Form)
        self.btnExit.setGeometry(QtCore.QRect(480, 220, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 220, 181, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.btnExit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "企业微信数据发送工具"))
        self.btnData.setText(_translate("Form", "数据"))
        self.btnSend.setText(_translate("Form", "发送"))
        self.btnHelp.setText(_translate("Form", "说明"))
        self.btnAbout.setText(_translate("Form", "关于"))
        self.groupBox_2.setTitle(_translate("Form", "发送信息"))
        self.groupBox.setTitle(_translate("Form", "数据字段"))
        self.btnInface.setText(_translate("Form", "接口"))
        self.btnExit.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "测试版本，谨慎操作！"))
