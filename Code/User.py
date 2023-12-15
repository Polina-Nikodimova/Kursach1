import sys

from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from Code.database import db
from interface.User_windows.user_menu import Ui_User_menu
from interface.User_windows.book_room import Ui_book_room
from interface.User_windows.book_ready import Ui_book_ready
from interface.User_windows.ready_choose import Ui_ready_choose
from interface.User_windows.my_reserv import Ui_My_reserv
from interface.User_windows.personal_area import Ui_personal_area
import re
from datetime import datetime

class UserMenu(QMainWindow):
    def __init__(self, login):
        """ Конструктор класса UserMenu """
        super().__init__()
        self.ui = Ui_User_menu()
        self.ui.setupUi(self)

        self.login = login

        self.ui.pushButton.clicked.connect(self.open_book_room)
        self.ui.pushButton_2.clicked.connect(self.open_personal_area)
        self.ui.pushButton_3.clicked.connect(self.open_my_reserv)

    def open_book_room(self):
        """ Метод для открытия окна выбора номера """
        self.book_room = BookRoom(self.login)
        self.book_room.show()
        self.hide()

    def open_personal_area(self):
        """ Метод для открытия окна личного кабтнета """
        self.personal_area = PersonalArea(self.login)
        self.personal_area.show()
        self.hide()

    def open_my_reserv(self):
        """ Метод для открытия окна с бронями пользователя """
        self.my_reserv = MyReserv(self.login)
        self.my_reserv.show()
        self.hide()


class PersonalArea(QMainWindow):
    def __init__(self, login):
        """ Конструктор класса PersonalArea """
        super().__init__()
        self.ui = Ui_personal_area()
        self.ui.setupUi(self)

        self.login = login
        self.query = QSqlQuery(db)

        self.ui.pushButton.clicked.connect(self.change)
        self.ui.pushButton_2.clicked.connect(self.back)

    def change(self):
        """ Метод для изменения логина и/или пароля """
        new_login = self.ui.lineEdit.text()
        new_password = self.ui.lineEdit_2.text()
        data = [new_login, new_password]
        spisok = ['!', '@', '#', ',', '%', '^', '&', '*', '=', '[', ']', '{', '}',
                  '|', '/', '.', ',', ';', ':', '?', '<', '>', '№']

        if len(new_login) == 0:
            self.ui.label_4.setText('Поле логина не должно быть пустым!')
            return

        if len(new_password) == 0:
            self.ui.label_4.setText('Поле пароля не должно быть пустым!')
            return

        if any(char in spisok for string in data for char in string):
            self.ui.label_4.setText('Поля не должны содержать символы!')
            return

        if len(new_login) > 50:
            self.ui.label_4.setText('Поле логина должно содержать менее 50 символов!')
            return

        if len(new_password) > 50:
            self.ui.label_4.setText('Поле пароля должно содержать менее 50 символов!')
            return

        self.query.exec(f"UPDATE User SET login = '{new_login}', password = '{new_password}'"
                        f"WHERE login = '{self.login}'")
        self.login = new_login
        self.ui.label_4.setText('Данные изменены')

    def back(self):
        """ Метод для открытия окна меню """
        self.back = UserMenu(self.login)
        self.back.show()
        self.hide()


