# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hallgato\HBgyak\newClassID.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNewClassID(object):
    def setupUi(self, AddNewClassID):
        AddNewClassID.setObjectName("AddNewClassID")
        AddNewClassID.resize(296, 93)
        self.centralwidget = QtWidgets.QWidget(AddNewClassID)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_classID = QtWidgets.QLineEdit(self.centralwidget)
        self.input_classID.setGeometry(QtCore.QRect(62, 23, 141, 20))
        self.input_classID.setObjectName("input_classID")
        self.btn_OK = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OK.setGeometry(QtCore.QRect(213, 22, 75, 23))
        self.btn_OK.setObjectName("btn_OK")
        AddNewClassID.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddNewClassID)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 296, 21))
        self.menubar.setObjectName("menubar")
        AddNewClassID.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddNewClassID)
        self.statusbar.setObjectName("statusbar")
        AddNewClassID.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewClassID)
        QtCore.QMetaObject.connectSlotsByName(AddNewClassID)

    def retranslateUi(self, AddNewClassID):
        _translate = QtCore.QCoreApplication.translate
        AddNewClassID.setWindowTitle(_translate("AddNewClassID", "Add new class ID"))
        self.label.setText(_translate("AddNewClassID", "class ID:"))
        self.btn_OK.setText(_translate("AddNewClassID", "OK"))

