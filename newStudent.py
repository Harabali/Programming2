# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hallgato\HBgyak\newStudent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNewStudent(object):
    def setupUi(self, AddNewStudent):
        AddNewStudent.setObjectName("AddNewStudent")
        AddNewStudent.resize(414, 90)
        self.centralwidget = QtWidgets.QWidget(AddNewStudent)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Name.setGeometry(QtCore.QRect(51, 23, 161, 20))
        self.input_Name.setObjectName("input_Name")
        self.btn_OK = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OK.setGeometry(QtCore.QRect(220, 21, 75, 23))
        self.btn_OK.setObjectName("btn_OK")
        self.btn_fromFile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fromFile.setGeometry(QtCore.QRect(301, 21, 91, 23))
        self.btn_fromFile.setObjectName("btn_fromFile")
        AddNewStudent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddNewStudent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 21))
        self.menubar.setObjectName("menubar")
        AddNewStudent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddNewStudent)
        self.statusbar.setObjectName("statusbar")
        AddNewStudent.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewStudent)
        QtCore.QMetaObject.connectSlotsByName(AddNewStudent)

    def retranslateUi(self, AddNewStudent):
        _translate = QtCore.QCoreApplication.translate
        AddNewStudent.setWindowTitle(_translate("AddNewStudent", "add new Student"))
        self.label.setText(_translate("AddNewStudent", "Name:"))
        self.btn_OK.setText(_translate("AddNewStudent", "OK"))
        self.btn_fromFile.setText(_translate("AddNewStudent", "Open..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewStudent = QtWidgets.QMainWindow()
    ui = Ui_AddNewStudent()
    ui.setupUi(AddNewStudent)
    AddNewStudent.show()
    sys.exit(app.exec_())
