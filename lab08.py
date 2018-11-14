# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Oktatás\Programozás 2\lab08\worker.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import re
from PyQt5 import QtCore, QtGui, QtWidgets

class PhoneNumberFormatException (Exception):
    pass

class EmailFormatException (Exception):
    pass

class MissingDataException(Exception):
    def __init__(self,value):
        self.__value = value

    def __str__(self):
        return "The " + self.__value + " text box is empty. You should provide this mandatory data!"

class Worker:

    def __init__(self,name,id,address,phone,email):
        self.__name = name
        self.__id = id
        self.__address = address
        self.__phone = phone
        self.__email = email

    def getName(self):
        return self.__name

    def setName(self,p):
        self.__name = p

    def getID(self):
        return self.__id

    def getAddress(self):
        return self.__address

    def setAddress(self,p):
        self.__address = p

    def getPhone(self):
        return self.__phone

    def setPhone(self,p):
        self.__phone = p

    def getEmail(self):
        return self.__email

    def setEmail(self,p):
        self.__email = p

    def __str__(self):
        return self.__name + '(ID: ' + self.__id + ')'

    def __le__(self, other):
        if self.getName() == other.getName():
            return self.getID() < other.getID()
        else:
            return self.getName() < other.getName()

    def __gt__(self, other):
        return self.getName() > other.getName()

    def __eq__(self, other):
        return self.getID() == other.getID()

class Ui_MainWindow(object):

    lsWorkers = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 155, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 155, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.inName = QtWidgets.QLineEdit(self.centralwidget)
        self.inName.setGeometry(QtCore.QRect(70, 0, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inName.setFont(font)
        self.inName.setObjectName("inName")
        self.inID = QtWidgets.QLineEdit(self.centralwidget)
        self.inID.setGeometry(QtCore.QRect(90, 40, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inID.setFont(font)
        self.inID.setObjectName("inID")
        self.inAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.inAdd.setGeometry(QtCore.QRect(90, 80, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inAdd.setFont(font)
        self.inAdd.setObjectName("inAdd")
        self.inPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.inPhone.setGeometry(QtCore.QRect(140, 120, 391, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.inPhone.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inPhone.setFont(font)
        self.inPhone.setObjectName("inPhone")
        self.inMail = QtWidgets.QLineEdit(self.centralwidget)
        self.inMail.setGeometry(QtCore.QRect(70, 160, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inMail.setFont(font)
        self.inMail.setObjectName("inMail")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(10, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd_2.setGeometry(QtCore.QRect(100, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAdd_2.setFont(font)
        self.btnAdd_2.setObjectName("btnAdd_2")
        self.btnAdd_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd_3.setGeometry(QtCore.QRect(190, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAdd_3.setFont(font)
        self.btnAdd_3.setObjectName("btnAdd_3")
        self.btnAdd_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd_4.setGeometry(QtCore.QRect(280, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAdd_4.setFont(font)
        self.btnAdd_4.setObjectName("btnAdd_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 280, 521, 291))
        self.list.setFrameShape(QtWidgets.QFrame.Box)
        self.list.setObjectName("list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnAdd.clicked.connect(self.btnAddClicked)
        self.list.itemClicked.connect(self.itemClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Workers"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "ID code:"))
        self.label_3.setText(_translate("MainWindow", "Address:"))
        self.label_4.setText(_translate("MainWindow", "Phone number:"))
        self.label_5.setText(_translate("MainWindow", "Email:"))
        self.inPhone.setText(_translate("MainWindow", "+36301234567"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnAdd_2.setText(_translate("MainWindow", "Edit"))
        self.btnAdd_3.setText(_translate("MainWindow", "Modify"))
        self.btnAdd_4.setText(_translate("MainWindow", "Delete"))
        self.label_6.setText(_translate("MainWindow", "List of persons:"))

    def btnAddClicked(self):
        try:
            name = self.inName.text()
            id = self.inID.text()
            address = self.inAdd.text()
            phone = self.inPhone.text()
            email = self.inMail.text()

            if len(name) == 0:
                raise MissingDataException('name')
            if len(id) == 0:
                raise MissingDataException('ID number')
            if len(address)==0:
                raise MissingDataException('address')
            if len(phone)==0:
                raise MissingDataException('phone number')
            if len(email)==0:
                raise MissingDataException('email address')

            if len(phone) < 11 or len(phone) > 12 or phone.find('+36') == -1:
                raise PhoneNumberFormatException

            if not re.match('(\w+@\w+(?:\.\w+))',email):
                raise EmailFormatException


        except MissingDataException as mse:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(mse.__str__())
            msg.exec()

        except PhoneNumberFormatException:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("The phone number is not in right format!")
            msg.exec()

        except EmailFormatException:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("The email address is not in right format!")
            msg.exec()

        else:
            w = Worker(name,id,address,phone,email)
            if w not in self.lsWorkers:
                self.lsWorkers.append(w)
                self.lsWorkers.sort()
                self.list.clear()
                for i in self.lsWorkers:
                    self.list.addItem(i.__str__())
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Warning!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("This person is already applied at your company!")
                msg.exec()

    def itemClicked(self,item):
        tmp = item.text()
        tmp = tmp.split('(')
        id = tmp[1][:-1].split(" ")
        id = id[1]
        for i in self.lsWorkers:
            if id == i.getID():
                self.inName.setText(i.getName())
                self.inID.setText(i.getID())
                self.inAdd.setText(i.getAddress())
                self.inPhone.setText(i.getPhone())
                self.inMail.setText(i.getEmail())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

