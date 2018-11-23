# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Oktatás\Programozás 2\lab08\worker.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import re
from PyQt5 import QtCore, QtGui, QtWidgets
import myClasses as mc

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
        # brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        # brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        # brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        # self.inPhone.setPalette(palette)
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
        self.btnAdd_2.clicked.connect(self.editClicked)
        self.btnAdd_3.clicked.connect(self.btnAddClicked)
        self.btnAdd_4.clicked.connect(self.deleteItem)
        # self.list.itemClicked.connect(self.itemClicked)

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
        self.reloadDatas()

    def btnAddClicked(self):
        try:
            name = self.inName.text()
            id = self.inID.text()
            address = self.inAdd.text()
            phone = self.inPhone.text()
            email = self.inMail.text()

            if len(name) == 0:
                raise mc.MissingDataException('name')
            if len(id) == 0:
                raise mc.MissingDataException('ID number')
            if len(address)==0:
                raise mc.MissingDataException('address')
            if len(phone)==0:
                raise mc.MissingDataException('phone number')
            if len(email)==0:
                raise mc.MissingDataException('email address')

            if len(phone) < 11 or len(phone) > 12 or not re.match('[+]36([0-9])',phone):
                raise mc.PhoneNumberFormatException

            if not re.match('([0-9a-zA-Z_.-]+@\w+(?:\.\w+))',email):
                raise mc.EmailFormatException


        except mc.MissingDataException as mse:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(mse.__str__())
            msg.exec()

        except mc.PhoneNumberFormatException:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("The phone number is not in right format!")
            msg.exec()

        except mc.EmailFormatException:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("The email address is not in right format!")
            msg.exec()

        else:
            if not self.inID.isReadOnly():
                w = mc.Worker(name,id,address,phone,email)
                if w not in self.lsWorkers:
                    self.lsWorkers.append(w)
                    self.lsWorkers.sort()
                    self.list.clear()
                    self.saveToFile()
                    for i in self.lsWorkers:
                        self.list.addItem(i.__str__())
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("This person has already applied at your company!")
                    msg.exec()
            else:
                for i in self.lsWorkers:
                    if i.getID() == self.inID.text():
                        self.lsWorkers.remove(i)
                        i.setName(name)
                        i.setAddress(address)
                        i.setPhone(phone)
                        i.setEmail(email)
                        self.lsWorkers.append(i)
                        self.lsWorkers.sort()
                        self.list.clear()
                        self.saveToFile()
                        self.inID.setReadOnly(False)
                        for j in self.lsWorkers:
                            self.list.addItem(j.__str__())


    def editClicked(self,item):
        if not self.list.currentItem():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should select any person from the list!")
            msg.exec()
        else:
            item = self.list.currentItem()
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
                    self.inID.setReadOnly(True)

    def deleteItem(self):
        if not self.list.currentItem():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should select any person from the list!")
            msg.exec()
        else:
            item = self.list.currentItem()
            tmp = item.text()
            tmp = tmp.split('(')
            id = tmp[1][:-1].split(" ")
            id = id[1]
            for i in self.lsWorkers:
                if id == i.getID():
                    self.lsWorkers.remove(i)
                    self.saveToFile()
                    self.list.clear()
                    for j in self.lsWorkers:
                        self.list.addItem(j.__str__())

    def saveToFile(self):
        outFile = open("database.txt","w")
        for i in self.lsWorkers:
            print('{};{};{};{};{}\n'.format(i.getName(),i.getID(),i.getAddress(),i.getPhone(),i.getEmail()),file=outFile)
        outFile.close()

    def reloadDatas(self):
        inFile = open("database.txt","r")
        for i in inFile:
            if i.count(";") == 4:
                tmp = i.split(';')
                self.lsWorkers.append(mc.Worker(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4][:-1]))
        inFile.close()
        self.lsWorkers.sort()
        for i in self.lsWorkers:
            self.list.addItem(i.__str__())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

