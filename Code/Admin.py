import sys

from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from interface.Admin_windows.admin_menu import Ui_Admin_menu
from interface.Admin_windows.check_in import Ui_Check_in
from interface.Admin_windows.choose import Ui_Choose
from interface.Admin_windows.database import Ui_Database
from interface.Admin_windows.personal_area import Ui_personal_area
from Code.database import db
import re
from datetime import datetime



class AdminMenu(QMainWindow):
    def __init__(self, login):
        """ Конструктор класса AdminMenu """
        super().__init__()
        self.ui = Ui_Admin_menu()
        self.ui.setupUi(self)

        self.login = login

        self.ui.pushButton.clicked.connect(self.open_check_in)
        self.ui.pushButton_2.clicked.connect(self.open_database)
        self.ui.pushButton_3.clicked.connect(self.open_personal_area)

    def open_check_in(self):
        """ Метод для открытия окна входа """
        self.check_in = CheckIn(self.login)
        self.check_in.show()
        self.hide()

    def open_database(self):
        """ Метод для открытия окна с базой данной """
        self.database = Database(self.login)
        self.database.show()
        self.hide()

    def open_personal_area(self):
        """ Метод для открытия окна личного кабинета """
        self.personal_area = PersonalArea(self.login)
        self.personal_area.show()
        self.hide()


class CheckIn(QMainWindow):
    def __init__(self, login):
        """ Конструктор класса CheckIn """
        super().__init__()
        self.query = QSqlQuery(db)
        self.ui = Ui_Check_in()
        self.ui.setupUi(self)

        self.login = login

        self.ui.pushButton.clicked.connect(self.ok)
        self.ui.pushButton_2.clicked.connect(self.choose)
        self.ui.pushButton_3.clicked.connect(self.back)

    def ok(self):
        """ Метод для вывода свободных номеров с определенными характеристиками """
        self.ui.tableWidget.clear()
        self.query = QSqlQuery(db)
        room_type = self.ui.comboBox.currentText()
        amount = int(self.ui.comboBox_2.currentText())
        self.result = []
        self.query.exec(f"SELECT id, name, price FROM Rooms "
                        f"WHERE name='{room_type}' and amount={amount} and status='Свободен'")
        while self.query.next():
            self.result.append([int(self.query.value(0)), self.query.value(1), int(self.query.value(2))])

        self.ui.tableWidget.setRowCount(len(self.result))
        """ Заполнение таблицы """
        for row, result in enumerate(self.result):
            for column, value in enumerate(result):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, column, item)
        self.ui.tableWidget.setHorizontalHeaderLabels(['№', 'Тип', 'Цена'])

    def choose(self):
        """ Метод для открытия окна регистрации гостя """
        self.choose = Choose(self.login, self.result[0][0])
        self.choose.show()
        self.hide()

    def back(self):
        """ Метод для открытия предыдущего окна """
        self.back = AdminMenu(self.login)
        self.back.show()
        self.hide()


class Choose(QMainWindow):
    def __init__(self, login, room_type_id):
        """ Конструктор класса Choose """
        super().__init__()
        self.ui = Ui_Choose()
        self.ui.setupUi(self)

        self.login = login
        self.type_id = room_type_id
        self.query = QSqlQuery(db)

        self.ui.lineEdit.setPlaceholderText('Name')
        self.ui.lineEdit_2.setPlaceholderText('Surname')
        self.ui.lineEdit_3.setPlaceholderText('Patronymic')
        self.ui.lineEdit_7.setPlaceholderText('1234')
        self.ui.lineEdit_8.setPlaceholderText('123456')
        self.ui.lineEdit_4.setPlaceholderText('+7(990)000-0000')
        self.ui.lineEdit_5.setPlaceholderText('2020-10-10')
        self.ui.lineEdit_6.setPlaceholderText('2020-10-10')

        self.ui.pushButton.clicked.connect(self.ready)
        self.ui.pushButton_2.clicked.connect(self.back)

    def ready(self):
        """ Метод для проверки и записи в бд вводимых данных """
        spisok = ['!', '@', '#', ',', '%', '^', '&', '*', '=', '[', ']', '{', '}',
                  '|', '/', '.', ',', ';', ':', '?', '<', '>', '№']
        name = self.ui.lineEdit.text()
        surname = self.ui.lineEdit_2.text()
        patronymic = self.ui.lineEdit_3.text()
        seria = self.ui.lineEdit_7.text()
        nomer = self.ui.lineEdit_8.text()
        phone_number = self.ui.lineEdit_4.text()
        start_date = self.ui.lineEdit_5.text()
        end_date = self.ui.lineEdit_6.text()
        strings = [name, surname, patronymic, seria, nomer, phone_number, start_date, end_date]

        fio = f"{name} {surname} {patronymic}"
        passport = f"{seria} {nomer}"

        def validate_phone_number(phone_number):
            # Шаблон для проверки номера телефона: +7 (XXX) XXX-XXXX
            phone_pattern = re.compile(r'^\+7 \(\d{3}\) \d{3}-\d{4}$')

            # Проверяем соответствие номера телефона шаблону
            if phone_pattern.match(phone_number):
                return True
            else:
                return False

        if not validate_phone_number(phone_number):
            self.ui.label_11.setText("Ошибка в формате номера телефонаt +7 (XXX) XXX-XXXX.")

        def validate_date(input_date, date_format='%Y-%m-%d'):
            try:
                validated_date = datetime.strptime(input_date, date_format)
                return True, validated_date
            except ValueError:
                return False, None

        is_valid, formatted_date = validate_date(start_date)
        if not is_valid:
            self.ui.label_11.setText('Поле даты заселения содержит недопустимое значение!')

        is_valid, formatted_date = validate_date(end_date)
        if not is_valid:
            self.ui.label_11.setText('Поле даты выселения содержит недопустимое значение!')

        if sum(char.isdigit() for char in strings) == 0:
            self.ui.label_11.setText('Поля не должны быть пустыми!')
            return
        if any(char in spisok for string in strings for char in string):
            self.ui.label_11.setText('Поля не должны содержать символы!')
            return
        if len(seria) != 4:
            self.ui.label_11.setText('Серия паспорта содержит недопустимое значение!')
            return
        if len(nomer) != 6:
            self.ui.label_11.setText('Номер паспорта содержит недопустимое значение!')
            return
        if sum(char.isdigit() for char in phone_number) != 11:
            self.ui.label_11.setText('Поле номера телефона содержит недопустимое значение!')
            return
        if sum(char.isdigit() for char in start_date) != 8:
            self.ui.label_11.setText('Поле даты заселения содержит недопустимое значение!')
            return
        if sum(char.isdigit() for char in end_date) != 8:
            self.ui.label_11.setText('Поле даты выселения содержит недопустимое значение!')
            return

        self.query.exec(f"INSERT INTO Reservation(type_id, FIO, passport, phone, check_in_date, eviction_date)"
                        f"VALUES ('{self.type_id}','{fio}', '{passport}', '{phone_number}', "
                        f"'{start_date}', '{end_date}')")
        self.query.exec(f"UPDATE Rooms SET status = 'Занят' WHERE id = {self.type_id}")
        self.ui.label_11.setText(f'Номер успешно зарезервирован!\n'
                                 f'Для просмотра перейдите в базу данных.')

    def back(self):
        """ Метод для открытия окна меню """
        self.back = AdminMenu(self.login)
        self.back.show()
        self.hide()


