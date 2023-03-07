import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from add_new_person import Add_New_Person
from chose_window import ChoseWindow

app = QtWidgets.QApplication(sys.argv)
Chose = QtWidgets.QMainWindow()
ui = ChoseWindow()
ui.setupUi(Chose)
Chose.show()


def open_add_new():
    global Add
    Add = QtWidgets.QMainWindow()
    ui = Add_New_Person()
    ui.setupUi(Add)
    Add.show()
    Chose.close()

    def press_btn_save():
        ui.save_info()
        Add.close()
        Chose.show()

    def q_5():
        ui.open_q5()

    def back():
        Add.close()
        Chose.show()

    ui.btn_save_new.clicked.connect(press_btn_save)
    ui.btn_back.clicked.connect(back)
    ui.btn_q5.clicked.connect(q_5)


def open_data():
    import subprocess
    try:
        subprocess.call('list_of_persons.xlsx', shell=True)
    except:
        err = QMessageBox()
        err.setWindowTitle('Ошибка')
        err.setText('Файл пуст, добавте нового пользователя')
        err.exec()


ui.btn_add_new.clicked.connect(open_add_new)
ui.btn_show_data.clicked.connect(open_data)

sys.exit(app.exec_())
