# Form implementation generated from reading ui file 'interface/User_windows/ready_choose.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ready_choose(object):
    def setupUi(self, ready_choose):
        ready_choose.setObjectName("ready_choose")
        ready_choose.resize(800, 550)
        ready_choose.setMinimumSize(QtCore.QSize(800, 550))
        ready_choose.setMaximumSize(QtCore.QSize(800, 550))
        self.centralwidget = QtWidgets.QWidget(parent=ready_choose)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 120, 221, 51))
        self.label.setStyleSheet("font-size: 28pt")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 320, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 370, 331, 51))
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 450, 51, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, -30, 800, 550))
        self.label_9.setMinimumSize(QtCore.QSize(600, 400))
        self.label_9.setMaximumSize(QtCore.QSize(800, 550))
        self.label_9.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(201, 218, 251, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(251, 196, 125, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(251, 231, 125, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(251, 266, 125, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(540, 195, 125, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(540, 230, 125, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(540, 265, 125, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(179, 266, 64, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(179, 231, 62, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(179, 196, 30, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(421, 230, 106, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(421, 265, 110, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(421, 195, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.pushButton_2.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        ready_choose.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ready_choose)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        ready_choose.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ready_choose)
        self.statusbar.setObjectName("statusbar")
        ready_choose.setStatusBar(self.statusbar)

        self.retranslateUi(ready_choose)
        QtCore.QMetaObject.connectSlotsByName(ready_choose)

    def retranslateUi(self, ready_choose):
        _translate = QtCore.QCoreApplication.translate
        ready_choose.setWindowTitle(_translate("ready_choose", "MainWindow"))
        self.label.setText(_translate("ready_choose", "Введите данные"))
        self.pushButton.setText(_translate("ready_choose", "Готово"))
        self.pushButton_2.setText(_translate("ready_choose", "<-"))
        self.label_4.setText(_translate("ready_choose", "Отчество:"))
        self.label_3.setText(_translate("ready_choose", "Фамилия:"))
        self.label_2.setText(_translate("ready_choose", "Имя:"))
        self.label_5.setText(_translate("ready_choose", "Серия паспорта:"))
        self.label_6.setText(_translate("ready_choose", "Номер паспорта:"))
        self.label_7.setText(_translate("ready_choose", "Номер телефона:"))
