# Form implementation generated from reading ui file 'interface/User_windows/personal_area.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_personal_area(object):
    def setupUi(self, personal_area):
        personal_area.setObjectName("personal_area")
        personal_area.resize(800, 550)
        personal_area.setMinimumSize(QtCore.QSize(800, 550))
        personal_area.setMaximumSize(QtCore.QSize(800, 550))
        self.centralwidget = QtWidgets.QWidget(parent=personal_area)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 120, 221, 41))
        self.label.setStyleSheet("font-size: 28pt")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 320, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 185, 321, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setStyleSheet("font-size: 18pt")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("font-size: 18pt")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 450, 51, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 380, 231, 31))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, -30, 800, 550))
        self.label_6.setMinimumSize(QtCore.QSize(600, 400))
        self.label_6.setMaximumSize(QtCore.QSize(800, 550))
        self.label_6.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(201, 218, 251, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.layoutWidget.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        personal_area.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=personal_area)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        personal_area.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=personal_area)
        self.statusbar.setObjectName("statusbar")
        personal_area.setStatusBar(self.statusbar)

        self.retranslateUi(personal_area)
        QtCore.QMetaObject.connectSlotsByName(personal_area)

    def retranslateUi(self, personal_area):
        _translate = QtCore.QCoreApplication.translate
        personal_area.setWindowTitle(_translate("personal_area", "MainWindow"))
        self.label.setText(_translate("personal_area", "Личный кабинет"))
        self.pushButton.setText(_translate("personal_area", "Изменить"))
        self.label_2.setText(_translate("personal_area", "Логин:"))
        self.label_3.setText(_translate("personal_area", "Пароль:"))
        self.pushButton_2.setText(_translate("personal_area", "<-"))
