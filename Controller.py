import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from mainWindow import Ui_MainWindow
from newClassID import Ui_AddNewClassID
from lab06 import SchoolClass, NameDaysOfMonth, Student
from newStudent import Ui_AddNewStudent
from newMonth import Ui_NameDays
from datetime import datetime

class Controller:

    def __init__(self):
        self.classes = dict()
        self.monthDict = dict()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.btn_addClass.clicked.connect(self.openNewClassID)
        self.ui.btn_addStudent.clicked.connect(self.openNewStudent)
        self.ui.btn_addMonth.clicked.connect(self.openNewMonth)
        self.MainWindow.show()

    def openNewClassID(self):
        self.newWindow = QtWidgets.QMainWindow()
        self.ui2 = Ui_AddNewClassID()
        self.ui2.setupUi(self.newWindow)
        self.ui2.btn_OK.clicked.connect(self.addNewClass)
        self.newWindow.show()

    def addNewClass(self):
        str = self.ui2.input_classID.text()
        if str not in self.classes:
            self.ui.box_Class.addItem(str)
            self.classes[str] = SchoolClass(str)
            self.newWindow.close()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("This class already exists!")
            msg.exec()

    def openNewStudent(self):
        self.addNewStudentWindow = QtWidgets.QMainWindow()
        self.ui3 = Ui_AddNewStudent()
        self.ui3.setupUi(self.addNewStudentWindow)
        self.ui3.btn_OK.clicked.connect(self.addNewStudent)
        self.addNewStudentWindow.show()

    def addNewStudent(self):
        try:
            s = self.ui3.input_Name.text()
            classID = str(self.ui.box_Class.currentText())
            self.classes[classID].inputMember(s)
            self.ui.listWidget.clear()
            for i in self.classes[classID].getMember():
                self.ui.listWidget.addItem(i.__str__())
        except Exception as ex:
            msg = QtWidgets.QMessageBox()
            msg.setText(ex.__str__())
            msg.exec()

    def openNewMonth(self):
        self.thrWindow = QtWidgets.QMainWindow()
        self.ui4 = Ui_NameDays()
        self.ui4.setupUi(self.thrWindow)
        self.ui4.btn_Add.clicked.connect(self.createNewMonth)
        self.ui4.btn_fromFile.clicked.connect(self.openFile)
        self.thrWindow.show()

    def createNewMonth(self):
        try:
            self.newMonth = NameDaysOfMonth(int(self.ui4.input_Name.text()))
            if self.newMonth.getName() not in self.monthDict:
                self.monthDict[self.newMonth.getName()] = []
            self.ui.box_Months.addItem(self.newMonth.getName())
            self.ui.calendarWidget.setSelectedDate(QDate(2019,self.newMonth.getNumber(),1))


        except Exception as ex:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(ex.__str__())
            msg.exec()

    def openFile(self):
        try:
            self.filename,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Select file...")
            self.newMonth.inputNames(self.filename)
            self.monthDict[self.newMonth.getName()] = self.newMonth.getNames()
            for i in self.newMonth.getNames():
                self.ui4.listWidget.addItem(i)

        except Exception as ex:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(ex.__str__())
            msg.exec()


#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec_())