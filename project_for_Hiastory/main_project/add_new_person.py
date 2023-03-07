from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from qustion_5 import Question_5


class Add_New_Person(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1528, 1160)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(80, 20, 31, 21))
        self.name.setObjectName("name")
        self.L_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.L_Name.setGeometry(QtCore.QRect(120, 20, 251, 21))
        self.L_Name.setText("")
        self.L_Name.setObjectName("L_Name")
        self.QL_1 = QtWidgets.QLabel(self.centralwidget)
        self.QL_1.setGeometry(QtCore.QRect(30, 70, 131, 21))
        self.QL_1.setObjectName("QL_1")
        self.cb_q_1 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_1.setGeometry(QtCore.QRect(250, 61, 221, 31))
        self.cb_q_1.setObjectName("cb_q_1")
        self.QL_2 = QtWidgets.QLabel(self.centralwidget)
        self.QL_2.setGeometry(QtCore.QRect(30, 130, 141, 21))
        self.QL_2.setObjectName("QL_2")
        self.cb_q_2 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_2.setGeometry(QtCore.QRect(250, 130, 221, 21))
        self.cb_q_2.setObjectName("cb_q_2")
        self.QL_3 = QtWidgets.QLabel(self.centralwidget)
        self.QL_3.setGeometry(QtCore.QRect(30, 190, 181, 41))
        self.QL_3.setObjectName("QL_3")
        self.cb_q_3 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_3.setGeometry(QtCore.QRect(250, 190, 221, 31))
        self.cb_q_3.setObjectName("cb_q_3")
        self.QL_4 = QtWidgets.QLabel(self.centralwidget)
        self.QL_4.setGeometry(QtCore.QRect(30, 260, 131, 21))
        self.QL_4.setObjectName("QL_4")
        self.cb_q_4 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_4.setGeometry(QtCore.QRect(250, 260, 221, 31))
        self.cb_q_4.setObjectName("cb_q_4")
        self.QL_5 = QtWidgets.QLabel(self.centralwidget)
        self.QL_5.setGeometry(QtCore.QRect(30, 330, 171, 41))
        self.QL_5.setObjectName("QL_5")
        self.QL_6 = QtWidgets.QLabel(self.centralwidget)
        self.QL_6.setGeometry(QtCore.QRect(30, 410, 161, 61))
        self.QL_6.setObjectName("QL_6")
        self.cb_q_6 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_6.setGeometry(QtCore.QRect(250, 420, 221, 31))
        self.cb_q_6.setObjectName("cb_q_6")
        self.QL_7 = QtWidgets.QLabel(self.centralwidget)
        self.QL_7.setGeometry(QtCore.QRect(30, 510, 151, 41))
        self.QL_7.setObjectName("QL_7")
        self.cb_q_7 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_7.setGeometry(QtCore.QRect(250, 510, 221, 31))
        self.cb_q_7.setObjectName("cb_q_7")
        self.QL_8 = QtWidgets.QLabel(self.centralwidget)
        self.QL_8.setGeometry(QtCore.QRect(30, 570, 151, 21))
        self.QL_8.setObjectName("QL_8")
        self.cb_q_8 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_8.setGeometry(QtCore.QRect(250, 570, 221, 31))
        self.cb_q_8.setObjectName("cb_q_8")
        self.QL_9 = QtWidgets.QLabel(self.centralwidget)
        self.QL_9.setGeometry(QtCore.QRect(30, 630, 191, 41))
        self.QL_9.setObjectName("QL_9")
        self.cb_q_9 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_9.setGeometry(QtCore.QRect(250, 630, 221, 31))
        self.cb_q_9.setObjectName("cb_q_9")
        self.QL_10 = QtWidgets.QLabel(self.centralwidget)
        self.QL_10.setGeometry(QtCore.QRect(30, 700, 211, 71))
        self.QL_10.setObjectName("QL_10")
        self.cb_q_10 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_10.setGeometry(QtCore.QRect(250, 710, 221, 31))
        self.cb_q_10.setObjectName("cb_q_10")
        self.QL_12 = QtWidgets.QLabel(self.centralwidget)
        self.QL_12.setGeometry(QtCore.QRect(530, 60, 261, 71))
        self.QL_12.setObjectName("QL_12")
        self.cb_q_12 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_12.setGeometry(QtCore.QRect(790, 60, 221, 31))
        self.cb_q_12.setObjectName("cb_q_12")
        self.QL_13 = QtWidgets.QLabel(self.centralwidget)
        self.QL_13.setGeometry(QtCore.QRect(530, 160, 231, 71))
        self.QL_13.setObjectName("QL_13")
        self.cb_q_13 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_13.setGeometry(QtCore.QRect(790, 160, 221, 31))
        self.cb_q_13.setObjectName("cb_q_13")
        self.QL_14 = QtWidgets.QLabel(self.centralwidget)
        self.QL_14.setGeometry(QtCore.QRect(530, 259, 251, 61))
        self.QL_14.setObjectName("QL_14")
        self.cb_q_14 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_14.setGeometry(QtCore.QRect(790, 250, 221, 31))
        self.cb_q_14.setObjectName("cb_q_14")
        self.QL_15 = QtWidgets.QLabel(self.centralwidget)
        self.QL_15.setGeometry(QtCore.QRect(530, 350, 221, 41))
        self.QL_15.setObjectName("QL_15")
        self.cb_q_15 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_15.setGeometry(QtCore.QRect(790, 350, 221, 31))
        self.cb_q_15.setObjectName("cb_q_15")
        self.QL_16 = QtWidgets.QLabel(self.centralwidget)
        self.QL_16.setGeometry(QtCore.QRect(530, 430, 241, 61))
        self.QL_16.setObjectName("QL_16")
        self.cb_q_16 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_16.setGeometry(QtCore.QRect(790, 430, 221, 31))
        self.cb_q_16.setObjectName("cb_q_16")
        self.QL_17 = QtWidgets.QLabel(self.centralwidget)
        self.QL_17.setGeometry(QtCore.QRect(530, 520, 251, 111))
        self.QL_17.setObjectName("QL_17")
        self.cb_q_17 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_17.setGeometry(QtCore.QRect(790, 520, 221, 31))
        self.cb_q_17.setObjectName("cb_q_17")
        self.QL_18 = QtWidgets.QLabel(self.centralwidget)
        self.QL_18.setGeometry(QtCore.QRect(530, 660, 251, 41))
        self.QL_18.setObjectName("QL_18")
        self.cb_q_18 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_18.setGeometry(QtCore.QRect(790, 660, 221, 31))
        self.cb_q_18.setObjectName("cb_q_18")
        self.QL_19 = QtWidgets.QLabel(self.centralwidget)
        self.QL_19.setGeometry(QtCore.QRect(530, 740, 241, 51))
        self.QL_19.setObjectName("QL_19")
        self.cb_q_19 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_19.setGeometry(QtCore.QRect(790, 740, 221, 31))
        self.cb_q_19.setObjectName("cb_q_19")
        self.QL_20 = QtWidgets.QLabel(self.centralwidget)
        self.QL_20.setGeometry(QtCore.QRect(1050, 60, 241, 111))
        self.QL_20.setObjectName("QL_20")
        self.cb_q_20 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_20.setGeometry(QtCore.QRect(1310, 60, 221, 31))
        self.cb_q_20.setObjectName("cb_q_20")
        self.QL_21 = QtWidgets.QLabel(self.centralwidget)
        self.QL_21.setGeometry(QtCore.QRect(1050, 210, 191, 71))
        self.QL_21.setObjectName("QL_21")
        self.cb_q_21 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_21.setGeometry(QtCore.QRect(1310, 210, 221, 31))
        self.cb_q_21.setObjectName("cb_q_21")
        self.QL_11 = QtWidgets.QLabel(self.centralwidget)
        self.QL_11.setGeometry(QtCore.QRect(30, 790, 171, 61))
        self.QL_11.setObjectName("QL_11")
        self.cb_q_11 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_q_11.setGeometry(QtCore.QRect(250, 790, 221, 31))
        self.cb_q_11.setObjectName("cb_q_11")
        self.btn_save_new = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_new.setGeometry(QtCore.QRect(1070, 300, 431, 61))
        self.btn_save_new.setObjectName("btn_save_new")
        self.L_Rang = QtWidgets.QLineEdit(self.centralwidget)
        self.L_Rang.setGeometry(QtCore.QRect(670, 20, 221, 21))
        self.L_Rang.setText("")
        self.L_Rang.setObjectName("L_Rang")
        self.rang = QtWidgets.QLabel(self.centralwidget)
        self.rang.setGeometry(QtCore.QRect(570, 20, 121, 21))
        self.rang.setObjectName("rang")
        self.age = QtWidgets.QLabel(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(1100, 20, 81, 16))
        self.age.setObjectName("age")
        self.L_Age = QtWidgets.QLineEdit(self.centralwidget)
        self.L_Age.setGeometry(QtCore.QRect(1200, 20, 221, 20))
        self.L_Age.setObjectName("L_Age")
        self.btn_q5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_q5.setGeometry(QtCore.QRect(250, 330, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_q5.setFont(font)
        self.btn_q5.setObjectName("btn_q5")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(1070, 400, 431, 61))
        self.btn_back.setObjectName("btn_back")

        # combobox TEXT

        self.cb_q_1.addItem('Нет данных')
        self.cb_q_1.addItems(['1)  Высшее военное', '2)  Среднее', '3)  Начальное', '4)  Необразован'])

        self.cb_q_2.addItem('Нет данных')
        self.cb_q_2.addItems(['1)  Да (не менее 1 года)', '2)  Частично (до 1 года)', '3)  Нет'])

        self.cb_q_3.addItem('Нет данных')
        self.cb_q_3.addItems(
            ['1)  Стратегическое звено (23-33 лет)', '2)  Оперативное звено (16-25 лет)', '3)  Тактическое звено (4-18 лет)'])

        self.cb_q_4.addItem('Нет данных')
        self.cb_q_4.addItems(
            ['1)  Стратегическое звено (свыше 8 лет)', '2)  Оперативное звено (3-8 лет)', '3)  Тактическое звено (до 5 лет)'])

        self.cb_q_6.addItem('Нет данных')
        self.cb_q_6.addItems(
            ['1)  Стратегическое звено (45-55 лет)', '2)  Оперативное звено (38-47 лет)', '3)  Тактическое звено (22-45 лет)'])

        self.cb_q_7.addItem('Нет данных')
        self.cb_q_7.addItems(['1)  Стратегическое звено (>5 лет службы)', '2)  Оперативное звено (3-5 лет службы)',
                              '3)  Тактическое звено (0-3 лет службы)'])

        self.cb_q_8.addItem('Нет данных')
        self.cb_q_8.addItems(['1)  Отличное', '2)  Хорошее', '3)  Удовлетворительное', '4)  Недовлетворительное'])

        self.cb_q_9.addItem('Нет данных')
        self.cb_q_9.addItems(
            ['1)  Принятие решения по управлению\n войсками адекватно в \nсложившеися \nстратегической обстановке',
             '2)  Принятие решения по управлению\n войсками соответствует \nвсем основным показателям СУВ',
             '3)  Принятие решения по управлению\n войсками частично соответствует в \nсложившеися \nстратегической обстановке'])

        self.cb_q_10.addItem('Нет данных')
        self.cb_q_10.addItems([
            '1)  Оптимальное использование\n современных методов \nупраления войсками в \nстрогом соответствии \nсо сложившейся \nоперативной обстановкой',
            '2)  Рациональное использование\n современных методов \nупраления войсками в \nстрогом соответствии \nсо сложившейся \nоперативной обстановкой',
            '3)  Использование современных методов \nупраления войсками без учета \nсложившейся оперативной обстановкой'])

        self.cb_q_11.addItem('Нет данных')
        self.cb_q_11.addItems(['1)  Улучшение значений главных \nпоказателей системы\nуправления войсками',
                               '2)  Улучшение значений основных \nпоказателей системы\nуправления войсками',
                               '3)  Улучшение значений дополнительных\nпоказателей системы\nуправления войсками'])

        self.cb_q_12.addItem('Нет данных')
        self.cb_q_12.addItems(['1)  Адекватное принятое \nрешение на операцию',
                               '2)  Рациональное принятое \nрешение на операцию',
                               '3)  Принятое решение на \nпредстоящую операцию\n не полностью соответсвует\n оперативной обстановке'])

        self.cb_q_13.addItem('Нет данных')
        self.cb_q_13.addItems(['1)  ДЛОУ полностью вскрыло \nзамысел(планы) противника на \nпредстоящую операцию',
                               '2)  ДЛОУ не полностью вскрыло \nзамысел(планы) противника на \nпредстоящую операцию',
                               '3)  ДЛОУ частияно вскрыло \nзамысел(планы) противника на \nпредстоящую операцию'])

        self.cb_q_14.addItem('Нет данных')
        self.cb_q_14.addItems(['1)  Принятое решение \nДЛОУ на предстоящую \nоперацию полностью отличается от \nотданных решений',
                               '2)  Принятое решение \nДЛОУ на предстоящую \nоперацию в основном отличается от \nотданных решений',
                               '3)  Принятое решение \nДЛОУ на предстоящую \nоперацию частично отличается от \nотданных решений'])

        self.cb_q_15.addItem('Нет данных')
        self.cb_q_15.addItems(['1)  Своевременно',
                               '2)  Относительно своевременно',
                               '3)  Не своевременно'])

        self.cb_q_16.addItem('Нет данных')
        self.cb_q_16.addItems(['1)  Адекватная оценка и \nприменение своих войск и \nсил в операции',
                               '2)  Рациональная оценка и \nприменение своих войс и \nсил в операции(по основным показателям)',
                               '3)  Приемлимая оценка и \nприменение своих войск и \nсил в операции'])

        self.cb_q_17.addItem('Нет данных')
        self.cb_q_17.addItems(
            ['1)  Взаимодействие в проводимой\nоперации обеспечило выполнение\nпоставленных боевых задач\nв полном объеме',
             '2)  Взаимодействие в проводимой\nоперации обеспечило выполнение\nпоставленных боевых\nзадач в основном',
             '3)  Взаимодействие в проводимой\nоперации обеспечило выполнение\nпоставленных боевых\nзадач частично'])

        self.cb_q_18.addItem('Нет данных')
        self.cb_q_18.addItems([
            '1)  Выдвинутые ДЛОУ предположения \nпо стратегическому\n взаимодействию группировок войск, \nсил и других различных ОСК по ТВД \nпозволяют решить задачи \nрегионального масштаба \nв полном объеме.',
            '2)  Выдвинутые ДЛОУ предположения \nпо стратегическому\n взаимодействию группировок войск, \nсил и других различных ОСК по ТВД \nпозволяют решить задачи \nрегионального масштаба в основном.',
            '3)  Выдвинутые ДЛОУ предположения \nпо стратегическому\n взаимодействию группировок войск, \nсил и других различных ОСК по ТВД \nпозволяют решить задачи \nрегионального масштаба в частично.'])

        self.cb_q_19.addItem('Нет данных')
        self.cb_q_19.addItems([
            '1)  Понимание ДЛОУ высоких \nпатроитических \nцелей и задач стоящих \nперед предстоящей \nоперацией и способность его \nпобудить (мотивировать)\n эти чувства в полном \nсоответствии со сложившейся \nморально-психологической\n обстановкой \nв подчененных войсках и силах',
            '2)  Понимание ДЛОУ высоких \nпатроитических \nцелей и задач стоящих \nперед предстоящей \nоперацией и способность его \nпобудить (мотивировать)\n эти чувства в основном \nсоответствии со сложившейся \nморально-психологической\n обстановкой \nв подчененных войсках и силах',
            '3)  Понимание ДЛОУ высоких \nпатроитических \nцелей и задач стоящих \nперед предстоящей \nоперацией и способность его \nпобудить (мотивировать)\n эти чувства в частичном \nсоответствии со сложившейся \nморально-психологической\n обстановкой \nв подчененных войсках и силах'])

        self.cb_q_20.addItem('Нет данных')
        self.cb_q_20.addItems([
            '1)  Умение ДЛОУ четко, по существу \nв рамках установленного \nвремени сформулировать \nи поставить задачи \nподчиненым войскам и \nсилам на предстоящую \nоперацию и \nосуществить еффективный \nконтроль за \nвыполнением отданных распоряжений',
            '2)  Умение ДЛОУ четко, по существу \nв рамках минимально допустимого \nвремени сформулировать \nи поставить задачи \nподчиненым войскам и \nсилам на предстоящую \nоперацию и \nосуществить еффективный \nконтроль за \nвыполнением отданных распоряжений',
            '3)  Умение ДЛОУ четко, по существу \nв рамках критичного \nвремени (на гране срыва) \nвремени сформулировать \nи поставить задачи \nподчиненым войскам и \nсилам на предстоящую \nоперацию и \nосуществить еффективный \nконтроль за \nвыполнением \nотданных распоряжений'])

        self.cb_q_21.addItem('Нет данных')
        self.cb_q_21.addItems(['1)  Успешное (не менее 3 лет)',
                               '2)  Хорошее (не менее 2 лет)',
                               '3)  Посредственное (не менее 1 года)',
                               '4)  Неудовлетворительное'])

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # my functions
        self.answer_5 = 0
        self.sum_res_score = 0

        self.is_Successful = True
        self.is_Mediocre = True
        self.is_Failed = True
        self.not_Needed = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "ФИО"))
        self.QL_1.setText(_translate("MainWindow", "1. Уровень образования"))
        self.QL_2.setText(_translate("MainWindow", "<html><head/><body><p>2. Наличие боевого опыта</p></body></html>"))
        self.QL_3.setText(_translate("MainWindow",
                                     "<html><head/><body><p>3. Выслуга лет в ВС для работы в</p><p>стратегическом звене управления</p></body></html>"))
        self.QL_4.setText(_translate("MainWindow", "<html><head/><body><p>4. Опыт штабной работы</p></body></html>"))
        self.QL_5.setText(_translate("MainWindow",
                                     "<html><head/><body><p>5. Успешность воинской службы</p><p>на предыдущей должности</p></body></html>"))
        self.QL_6.setText(_translate("MainWindow",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                     "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6. Возраст и его соответствие</p>\n"
                                     "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">определенному уровню в</p>\n"
                                     "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">занимаемой должности</p></body></html>"))
        self.QL_7.setText(_translate("MainWindow",
                                     "<html><head/><body><p>7. Опыт службы на театрах</p><p>военных действий</p></body></html>"))
        self.QL_8.setText(
            _translate("MainWindow", "<html><head/><body><p>8. Степень работоспособности</p></body></html>"))
        self.QL_9.setText(_translate("MainWindow",
                                     "<html><head/><body><p>9. Умение использования современных</p><p>способов управления войсками</p></body></html>"))
        self.QL_10.setText(_translate("MainWindow",
                                      "<html><head/><body><p>10 .<span style=\" font-family:\'JetBrains Mono,monospace\'; color:#000000;\">Использование современных методов</span></p><p><span style=\" font-family:\'JetBrains Mono,monospace\'; color:#000000;\">управления войсками для сокращения</span></p><p><span style=\" font-family:\'JetBrains Mono,monospace\'; color:#000000;\">времени цикла управления</span></p></body></html>"))
        self.QL_12.setText(_translate("MainWindow",
                                      "<html><head/><body><p>12. Умение ДЛОУ (органа управления) правильно</p><p>оценивать оперативную обстановку на</p><p>СН (ТВД) на предстоящую операцию</p></body></html>"))
        self.QL_13.setText(_translate("MainWindow",
                                      "<html><head/><body><p>13. Способность ДЛОУ (органа управления)</p><p>на основе оперативной обстановки</p><p>сформулировать намерения (планы)</p><p>противника</p></body></html>"))
        self.QL_14.setText(_translate("MainWindow",
                                      "<html><head/><body><p>14. Степнь нестандарнтности (оригинальности)</p><p>принятого решения ДЛОУ на предстаящую</p><p>операцию</p></body></html>"))
        self.QL_15.setText(_translate("MainWindow",
                                      "<html><head/><body><p>15. Своевременность принятия решения</p><p>ДЛОУ на предстоящую операцию</p></body></html>"))
        self.QL_16.setText(_translate("MainWindow",
                                      "<html><head/><body><p>16. Оценка и применение своих войск и сил в</p><p>операции в соответствии со сложившейся</p><p>оперативной обстановкой</p></body></html>"))
        self.QL_17.setText(_translate("MainWindow",
                                      "<html><head/><body><p>17. Умение ДЛОУ организовать взаимодействие</p><p>видов вооруженных сил, видов войск,</p><p>специальных войск и других военных</p><p>формирований, находящихся на</p><p>СН (ТВД) в предстоящей операции</p></body></html>"))
        self.QL_18.setText(_translate("MainWindow",
                                      "<html><head/><body><p>18. Умение ДЛОУ организовать взаимодействие</p><p>с соседними ОСК по ТВД </p></body></html>"))
        self.QL_19.setText(_translate("MainWindow",
                                      "<html><head/><body><p>19. Умение ДЛОУ оценить</p><p>маральнопсихологическую обстановку</p></body></html>"))
        self.QL_20.setText(_translate("MainWindow",
                                      "<html><head/><body><p>20. Умение ДЛОУ сформулировать и поставить</p><p>задачи подчиненным, войскам и силам на</p><p>предстоящую операцию и осуществить</p><p>эффективнй контроль за выполнением</p><p>отданных распоряжений</p></body></html>"))
        self.QL_21.setText(_translate("MainWindow",
                                      "<html><head/><body><p>21. Степень эффективности</p><p>функционирования (сработанности)</p><p>оперативной группы ПУ ГК СН (ТВД)</p></body></html>"))
        self.QL_11.setText(_translate("MainWindow",
                                      "<html><head/><body><p>11. Способность использования</p><p>предыдущего боевого и</p><p>воискового опыта</p><p><br/></p></body></html>"))
        self.btn_save_new.setText(_translate("MainWindow", "Сохранить"))
        self.btn_back.setText(_translate("MainWindow", "Назад"))
        self.rang.setText(_translate("MainWindow", "Воинское звание"))
        self.age.setText(_translate("MainWindow", "Дата рождения"))
        self.btn_q5.setText(_translate("MainWindow", "Ответить"))

    def open_q5(self):
        global Q_5
        Q_5 = QtWidgets.QWidget()
        ui = Question_5()
        ui.setupUi(Q_5)
        Q_5.show()

        def go_back():
            peace = 0
            war = 0
            if ui.num_war_unsucssese.text() == '0':
                peace += int(ui.num_peace_1.text())
                peace += int(ui.num_peace_2.text())
                peace += int(ui.num_peace_3.text())
                war += int(ui.num_war_sucssese.text())
            else:
                self.not_Needed = True

            if peace < 4:
                self.not_Needed = True
            elif peace < 5:
                self.is_Successful = False
                self.is_Mediocre = False
            elif peace < 8:
                self.is_Successful = False

            if war < 4:
                self.not_Needed = True
            elif war < 5:
                self.is_Successful = False
                self.is_Mediocre = False
            elif war < 8:
                self.is_Successful = False

            self.answer_5 = peace + war

            Q_5.close()

        ui.btn_q5_save.clicked.connect(go_back)

    def count_result(self):
        sum_res_score = 0

        answer_1 = self.cb_q_1.currentText()
        answer_2 = self.cb_q_2.currentText()
        answer_3 = self.cb_q_3.currentText()
        answer_4 = self.cb_q_4.currentText()
        #answer_5 in global class variable
        answer_6 = self.cb_q_6.currentText()
        answer_7 = self.cb_q_7.currentText()
        answer_8 = self.cb_q_8.currentText()
        answer_9 = self.cb_q_9.currentText()
        answer_10 = self.cb_q_10.currentText()
        answer_11 = self.cb_q_11.currentText()
        answer_12 = self.cb_q_12.currentText()
        answer_13 = self.cb_q_13.currentText()
        answer_14 = self.cb_q_14.currentText()
        answer_15 = self.cb_q_15.currentText()
        answer_16 = self.cb_q_16.currentText()
        answer_17 = self.cb_q_17.currentText()
        answer_18 = self.cb_q_18.currentText()
        answer_19 = self.cb_q_19.currentText()
        answer_20 = self.cb_q_20.currentText()
        answer_21 = self.cb_q_21.currentText()

        if answer_1 == '':
            answer_1 = 'Нет данных'
            self.sum_res_score += (4 + 3 + 2 + 1) / 4
        elif answer_1[0] == '1':
            self.sum_res_score += 4
            answer_1 += ' (4 балла)'
        elif answer_1[0] == '2':
            self.sum_res_score += 3
            answer_1 += ' (3 балла)'
            self.not_Needed = True
        elif answer_1[0] == '3':
            self.sum_res_score += 2
            answer_1 += ' (2 балла)'
            self.not_Needed = True
        elif answer_1[0] == '4':
            self.sum_res_score += 1
            answer_1 += ' (1 балл)'
            self.not_Needed = True

        if answer_2 == '':
            answer_2 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_2[0] == '1':
            self.sum_res_score += 3
            answer_2 += ' (3 балла)'
        elif answer_2[0] == '2':
            self.sum_res_score += 2
            answer_2 += ' (2 балла)'
            self.is_Successful = False
        elif answer_2[0] == '3':
            self.sum_res_score += 1
            answer_2 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_3 == '':
            answer_3 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_3[0] == '1':
            self.sum_res_score += 3
            answer_3 += ' (3 балла)'
        elif answer_3[0] == '2':
            self.sum_res_score += 2
            answer_3 += ' (2 балла)'
            self.not_Needed = True
        elif answer_3[0] == '3':
            self.sum_res_score += 1
            answer_3 += ' (1 балл)'
            self.not_Needed = True

        if answer_4 == '':
            answer_4 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_4[0] == '1':
            self.sum_res_score += 3
            answer_4 += ' (3 балла)'
        elif answer_4[0] == '2':
            self.sum_res_score += 2
            answer_4 += ' (2 балла)'
            self.not_Needed = True
        elif answer_4[0] == '3':
            self.sum_res_score += 1
            answer_4 += ' (1 балл)'
            self.not_Needed = True

        self.sum_res_score += self.answer_5

        if answer_6 == '':
            answer_6 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_6[0] == '1':
            self.sum_res_score += 3
            answer_6 += ' (3 балла)'
        elif answer_6[0] == '2':
            self.sum_res_score += 2
            answer_6 += ' (2 балла)'
            self.not_Needed = True
        elif answer_6[0] == '3':
            self.sum_res_score += 1
            answer_6 += ' (1 балл)'
            self.not_Needed = True

        if answer_7 == '':
            answer_7 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_7[0] == '1':
            self.sum_res_score += 3
            answer_7 += ' (3 балла)'
        elif answer_7[0] == '2':
            self.sum_res_score += 2
            answer_7 += ' (2 балла)'
            self.is_Successful = False
        elif answer_7[0] == '3':
            self.sum_res_score += 1
            answer_7 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_8 == '':
            answer_8 = 'Нет данных'
            self.sum_res_score += (9 + 7 + 5 + 0) / 4
        elif answer_8[0] == '1':
            self.sum_res_score += 9
            answer_8 += ' (4 балла)'
        elif answer_8[0] == '2':
            self.sum_res_score += 7
            answer_8 += ' (3 балла)'
            self.is_Successful = False
        elif answer_8[0] == '3':
            self.sum_res_score += 5
            answer_8 += ' (2 балла)'
            self.is_Successful = False
            self.is_Mediocre = False
        elif answer_8[0] == '4':
            self.sum_res_score += 0
            answer_8 += ' (1 балл)'
            self.not_Needed = True

        if answer_9 == '':
            answer_9 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_9[0] == '1':
            self.sum_res_score += 3
            answer_9 += ' (3 балла)'
        elif answer_9[0] == '2':
            self.sum_res_score += 2
            answer_9 += ' (2 балла)'
            self.is_Successful = False
        elif answer_9[0] == '3':
            self.sum_res_score += 1
            answer_9 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_10 == '':
            answer_10 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_10[0] == '1':
            self.sum_res_score += 3
            answer_10 += ' (3 балла)'
        elif answer_10[0] == '2':
            self.sum_res_score += 2
            answer_10 += ' (2 балла)'
            self.is_Successful = False
        elif answer_10[0] == '3':
            self.sum_res_score += 1
            answer_10 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_11 == '':
            answer_11 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_11[0] == '1':
            self.sum_res_score += 3
            answer_11 += ' (3 балла)'
        elif answer_11[0] == '2':
            self.sum_res_score += 2
            answer_11 += ' (2 балла)'
            self.is_Successful = False
        elif answer_11[0] == '3':
            self.sum_res_score += 1
            answer_11 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_12 == '':
            answer_12 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_12[0] == '1':
            self.sum_res_score += 3
            answer_12 += ' (3 балла)'
        elif answer_12[0] == '2':
            self.sum_res_score += 2
            answer_12 += ' (2 балла)'
            self.is_Successful = False
        elif answer_12[0] == '3':
            self.sum_res_score += 1
            answer_12 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_13 == '':
            answer_13 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_13[0] == '1':
            self.sum_res_score += 3
            answer_13 += ' (3 балла)'
        elif answer_13[0] == '2':
            self.sum_res_score += 2
            answer_13 += ' (2 балла)'
            self.is_Successful = False
        elif answer_13[0] == '3':
            self.sum_res_score += 1
            answer_13 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_14 == '':
            answer_14 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_14[0] == '1':
            self.sum_res_score += 3
            answer_14 += ' (3 балла)'
        elif answer_14[0] == '2':
            self.sum_res_score += 2
            answer_14 += ' (2 балла)'
            self.is_Successful = False
        elif answer_14[0] == '3':
            self.sum_res_score += 1
            answer_14 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_15 == '':
            answer_15 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_15[0] == '1':
            self.sum_res_score += 3
            answer_15 += ' (3 балла)'
        elif answer_15[0] == '2':
            self.sum_res_score += 2
            answer_15 += ' (2 балла)'
            self.is_Successful = False
        elif answer_15[0] == '3':
            self.sum_res_score += 1
            answer_15 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_16 == '':
            answer_16 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_16[0] == '1':
            self.sum_res_score += 3
            answer_16 += ' (3 балла)'
        elif answer_16[0] == '2':
            self.sum_res_score += 2
            answer_16 += ' (2 балла)'
            self.is_Successful = False
        elif answer_16[0] == '3':
            self.sum_res_score += 1
            answer_16 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_17 == '':
            answer_17 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_17[0] == '1':
            self.sum_res_score += 3
            answer_17 += ' (3 балла)'
        elif answer_17[0] == '2':
            self.sum_res_score += 2
            answer_17 += ' (2 балла)'
            self.is_Successful = False
        elif answer_17[0] == '3':
            self.sum_res_score += 1
            answer_17 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_18 == '':
            answer_18 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_18[0] == '1':
            self.sum_res_score += 3
            answer_18 += ' (3 балла)'
        elif answer_18[0] == '2':
            self.sum_res_score += 2
            answer_18 += ' (2 балла)'
            self.is_Successful = False
        elif answer_18[0] == '3':
            self.sum_res_score += 1
            answer_18 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_19 == '':
            answer_19 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_19[0] == '1':
            self.sum_res_score += 3
            answer_19 += ' (3 балла)'
        elif answer_19[0] == '2':
            self.sum_res_score += 2
            answer_19 += ' (2 балла)'
            self.is_Successful = False
        elif answer_19[0] == '3':
            self.sum_res_score += 1
            answer_19 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_20 == '':
            answer_20 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_20[0] == '1':
            self.sum_res_score += 3
            answer_20 += ' (3 балла)'
        elif answer_20[0] == '2':
            self.sum_res_score += 2
            answer_20 += ' (2 балла)'
            self.is_Successful = False
        elif answer_20[0] == '3':
            self.sum_res_score += 1
            answer_20 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False

        if answer_21 == '':
            answer_21 = 'Нет данных'
            self.sum_res_score += (3 + 2 + 1) / 3
        elif answer_21[0] == '1':
            self.sum_res_score += 4
            answer_21 += ' (4 балла)'
        elif answer_21[0] == '2':
            self.sum_res_score += 3
            answer_21 += ' (3 балла)'
        elif answer_21[0] == '3':
            self.sum_res_score += 2
            answer_21 += ' (2 балла)'
            self.is_Successful = False
        elif answer_21[0] == '4':
            self.sum_res_score += 1
            answer_21 += ' (1 балл)'
            self.is_Successful = False
            self.is_Mediocre = False


        res = [answer_1, answer_2, answer_3, answer_4, self.answer_5, answer_6, answer_7, answer_8,
                answer_9, answer_10, answer_11, answer_12, answer_13, answer_14, answer_15, answer_16, answer_17,
                answer_18, answer_19, answer_20, answer_21]

        return res

    def save_info(self):
        from openpyxl import load_workbook

        file_name = 'list_of_persons.xlsx'
        wb = load_workbook(file_name)
        ws = wb['data']

        q_score = self.count_result()

        if self.not_Needed:
            q_score.insert(0, 'Не подходит не под одну из категорий')
            q_score.insert(1, self.sum_res_score)
        else:
            if self.sum_res_score >= 55 and self.is_Successful:
                q_score.insert(0, 'Успешное')
                q_score.insert(1, self.sum_res_score)
            elif self.sum_res_score >= 35 and self.is_Mediocre:
                q_score.insert(0, 'Посредственное')
                q_score.insert(1, self.sum_res_score)
            elif self.is_Failed:
                q_score.insert(0, 'Неуспешное')
                q_score.insert(1, self.sum_res_score)
            else:
                q_score.insert(0, 'Не подходит не под одну из категорий')
                q_score.insert(1, self.sum_res_score)

        person_inf = [self.L_Name.text(), self.L_Rang.text(), self.L_Age.text()]

        if self.L_Name.text() != '':
            ws.append(person_inf + q_score)
        else:
            err = QMessageBox()
            err.setWindowTitle('Ошибка')
            err.setText('Не введино ФИО!\nВведите ФИО или сохронаение не произойдет!')
            err.exec()

        wb.save(file_name)
        wb.close()

