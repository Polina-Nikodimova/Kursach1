import sys
from PyQt6.QtWidgets import QApplication
from Code.Welcome import EnterOrReg


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window1 = EnterOrReg()
    login_window1.show()
    sys.exit(app.exec())
