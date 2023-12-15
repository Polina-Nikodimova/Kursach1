import sys
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QApplication, QMainWindow

from interface.Welcome_windows.enter_or_reg import Ui_Enter_or_reg
from interface.Welcome_windows.enter import Ui_enter
from interface.Welcome_windows.reg import Ui_Reg

from Code.Admin import AdminMenu
from Code.User import UserMenu
from Code.database import db


class EnterOrReg(QMainWindow):
    def __init__(self):
        """ Конструктор класса EnterOrReg """
        super().__init__()
        self.ui = Ui_Enter_or_reg()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.open_enter_window)
        self.ui.pushButton_2.clicked.connect(self.open_reg_window)

    def open_enter_window(self):
        """ Метод для открытия окна входа """
        self.enter_window = EnterWindow()
        self.enter_window.show()
        self.hide()

    def open_reg_window(self):
        """ Метод для открытия окна регистрации """
        self.reg_window = Reg()
        self.reg_window.show()
        self.hide()


class EnterWindow(QMainWindow):
    def __init__(self):
        """ Конструктор класса EnterWindow """
        super().__init__()
        self.ui = Ui_enter()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.check_enter)
        self.ui.pushButton_2.clicked.connect(self.back)

        self.db = db
        self.query = QSqlQuery()

    def check_enter(self):
        """ Метод для открытия окна меню в зависимости от роли """
        user_login = self.ui.lineEdit.text()
        user_password = self.ui.lineEdit_2.text()

        if len(user_login) == 0:
            self.ui.label_4.setText('Поле логина не должно быть пустым!')
            return

        if len(user_password) == 0:
            self.ui.label_4.setText('Поле пароля не должно быть пустым!')
            return

        self.query.exec(f"SELECT login, password, role FROM User WHERE login='{user_login}'")
        if self.query.first():
            role = self.query.value(2)
            check_pass = self.query.value(1) == user_password
            if check_pass:
                match role:
                    case 'Администратор':
                        self.admin_window = AdminMenu(user_login)
                        self.admin_window.show()
                        self.hide()
                    case 'Пользователь':
                        self.user_window = UserMenu(user_login)
                        self.user_window.show()
                        self.hide()
                    case _:
                        self.ui.label_4.setText('Ошибка авторизации!')
            else:
                self.ui.label_4.setText('Неправильный пароль!')
        else:
            self.ui.label_4.setText('Такого пользователя не существует!')

    def back(self):
        """ Метод для открытия входного окна """
        self.back = EnterOrReg()
        self.back.show()
        self.hide()


class Reg(QMainWindow):
    def __init__(self):
        """ Конструктор класса Reg """
        super().__init__()
        self.ui = Ui_Reg()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.back)

        self.db = db
        self.query = QSqlQuery()

    def reg(self):
        """ Метод для открытия окна меню в зависимости от роли """
        user_login = self.ui.lineEdit.text()
        user_password = self.ui.lineEdit_2.text()
        user_role = self.ui.comboBox.currentText()

        if len(user_login) == 0:
            self.ui.label_5.setText('Поле логина не должно быть пустым!')
            return

        if len(user_password) == 0:
            self.ui.label_5.setText('Поле пароля не должно быть пустым!')
            return

        self.query.exec(f'SELECT login FROM User WHERE login={user_login}')
        self.query.first()
        if self.query.value(0) is None:
            self.query.exec(f"INSERT INTO User(login, password, role)"
                            f"VALUES ('{user_login}', '{user_password}', '{user_role}')")
            match user_role:
                case 'Администратор':
                    self.admin_window = AdminMenu(user_login)
                    self.admin_window.show()
                    self.hide()
                case 'Пользователь':
                    self.user_window = UserMenu(user_login)
                    self.user_window.show()
                    self.hide()
            self.ui.label_5.setText('Аккаунт успешно зарегистрирован!')
        else:
            self.ui.label_5.setText('Такой пользователь уже зарегистрирован!')

    def back(self):
        """ Метод для открытия входного окна """
        self.back = EnterOrReg()
        self.back.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window1 = EnterWindow()
    login_window1.show()
    login_window2 = EnterOrReg()
    login_window2.show()
    login_window3 = Reg()
    login_window3.show()
    sys.exit(app.exec())