class Database(QMainWindow):
    def __init__(self, login):
        """ Конструктор класса Database """
        super().__init__()
        self.ui = Ui_Database()
        self.ui.setupUi(self)

        self.login = login
        self.query = QSqlQuery(db)

        self.get_data()

        self.ui.pushButton_3.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.delete)

    def back(self):
        """ Метод для открытия окна меню """
        self.back = AdminMenu(self.login)
        self.back.show()
        self.hide()

    def get_data(self):
        """ Метод для просмотра базы данных """
        self.ui.tableWidget.clear()
        self.result = []
        self.query.exec(f"SELECT RT.id, RT.name, RT.price, R.FIO, R.passport, R.check_in_date, R.eviction_date "
                        f"FROM Rooms RT lEFT JOIN main.Reservation R ON RT.id = R.type_id")
        while self.query.next():
            self.result.append([self.query.value(0), self.query.value(1), self.query.value(2), self.query.value(3),
                                self.query.value(4), self.query.value(5), self.query.value(6)])

        self.ui.tableWidget.setRowCount(len(self.result))
        self.ui.tableWidget.setHorizontalHeaderLabels(['№', 'Тип', 'Цена', 'ФИО', 'Паспортные данные',
                                                       'Дата заселения', 'Дата выселения'])
        """ Заполнение таблицы """
        for row, result in enumerate(self.result):
            for column, value in enumerate(result):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, column, item)
        self.ui.tableWidget.resizeColumnsToContents()

    def delete(self):
        """ Метод для удаления записи из бд """
        cur_row = self.ui.tableWidget.currentRow()
        room = int(self.ui.tableWidget.item(cur_row, 0).text())
        type_id = self.query.exec(f"SELECT type_id FROM Reservation WHERE id = '{room}'")
        self.query.exec(f"DELETE FROM Reservation WHERE type_id = {room}")
        self.query.exec(f"UPDATE Rooms SET status = 'Свободен' WHERE id = {type_id}")
        self.ui.tableWidget.update()


class PersonalArea(QMainWindow):
    def __init__(self, login):
        """ Конструктор класса PersonalArea """
        super().__init__()
        self.ui = Ui_personal_area()
        self.ui.setupUi(self)

        self.login = login

        self.query = QSqlQuery(db)

        self.ui.pushButton_5.clicked.connect(self.change)
        self.ui.pushButton_4.clicked.connect(self.back)

    def change(self):
        """ Метод для изменения логина и/или пароля """
        new_login = self.ui.lineEdit_3.text()
        new_password = self.ui.lineEdit_4.text()
        data = [new_login, new_password]
        spisok = ['!', '@', '#', ',', '%', '^', '&', '*', '=', '[', ']', '{', '}',
                  '|', '/', '.', ',', ';', ':', '?', '<', '>', '№']

        if len(new_login) == 0:
            self.ui.label_1.setText('Поле логина не должно быть пустым!')
            return

        if len(new_password) == 0:
            self.ui.label_1.setText('Поле пароля не должно быть пустым!')
            return

        if any(char in spisok for string in data for char in string):
            self.ui.label_1.setText('Поля не должны содержать символы!')
            return

        if len(new_login) > 50:
            self.ui.label_1.setText('Поле логина должно содержать менее 50 символов!')
            return

        if len(new_password) > 50:
            self.ui.label_1.setText('Поле пароля должно содержать менее 50 символов!')
            return

        self.query.exec(f"UPDATE User SET login = '{new_login}', password = '{new_password}'"
                        f"WHERE login = '{self.login}'")
        self.login = new_login
        self.ui.label_1.setText('Данные изменены')

    def back(self):
        """ Метод для открытия окна меню """
        self.back = AdminMenu(self.login)
        self.back.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # login_window1 = Admin_menu()
    # login_window1.show()
    # login_window2 = Check_in()
    # login_window2.show()
    # login_window3 = Choose()
    # login_window3.show()
    # login_window4 = Database()
    # login_window4.show()
    # login_window5 = Personal_area()
    # login_window5.show()
    sys.exit(app.exec())
