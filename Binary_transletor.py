from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 268)
        MainWindow.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Btn.setGeometry(QtCore.QRect(60, 210, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Btn.setFont(font)
        self.Btn.setStyleSheet("background-color: rgb(172, 255, 149);")
        self.Btn.setObjectName("Btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 291, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Text.setFont(font)
        self.Text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Text.setText("")
        self.Text.setObjectName("Text")
        self.verticalLayout.addWidget(self.Text)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 291, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Line = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Line.setFont(font)
        self.Line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Line.setObjectName("Line")
        self.verticalLayout_2.addWidget(self.Line)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # my variables
        self.function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Бинарный переводчик"))
        self.Btn.setText(_translate("MainWindow", "Перевести"))

    def function(self):
        self.Btn.clicked.connect(lambda: self.print_result())

    def print_result(self):
        line = self.Line.text()
        if line == '0':
            self.Text.setText("Отрицание\n(Отрицательный отзыв)")
        elif line == '1':
            self.Text.setText("Согласие\n(Положительный отзыв)")
        elif line == '10':
            self.Text.setText("Пизда!")
        elif line == '11':
            self.Text.setText("ХУЙ!")
        elif line == '100':
            self.Text.setText("Есть кто в роте?\n(оферы)")
        elif line == '101':
            self.Text.setText("Кто по факультету заступил?")
        elif line == '110':
            self.Text.setText("Идешь на кафедру?")
        elif line == '111':
            self.Text.setText("Как дела?")
        else:
            error = QMessageBox()
            error.setWindowTitle("ERROR!")
            error.setText("Данное слово невозможно перевести")
            error.setDetailedText("Данная комбинация символов не может быть переведена в данной версии переводчика")

            error.exec()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
