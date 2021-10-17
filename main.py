# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 421)
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(20, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.one.setFont(font)
        self.one.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(90, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.two.setFont(font)
        self.two.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.two.setObjectName("two")
        self.theere = QtWidgets.QPushButton(self.centralwidget)
        self.theere.setGeometry(QtCore.QRect(160, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.theere.setFont(font)
        self.theere.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.theere.setObjectName("theere")
        self.foure = QtWidgets.QPushButton(self.centralwidget)
        self.foure.setGeometry(QtCore.QRect(230, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.foure.setFont(font)
        self.foure.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.foure.setObjectName("foure")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(20, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.five.setFont(font)
        self.five.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(90, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.six.setFont(font)
        self.six.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.six.setObjectName("six")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(160, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.seven.setFont(font)
        self.seven.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(230, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eight.setFont(font)
        self.eight.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(90, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nine.setFont(font)
        self.nine.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.nine.setObjectName("nine")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(20, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plus.setFont(font)
        self.plus.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(230, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minus.setFont(font)
        self.minus.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.minus.setObjectName("minus")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(160, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.zero.setFont(font)
        self.zero.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.zero.setObjectName("zero")
        self.razdel = QtWidgets.QPushButton(self.centralwidget)
        self.razdel.setGeometry(QtCore.QRect(90, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.razdel.setFont(font)
        self.razdel.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.razdel.setObjectName("razdel")
        self.umnozh = QtWidgets.QPushButton(self.centralwidget)
        self.umnozh.setGeometry(QtCore.QRect(20, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.umnozh.setFont(font)
        self.umnozh.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.umnozh.setObjectName("umnozh")
        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(230, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.result.setFont(font)
        self.result.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.result.setObjectName("result")
        self.tochka = QtWidgets.QPushButton(self.centralwidget)
        self.tochka.setGeometry(QtCore.QRect(160, 360, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tochka.setFont(font)
        self.tochka.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.tochka.setObjectName("tochka")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(20, 80, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_s1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_s1.setGeometry(QtCore.QRect(160, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_s1.setFont(font)
        self.btn_s1.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.btn_s1.setObjectName("btn_s1")
        self.btn_s2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_s2.setGeometry(QtCore.QRect(230, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_s2.setFont(font)
        self.btn_s2.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border: 2px solid rgb(255, 152, 152);\n"
"border-radius: 5%;")
        self.btn_s2.setObjectName("btn_s2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 91, 51))
        self.widget.setStyleSheet("background-color: rgb(255, 152, 152);\n"
"border-radius: 10%;\n"
"")
        self.widget.setObjectName("widget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(30, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(226, 226, 226);\n"
"background-color: rgb(255, 152, 152);\n"
"border-radius: 10%;")
        self.label_result.setObjectName("label_result")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def add_functions(self):
        self.zero.clicked.connect(lambda: self.write_number(self.zero.text()))
        self.one.clicked.connect(lambda: self.write_number(self.one.text()))
        self.two.clicked.connect(lambda: self.write_number(self.two.text()))
        self.theere.clicked.connect(lambda: self.write_number(self.theere.text()))
        self.foure.clicked.connect(lambda: self.write_number(self.foure.text()))
        self.five.clicked.connect(lambda: self.write_number(self.five.text()))
        self.six.clicked.connect(lambda: self.write_number(self.six.text()))
        self.seven.clicked.connect(lambda: self.write_number(self.seven.text()))
        self.eight.clicked.connect(lambda: self.write_number(self.eight.text()))
        self.nine.clicked.connect(lambda: self.write_number(self.nine.text()))
        self.plus.clicked.connect(lambda: self.write_number(self.plus.text()))
        self.tochka.clicked.connect(lambda: self.write_number(self.tochka.text()))
        self.minus.clicked.connect(lambda: self.write_number(self.minus.text()))
        self.razdel.clicked.connect(lambda: self.write_number(self.razdel.text()))
        self.btn_s1.clicked.connect(lambda: self.write_number(self.btn_s1.text()))
        self.btn_s2.clicked.connect(lambda: self.write_number(self.btn_s2.text()))
        self.umnozh.clicked.connect(lambda: self.write_number(self.umnozh.text()))
        self.btn_delete.clicked.connect(lambda: self.write_number(self.btn_delete.text()))
        self.result.clicked.connect(lambda: self.write_number(self.result.text()))

    def write_number(self, number):
        if number == self.btn_delete.text():
            self.label_result.setText("0")
        elif number == self.result.text():
            try:
                self.label_result.setText(str(eval(self.label_result.text())))
            except ZeroDivisionError:
                self.label_result.setText("Деление на 0!")
            except SyntaxError:
                error = QMessageBox()
                error.setWindowTitle("WARNING")
                error.setText("Непонятная запись!")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.setDetailedText("Вы ввели Синтаксическую ошибку. Вы ввели: "+self.label_result.text())
                error.exec_()
                self.label_result.setText("0")
            except TypeError:
                error = QMessageBox()
                error.setWindowTitle("WARNING")
                error.setText("Непонятная запись!")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.setDetailedText("Вы ввели Синтаксическую ошибку. Вы ввели: " + self.label_result.text())
                error.exec_()
                self.label_result.setText("0")
        else:
            if self.label_result.text() == "0" or self.label_result.text() == "Деление на 0!" or self.label_result.text() == "Непонятная запись!":
                self.label_result.setText(number)
            else:
                self.label_result.setText(self.label_result.text() + number)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.theere.setText(_translate("MainWindow", "3"))
        self.foure.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.razdel.setText(_translate("MainWindow", "/"))
        self.umnozh.setText(_translate("MainWindow", "*"))
        self.result.setText(_translate("MainWindow", "="))
        self.tochka.setText(_translate("MainWindow", "."))
        self.btn_delete.setText(_translate("MainWindow", "DEL"))
        self.btn_s1.setText(_translate("MainWindow", "("))
        self.btn_s2.setText(_translate("MainWindow", ")"))
        self.label_result.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