class BookRoom(QMainWindow):
    def __init__(self, login):
        """ Конструктор класса BookRoom """
        super().__init__()
        self.ui = Ui_book_room()
        self.ui.setupUi(self)

        self.login = login

        self.ui.lineEdit.setPlaceholderText('2020-10-10')
        self.ui.lineEdit_2.setPlaceholderText('2020-10-10')

        self.ui.pushButton.clicked.connect(self.open_book_ready)
        self.ui.pushButton_2.clicked.connect(self.back)

    def open_book_ready(self):
        """ Метод для открытия окна с таблицей подходящих номеров """
        check_in_date = self.ui.lineEdit.text()
        eviction_date = self.ui.lineEdit_2.text()
        date = [check_in_date, eviction_date]
        room_type = self.ui.comboBox.currentText()
        amount = int(self.ui.comboBox_2.currentText())

        def validate_date(input_date, date_format='%Y-%m-%d'):
            try:
                validated_date = datetime.strptime(input_date, date_format)
                return True, validated_date
            except ValueError:
                return False, None

        is_valid, formatted_date = validate_date(check_in_date)
        if not is_valid:
            self.ui.label_6.setText('Поле даты заселения содержит недопустимое значение!')

        is_valid, formatted_date = validate_date(eviction_date)
        if not is_valid:
            self.ui.label_6.setText('Поле даты выселения содержит недопустимое значение!')

        if sum(char.isdigit() for char in check_in_date) != 8:
            self.ui.label_6.setText('Поле даты заселения \n содержит недопустимое значение!')
            return
        if sum(char.isdigit() for char in eviction_date) != 8:
            self.ui.label_6.setText('Поле даты выселения \n содержит недопустимое значение!')
            return

        self.book_ready = BookReady(self.login, check_in_date, eviction_date, room_type, amount)
        self.book_ready.show()
        self.hide()

    def back(self):
        """ Метод для открытия окна меню """
        self.back = UserMenu(self.login)
        self.back.show()
        self.hide()


class BookReady(QMainWindow):
    def __init__(self, login, check_in_date, eviction_date, room_type, amount):
        """ Конструктор класса BookReady """
        super().__init__()
        self.ui = Ui_book_ready()
        self.ui.setupUi(self)

        self.eviction_date = eviction_date
        self.check_in_date = check_in_date
        self.login = login

        self.conclusion(room_type, amount)

        self.ui.pushButton.clicked.connect(self.open_ready_choose)
        self.ui.pushButton_2.clicked.connect(self.back)

    def conclusion(self, room_type, amount):
        """ Метод для вывода свободных номеров с определенными характеристиками """
        self.ui.tableWidget.clear()
        self.query = QSqlQuery(db)
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

    def open_ready_choose(self):
        """ Метод для открытия окна бронирования номера """
        cur_row = self.ui.tableWidget.currentRow()
        room = int(self.ui.tableWidget.item(cur_row, 0).text())
        self.ready_choose = ReadyChoose(self.login, self.check_in_date, self.eviction_date, room)
        self.ready_choose.show()
        self.hide()

    def back(self):
        """ Метод для открытия предыдущего окна """
        self.back = BookRoom(self.login)
        self.back.show()
        self.hide()


class ReadyChoose(QMainWindow):
    def __init__(self, login, check_in_date, eviction_date, room):
        """ Конструктор класса ReadyChoose """
        super().__init__()
        self.eviction_date = eviction_date
        self.check_in_date = check_in_date
        self.type_id = room
        self.login = login
        self.ui = Ui_ready_choose()
        self.ui.setupUi(self)

        self.query = QSqlQuery(db)

        self.ui.lineEdit.setPlaceholderText('Name')
        self.ui.lineEdit_2.setPlaceholderText('Surname')
        self.ui.lineEdit_3.setPlaceholderText('Patronymic')
        self.ui.lineEdit_4.setPlaceholderText('+7(990)000-00-00')
        self.ui.lineEdit_5.setPlaceholderText('1234')
        self.ui.lineEdit_6.setPlaceholderText('123456')

        self.ui.pushButton.clicked.connect(self.ready)
        self.ui.pushButton_2.clicked.connect(self.back)

    def ready(self):
        """ Метод для проверки и записи в бд вводимых данных """
        spisok = ['!', '@', '#', ',', '%', '^', '&', '*', '=', '[', ']',
                  '{', '}', '|', '/', '.', ',', ';', ':', '?','<', '>','№']
        name = self.ui.lineEdit.text()
        surname = self.ui.lineEdit_2.text()
        patronymic = self.ui.lineEdit_3.text()
        phone_number = self.ui.lineEdit_4.text()
        seria = self.ui.lineEdit_5.text()
        nomer = self.ui.lineEdit_6.text()
        strings = [name, surname, patronymic, seria, nomer, phone_number]

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
            self.ui.label_8.setText("Ошибка в формате номера телефона +7 (XXX) XXX-XXXX.")

        if sum(char.isdigit() for char in strings) == 0:
            self.ui.label_8.setText('Поля не должны быть пустыми!')
            return
        if any(char in spisok for string in strings for char in string):
            self.ui.label_8.setText('Поля не должны содержать символы!')
            return
        if len(seria) != 4:
            self.ui.label_8.setText('Серия паспорта содержит недопустимое значение!')
            return
        if len(nomer) != 6:
            self.ui.label_8.setText('Номер паспорта содержит недопустимое значение!')
            return
        if sum(char.isdigit() for char in phone_number) != 11:
            self.ui.label_8.setText('Поле номера телефона \n содержит недопустимое значение!')
            return

        self.query.exec(f"SELECT id FROM User WHERE login = '{self.login}'")
        self.query.first()
        self.user_id = self.query.value(0)
        self.query.exec(f"INSERT INTO Reservation(type_id, id_user, FIO, passport, phone, check_in_date, eviction_date)"
                        f"VALUES ('{self.type_id}','{self.user_id}', '{fio}', '{passport}', '{phone_number}',"
                        f"'{self.check_in_date}', '{self.eviction_date}')")
        self.query.exec(f"UPDATE Rooms SET status = 'Занят' WHERE id = {self.type_id}")
        self.ui.label_8.setText(f'Номер успешно зарезервирован!\n'
                                f'Можете перейти в меню и посмотреть свои брони.')

    def back(self):
        """ Метод для открытия окна меню """
        self.back = UserMenu(self.login)
        self.back.show()
        self.hide()


