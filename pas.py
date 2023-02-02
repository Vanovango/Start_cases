from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 279)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.function()
        self.try_num = 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your pasword"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

    def function(self):
        self.pushButton.clicked.connect(lambda: self.window())

    def window(self):
        if self.lineEdit.text() == '12345678':
            out = QMessageBox()
            out.setWindowTitle('Всё OK!!!')
            out.setText('Ваш пaроль подошел! Поздравляю, вы можете продолжить работать!')
            out.exec()

            sys.exit()
        else:
            error = QMessageBox()
            if self.try_num == 0:
                os.system("shutdown -s")
            else:
                error.setWindowTitle('Ошибка')
                error.setText(f'Осталось {self.try_num} попытоки. Вспоминай пароль а то пизда компу!')
                error.exec()

                self.try_num -= 1


if __name__ == "__main__":
    import sys
    import os

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
