# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Oktatás\Programozás 2\lab07\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import mTT
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    filename = ""
    lsTrain = dict([])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setGeometry(QtCore.QRect(160, 310, 75, 23))
        self.btnOpen.setObjectName("btnOpen")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 21))
        self.label.setObjectName("label")
        self.trainList = QtWidgets.QListWidget(self.centralwidget)
        self.trainList.setGeometry(QtCore.QRect(10, 30, 341, 51))
        self.trainList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trainList.setObjectName("trainList")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.stopList = QtWidgets.QListWidget(self.centralwidget)
        self.stopList.setGeometry(QtCore.QRect(10, 110, 341, 121))
        self.stopList.setObjectName("stopList")
        self.inID = QtWidgets.QLineEdit(self.centralwidget)
        self.inID.setGeometry(QtCore.QRect(30, 250, 113, 20))
        self.inID.setObjectName("inID")
        self.inName = QtWidgets.QLineEdit(self.centralwidget)
        self.inName.setGeometry(QtCore.QRect(190, 250, 113, 20))
        self.inName.setObjectName("inName")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 47, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 250, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 280, 47, 13))
        self.label_5.setObjectName("label_5")
        self.inFrom = QtWidgets.QLineEdit(self.centralwidget)
        self.inFrom.setGeometry(QtCore.QRect(90, 280, 113, 20))
        self.inFrom.setObjectName("inFrom")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 280, 47, 13))
        self.label_6.setObjectName("label_6")
        self.inDest = QtWidgets.QLineEdit(self.centralwidget)
        self.inDest.setGeometry(QtCore.QRect(230, 280, 113, 20))
        self.inDest.setObjectName("inDest")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 310, 47, 13))
        self.label_7.setObjectName("label_7")
        self.btnAddnew = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddnew.setGeometry(QtCore.QRect(244, 310, 111, 23))
        self.btnAddnew.setObjectName("btnAddnew")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnAddnew.clicked.connect(self.createNewTrainElement)
        self.btnOpen.clicked.connect(self.inputFileName)
        self.trainList.itemClicked.connect(self.item_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inter City"))
        self.btnOpen.setText(_translate("MainWindow", "Open..."))
        self.label.setText(_translate("MainWindow", "Trains:"))
        self.label_2.setText(_translate("MainWindow", "Stops:"))
        self.label_3.setText(_translate("MainWindow", "Id:"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "From:"))
        self.label_6.setText(_translate("MainWindow", "To:"))
        self.label_7.setText(_translate("MainWindow", "Stops:"))
        self.btnAddnew.setText(_translate("MainWindow", "Add new train"))

    def createNewTrainElement(self):
        t1 = mTT.IC(self.inID.text(),self.inName.text(),self.inFrom.text(),self.inDest.text())
        t1.inputStops(self.filename)
        if t1.getID() not in self.lsTrain:
            self.trainList.addItem(t1.getID() + " - " + t1.getName())
            self.lsTrain[t1.getID()] = t1

    def inputFileName(self):
        self.filename,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Select file...")

    def item_click(self,item):
        self.stopList.clear()
        tmp1 = str(item.text())
        tmp = tmp1.split(" ")
        if tmp[0] in self.lsTrain:
            for i in self.lsTrain[tmp[0]].getStops():
                self.stopList.addItem(i.__str__())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