class MyReserv(QMainWindow):
    def __init__(self, login):
        """ Конструктор класса MyReserv """
        super().__init__()
        self.ui = Ui_My_reserv()
        self.ui.setupUi(self)

        self.login = login
        self.query = QSqlQuery(db)

        self.conclusion()

        self.ui.pushButton.clicked.connect(self.delete)
        self.ui.pushButton_2.clicked.connect(self.back)

    def conclusion(self):
        """ Метод для просмотра броней пользователя """
        self.query = QSqlQuery(db)
        self.result = []
        self.query.exec(f"SELECT id FROM User WHERE login = '{self.login}'")
        self.query.first()
        self.user_id = self.query.value(0)
        self.query.exec(f"SELECT RT.id, RT.name, RT.amount, RT.price, "
                        f"R.check_in_date, R.eviction_date "
                        f"FROM Rooms RT JOIN Reservation R ON RT.id = R.type_id "
                        f"WHERE R.id_user = {self.user_id}")

        while self.query.next():
            self.result.append([self.query.value(0), self.query.value(1), self.query.value(2), self.query.value(3),
                                self.query.value(4), self.query.value(5), self.query.value(6)])

        self.ui.tableWidget.setRowCount(len(self.result))
        """ Заполнение таблицы """
        for row, result in enumerate(self.result):
            for column, value in enumerate(result):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, column, item)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Номер', 'Тип', 'Кол-во человек', 'Цена',
                                                       'Дата заселения', 'Дата выселения'])

    def delete(self):
        """ Метод для удаления записи из бд """
        cur_row = self.ui.tableWidget.currentRow()
        room = int(self.ui.tableWidget.item(cur_row, 0).text())
        type_id = self.query.exec(f"SELECT type_id FROM Reservation WHERE id = '{room}'")
        self.query.exec(f"DELETE FROM Reservation WHERE type_id = {room}")
        self.query.exec(f"UPDATE Rooms SET status = 'Свободен' WHERE id = {type_id}")
        self.ui.tableWidget.update()

    def back(self):
        """ Метод для открытия окна меню """
        self.back = UserMenu(self.login)
        self.back.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # login_window1 = Personal_area()
    # login_window1.show()
    # login_window2 = Book_ready()
    # login_window2.show()
    # login_window3 = Book_room()
    # login_window3.show()
    # login_window4 = My_reserv()
    # login_window4.show()
    # login_window5 = Ready_choose()
    # login_window5.show()
    # login_window6 = User_menu()
    # login_window6.show()
    sys.exit(app.exec())
