# Form implementation generated from reading ui file 'interface/Admin_windows/admin_menu.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Admin_menu(object):
    def setupUi(self, Admin_menu):
        Admin_menu.setObjectName("Admin_menu")
        Admin_menu.resize(800, 550)
        Admin_menu.setMinimumSize(QtCore.QSize(800, 550))
        Admin_menu.setMaximumSize(QtCore.QSize(800, 550))
        self.centralwidget = QtWidgets.QWidget(parent=Admin_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 90, 121, 91))
        self.label.setStyleSheet("font-size: 35pt;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 180, 200, 60))
        self.pushButton.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 240, 200, 60))
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 300, 200, 60))
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 60))
        self.pushButton_3.setObjectName("pushButton_3")
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
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        Admin_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Admin_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Admin_menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Admin_menu)
        self.statusbar.setObjectName("statusbar")
        Admin_menu.setStatusBar(self.statusbar)

        self.retranslateUi(Admin_menu)
        QtCore.QMetaObject.connectSlotsByName(Admin_menu)

    def retranslateUi(self, Admin_menu):
        _translate = QtCore.QCoreApplication.translate
        Admin_menu.setWindowTitle(_translate("Admin_menu", "MainWindow"))
        self.label.setText(_translate("Admin_menu", "Меню"))
        self.pushButton.setText(_translate("Admin_menu", "Заселение"))
        self.pushButton_2.setText(_translate("Admin_menu", "База"))
        self.pushButton_3.setText(_translate("Admin_menu", "Личный кабинет"))
