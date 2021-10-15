from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calculator(object):
    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(300, 350)
        calculator.setMaximumWidth(300)
        calculator.setMaximumHeight(350)
        calculator.setMinimumWidth(300)
        calculator.setMinimumHeight(350)
        self.centralwidget = QtWidgets.QWidget(calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.show_result = QtWidgets.QLabel(self.centralwidget)
        self.show_result.setGeometry(QtCore.QRect(0, 0, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.show_result.setFont(font)
        self.show_result.setStyleSheet("background-color: rgb(168, 165, 255);\n"
                                       "color: rgb(255, 193, 152);")
        self.show_result.setObjectName("result")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(0, 50, 75, 75))
        self.b1.setStyleSheet("background-color: rgb(222, 233, 255);\n"
                              "")
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(75, 50, 75, 75))
        self.b2.setStyleSheet("background-color: rgb(222, 233, 255);\n"
                              "")
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(150, 50, 75, 75))
        self.b3.setStyleSheet("background-color: rgb(222, 233, 255);")
        self.b3.setObjectName("b3")
        self.b_procent = QtWidgets.QPushButton(self.centralwidget)
        self.b_procent.setGeometry(QtCore.QRect(225, 50, 75, 75))
        self.b_procent.setStyleSheet("background-color: rgb(222, 233, 255);")
        self.b_procent.setObjectName("b_procent")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(150, 125, 75, 75))
        self.b6.setStyleSheet("background-color: rgb(222, 233, 255);")
        self.b6.setObjectName("b6")
        self.b_plus = QtWidgets.QPushButton(self.centralwidget)
        self.b_plus.setGeometry(QtCore.QRect(225, 125, 75, 75))
        self.b_plus.setStyleSheet("background-color: rgb(222, 233, 255);")
        self.b_plus.setObjectName("b_fr")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(75, 125, 75, 75))
        self.b5.setStyleSheet("background-color: rgb(222, 233, 255);\n"
                              "")
        self.b5.setObjectName("b5")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(0, 125, 75, 75))
        self.b4.setStyleSheet("background-color: rgb(222, 233, 255);\n"
                              "")
        self.b4.setObjectName("b4")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(150, 200, 75, 75))
        self.b9.setStyleSheet("background-color: rgb(222, 233, 255);")
        self.b9.setObjectName("b9")
        self.b_minus = QtWidgets.QPushButton(self.centralwidget)
        self.b_minus.setGeometry(QtCore.QRect(225, 200, 75, 75))
        self.b_minus.setStyleSheet("background-color: rgb(222, 233, 255);")
        self.b_minus.setObjectName("b_pow")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(75, 200, 75, 75))
        self.b8.setStyleSheet("background-color: rgb(222, 233, 255);\n"
                              "")
        self.b8.setObjectName("b8")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(0, 200, 75, 75))
        self.b7.setStyleSheet("background-color: rgb(222, 233, 255);\n"
                              "")
        self.b7.setObjectName("b7")
        self.b_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.b_multiply.setGeometry(QtCore.QRect(150, 275, 75, 75))
        self.b_multiply.setStyleSheet("background-color: rgb(222, 233, 255);")
        self.b_multiply.setObjectName("b_multiply")
        self.b_eq = QtWidgets.QPushButton(self.centralwidget)
        self.b_eq.setGeometry(QtCore.QRect(225, 275, 75, 75))
        self.b_eq.setStyleSheet("\n"
                                "background-color: rgb(255, 219, 230);")
        self.b_eq.setObjectName("b_eq")
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(75, 275, 75, 75))
        self.b0.setStyleSheet("background-color: rgb(222, 233, 255);\n"
                              "")
        self.b0.setObjectName("b0")
        self.b_devision = QtWidgets.QPushButton(self.centralwidget)
        self.b_devision.setGeometry(QtCore.QRect(0, 275, 75, 75))
        self.b_devision.setStyleSheet("background-color: rgb(222, 233, 255);\n"
                                      "")
        self.b_devision.setObjectName("b_devision")
        calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)

        self.add_functions()

    def retranslateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "calculator"))
        self.show_result.setText(_translate("calculator", "0"))
        self.b1.setText(_translate("calculator", "1"))
        self.b2.setText(_translate("calculator", "2"))
        self.b3.setText(_translate("calculator", "3"))
        self.b_procent.setText(_translate("calculator", "%"))
        self.b6.setText(_translate("calculator", "6"))
        self.b_plus.setText(_translate("calculator", "+"))
        self.b5.setText(_translate("calculator", "5"))
        self.b4.setText(_translate("calculator", "4"))
        self.b9.setText(_translate("calculator", "9"))
        self.b_minus.setText(_translate("calculator", "-"))
        self.b8.setText(_translate("calculator", "8"))
        self.b7.setText(_translate("calculator", "7"))
        self.b_multiply.setText(_translate("calculator", "*"))
        self.b_eq.setText(_translate("calculator", "="))
        self.b0.setText(_translate("calculator", "0"))
        self.b_devision.setText(_translate("calculator", "/"))

    def add_functions(self):
        self.b0.clicked.connect(lambda: self.write_nummber(self.b0.text()))
        self.b1.clicked.connect(lambda: self.write_nummber(self.b1.text()))
        self.b2.clicked.connect(lambda: self.write_nummber(self.b2.text()))
        self.b3.clicked.connect(lambda: self.write_nummber(self.b3.text()))
        self.b4.clicked.connect(lambda: self.write_nummber(self.b4.text()))
        self.b5.clicked.connect(lambda: self.write_nummber(self.b5.text()))
        self.b6.clicked.connect(lambda: self.write_nummber(self.b6.text()))
        self.b7.clicked.connect(lambda: self.write_nummber(self.b7.text()))
        self.b8.clicked.connect(lambda: self.write_nummber(self.b8.text()))
        self.b9.clicked.connect(lambda: self.write_nummber(self.b9.text()))

        self.b_devision.clicked.connect(lambda: self.write_sign(self.b_devision.text()))
        self.b_multiply.clicked.connect(lambda: self.write_sign(self.b_multiply.text()))

        self.b_minus.clicked.connect(lambda: self.write_sign(self.b_minus.text()))

        self.b_procent.clicked.connect(lambda: self.write_sign('/100*'))
        self.b_plus.clicked.connect(lambda: self.write_sign(self.b_plus.text()))

        self.b_eq.clicked.connect(self.result)

    checsign = lambda self, x: x == '/' or x == '*' or x == '+' or x == '-'
    pres_equal = True

    # =='/'or self.show_result.text()[-1]=='*'or self.show_result.text()[-1]=='+'or self.show_result.text()[-1]=='-'
    def result(self):
        if self.pres_equal:
            self.show_result.setText('0')
        else:
            if self.checsign(self.show_result.text()[-1]):
                self.show_result.setText(self.show_result.text()[0:-1])

        try:
            res = eval(self.show_result.text())
        except:
            res = '0'
        self.pres_equal = True
        self.show_result.setText(str(res))

    def write_sign(self, sign):
        if len(self.show_result.text()) > 0:
            b = self.show_result.text()[-1]
            if self.checsign(b):
                self.show_result.setText(self.show_result.text()[0:-1])
            print(sign)
            self.write_nummber(sign)

    def write_nummber(self, nummber):
        self.pres_equal = False
        if self.show_result.text() == '0' and not self.checsign(nummber[0]):
            self.show_result.setText(nummber)
        else:
            self.show_result.setText(self.show_result.text() + nummber)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    calculator = QtWidgets.QMainWindow()
    ui = Ui_calculator()
    ui.setupUi(calculator)
    calculator.show()
    sys.exit(app.exec_())
