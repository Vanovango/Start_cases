from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Aproksimation(object):
    def setupUi(self, Aproksimation):
        Aproksimation.setObjectName("Aproksimation")
        Aproksimation.resize(483, 572)
        self.centralwidget = QtWidgets.QWidget(Aproksimation)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setGeometry(QtCore.QRect(10, 480, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_result.setFont(font)
        self.btn_result.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.btn_result.setObjectName("btn_result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.num_of_variables = QtWidgets.QLineEdit(self.centralwidget)
        self.num_of_variables.setGeometry(QtCore.QRect(310, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_of_variables.setFont(font)
        self.num_of_variables.setObjectName("num_of_variables")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 461, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.variables_x = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.variables_x.setFont(font)
        self.variables_x.setObjectName("variables_x")
        self.verticalLayout.addWidget(self.variables_x)
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.variables_y = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.variables_y.setFont(font)
        self.variables_y.setObjectName("variables_y")
        self.verticalLayout.addWidget(self.variables_y)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(150, 450, 311, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        Aproksimation.setCentralWidget(self.centralwidget)

        self.retranslateUi(Aproksimation)
        QtCore.QMetaObject.connectSlotsByName(Aproksimation)

        # my Variables
        self.function()

        self.learning_rate = 0.001
        self.train_epochs = 1000
        self.num_coefs = 5

        self.n
        self.x
        self.y

        self.X
        self.Y

    def retranslateUi(self, Aproksimation):
        _translate = QtCore.QCoreApplication.translate
        Aproksimation.setWindowTitle(_translate("Aproksimation", "Апроксимация"))
        self.btn_result.setText(_translate("Aproksimation", "Расчитать"))
        self.label.setText(_translate("Aproksimation", "Введите количество точек ->"))
        self.label_1.setText(_translate("Aproksimation", "Введите значениея х через пробел"))
        self.label_2.setText(_translate("Aproksimation", "Введите соостветствующие значения у через пробел"))

    def function(self):
        self.btn_result.clicked.connect(self.count())

    def count(self):
        self.n = int(self.num_of_variables.text())

        self.x = [int(i) for i in self.variables_x.split()]
        self.y = [int(i) for i in self.variables_y.split()]

        tf.compat.v1.disable_eager_execution()
        self.X = tf.compat.v1.placeholder(tf.float32)
        self.Y = tf.compat.v1.placeholder(tf.float32)


if __name__ == "__main__":
    import sys
    import tensorflow as tf
    import numpy as np
    import matplotlib.pyplot as plt

    app = QtWidgets.QApplication(sys.argv)
    Aproksimation = QtWidgets.QMainWindow()
    ui = Ui_Aproksimation()
    ui.setupUi(Aproksimation)
    Aproksimation.show()
    sys.exit(app.exec())
