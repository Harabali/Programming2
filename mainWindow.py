# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hallgato\HBgyak\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Close.setGeometry(QtCore.QRect(510, 390, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Close.setFont(font)
        self.btn_Close.setObjectName("btn_Close")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.box_Class = QtWidgets.QComboBox(self.centralwidget)
        self.box_Class.setGeometry(QtCore.QRect(70, 20, 111, 22))
        self.box_Class.setObjectName("box_Class")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 251, 301))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_addClass = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addClass.setGeometry(QtCore.QRect(187, 19, 75, 21))
        self.btn_addClass.setObjectName("btn_addClass")
        self.btn_addStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addStudent.setGeometry(QtCore.QRect(10, 390, 81, 31))
        self.btn_addStudent.setObjectName("btn_addStudent")
        self.btn_delStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delStudent.setGeometry(QtCore.QRect(100, 390, 81, 31))
        self.btn_delStudent.setObjectName("btn_delStudent")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.box_Months = QtWidgets.QComboBox(self.centralwidget)
        self.box_Months.setGeometry(QtCore.QRect(380, 20, 111, 21))
        self.box_Months.setObjectName("box_Months")
        self.btn_addMonth = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addMonth.setGeometry(QtCore.QRect(491, 19, 21, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addMonth.setFont(font)
        self.btn_addMonth.setObjectName("btn_addMonth")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(280, 80, 311, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Celebrations of Class"))
        self.btn_Close.setText(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "Class ID:"))
        self.label_2.setText(_translate("MainWindow", "Students:"))
        self.btn_addClass.setText(_translate("MainWindow", "Add..."))
        self.btn_addStudent.setText(_translate("MainWindow", "Add..."))
        self.btn_delStudent.setText(_translate("MainWindow", "Delete"))
        self.label_3.setText(_translate("MainWindow", "Celebrations in"))
        self.btn_addMonth.setText(_translate("MainWindow", "+"))
        self.label_4.setText(_translate("MainWindow", "Namedays:"))

