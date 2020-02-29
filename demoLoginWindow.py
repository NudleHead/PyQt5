# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoLoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(692, 542)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(320, 20, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 20, 55, 16))
        self.label_2.setObjectName("label_2")
        self.passwordEditLine = QtWidgets.QLineEdit(Dialog)
        self.passwordEditLine.setGeometry(QtCore.QRect(500, 50, 151, 31))
        self.passwordEditLine.setObjectName("passwordEditLine")
        self.loginEditLine = QtWidgets.QLineEdit(Dialog)
        self.loginEditLine.setGeometry(QtCore.QRect(320, 50, 151, 31))
        self.loginEditLine.setObjectName("loginEditLine")
        self.signInButton = QtWidgets.QPushButton(Dialog)
        self.signInButton.setGeometry(QtCore.QRect(560, 120, 93, 28))
        self.signInButton.setObjectName("signInButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 200, 131, 21))
        self.label_3.setObjectName("label_3")
        self.regNameEdit = QtWidgets.QLineEdit(Dialog)
        self.regNameEdit.setGeometry(QtCore.QRect(490, 260, 151, 31))
        self.regNameEdit.setObjectName("regNameEdit")
        self.regLoginEdit = QtWidgets.QLineEdit(Dialog)
        self.regLoginEdit.setGeometry(QtCore.QRect(490, 320, 151, 31))
        self.regLoginEdit.setObjectName("regLoginEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(390, 270, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(390, 330, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(390, 390, 55, 16))
        self.label_6.setObjectName("label_6")
        self.registrationButton = QtWidgets.QPushButton(Dialog)
        self.registrationButton.setGeometry(QtCore.QRect(440, 480, 201, 41))
        self.registrationButton.setObjectName("registrationButton")
        self.regPasswordEdit = QtWidgets.QLineEdit(Dialog)
        self.regPasswordEdit.setGeometry(QtCore.QRect(490, 380, 151, 31))
        self.regPasswordEdit.setObjectName("regPasswordEdit")
        self.warningLabel = QtWidgets.QLabel(Dialog)
        self.warningLabel.setGeometry(QtCore.QRect(400, 430, 261, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.warningLabel.setPalette(palette)
        self.warningLabel.setObjectName("warningLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "login"))
        self.label_2.setText(_translate("Dialog", "password"))
        self.signInButton.setText(_translate("Dialog", "Sign in"))
        self.label_3.setText(_translate("Dialog", "Registration"))
        self.label_4.setText(_translate("Dialog", "name"))
        self.label_5.setText(_translate("Dialog", "login"))
        self.label_6.setText(_translate("Dialog", "password"))
        self.registrationButton.setText(_translate("Dialog", "Register"))
        self.warningLabel.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
