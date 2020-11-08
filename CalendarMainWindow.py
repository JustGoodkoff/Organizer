import sys

from PyQt5.QtWidgets import QApplication

from calendar_view import *


class CalendarMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = CalendarMainWindow()
    mw.show()
    sys.exit(app.exec())


    # def go_to_plan(self, MainWindow):
    #     print(self.calendar.selectedDate().toPyDate())
    #     dialog = QtWidgets.QDialog(self)
    #     dialog.show()
