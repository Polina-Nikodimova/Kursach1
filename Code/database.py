import os
import sys

from PyQt6.QtSql import QSqlQuery, QSqlDatabase


def db_connect(db_name: str = 'MyDatabase', new_db: bool = False) -> QSqlDatabase:
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(db_name)
    query = QSqlQuery()

    if not db.open():
        print(f"Database Error: {db.lastError().databaseText()}")
        sys.exit(1)

    query.exec('''create table if not exists Rooms(
        id integer primary key,
        name varchar(25) not null,
        amount int,
        price int
    );''')
    query.exec('''create table if not exists User(
        id integer primary key,
        login varchar(50),
        password varchar(50),
        role varchar(25)
    );''')
    query.exec('''create table if not exists Reservation(
        id integer primary key,
        type_id int references Rooms(id),
        id_user int null references User(id),
        FIO varchar(150),
        passport varchar(15),
        phone varchar(20),
        check_in_date varchar(20),
        eviction_date varchar(20),
        price int,
        status varchar(10) default 'Свободен'
        );''')
    if new_db:
        query.exec('''drop table if exists Rooms''')
        query.exec('''create table if not exists Rooms(
        id integer primary key,
        name varchar(25) not null,
        amount int,
        price int
        );''')

        query.exec('''INSERT INTO Rooms(id, name, amount, price) VALUES
            (101,'Стандартный',1, 2500),
            (102,'Стандартный',1, 2500),
            (103, 'Стандартный',2, 3000),
            (104, 'Стандартный',2, 3000),
            (105, 'Стандартный',2, 3000),
            (106, 'Стандартный',3, 3500),
            (107, 'Стандартный',4, 4000),
            (108, 'Стандартный',4, 4000),
            (109, 'Стандартный',5, 5000),
            (110, 'Стандартный',6, 6000),
            (201, 'Улучшенный',1, 4000),
            (202, 'Улучшенный',1, 4000),
            (203, 'Улучшенный',1, 4000),
            (204, 'Улучшенный',2, 5000),
            (205, 'Улучшенный',2, 5000),
            (206, 'Улучшенный',3, 6000),
            (207, 'Улучшенный',4, 7000),
            (208, 'Улучшенный',4, 7000),
            (209, 'Улучшенный',5, 8000),
            (210, 'Улучшенный',6, 9000),
            (301, 'Люкс',1, 5600),
            (302, 'Люкс',1, 5600),
            (303, 'Люкс',1, 5600),
            (304, 'Люкс',1, 5600),
            (305, 'Люкс',2, 7200),
            (306, 'Люкс',2, 7200),
            (307, 'Люкс',2, 7200),
            (308, 'Люкс',3, 8700),
            (309, 'Люкс',4, 9000),
            (310, 'Люкс',5, 10000),
            (401, 'Президентский',1, 16000),
            (402, 'Президентский',1, 16000),
            (403, 'Президентский',1, 16000),
            (404, 'Президентский',1, 16000),
            (405, 'Президентский',1, 16000),
            (406, 'Президентский',2, 20000),
            (407, 'Президентский',3, 26000),
            (408, 'Президентский',3, 26000),
            (409, 'Президентский',4, 30000),
            (410, 'Президентский',5, 33000);
        ''')

    return db


if os.path.exists('Hotel'):
    db = db_connect('Hotel')
else:
    db = db_connect('Hotel', new_db=True)

