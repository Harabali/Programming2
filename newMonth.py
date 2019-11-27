# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hallgato\HBgyak\newMonth.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NameDays(object):
    def setupUi(self, NameDays):
        NameDays.setObjectName("NameDays")
        NameDays.resize(408, 278)
        self.centralwidget = QtWidgets.QWidget(NameDays)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Name.setGeometry(QtCore.QRect(121, 23, 91, 20))
        self.input_Name.setObjectName("input_Name")
        self.btn_Add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Add.setGeometry(QtCore.QRect(220, 21, 75, 23))
        self.btn_Add.setObjectName("btn_Add")
        self.btn_fromFile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fromFile.setGeometry(QtCore.QRect(301, 21, 91, 23))
        self.btn_fromFile.setObjectName("btn_fromFile")
        self.ls_Names = QtWidgets.QListWidget(self.centralwidget)
        self.ls_Names.setGeometry(QtCore.QRect(10, 50, 381, 181))
        self.ls_Names.setObjectName("ls_Names")
        NameDays.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NameDays)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 21))
        self.menubar.setObjectName("menubar")
        NameDays.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NameDays)
        self.statusbar.setObjectName("statusbar")
        NameDays.setStatusBar(self.statusbar)

        self.retranslateUi(NameDays)
        QtCore.QMetaObject.connectSlotsByName(NameDays)

    def retranslateUi(self, NameDays):
        _translate = QtCore.QCoreApplication.translate
        NameDays.setWindowTitle(_translate("NameDays", "setup new Month and Names"))
        self.label.setText(_translate("NameDays", "Number of Month:"))
        self.btn_Add.setText(_translate("NameDays", "Add"))
        self.btn_fromFile.setText(_translate("NameDays", "Open..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NameDays = QtWidgets.QMainWindow()
    ui = Ui_NameDays()
    ui.setupUi(NameDays)
    NameDays.show()
    sys.exit(app.exec_())
