# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


from plan_dialog import Ui_Dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 300)
        MainWindow.setMinimumSize(QtCore.QSize(413, 300))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setEnabled(True)
        self.calendar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calendar.setMouseTracking(False)
        self.calendar.setTabletTracking(False)
        self.calendar.setAcceptDrops(False)
        self.calendar.setObjectName("calendar")
        self.verticalLayout.addWidget(self.calendar)
        self.go_to_plan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.go_to_plan_btn.setObjectName("go_to_plan_btn")

        self.go_to_plan_btn.clicked.connect(self.go_to_plan)


        self.connect_to_database()

        self.verticalLayout.addWidget(self.go_to_plan_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def go_to_plan(self):
        fselected_date = f"{self.calendar.selectedDate().day()}" \
                         f".{self.calendar.selectedDate().month()}" \
                         f".{self.calendar.selectedDate().year()}"
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, self.calendar.selectedDate())
        Dialog.show()
        Dialog.exec_()

    def connect_to_database(self):
        conn = sqlite3.connect("organizer.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS plans (
                                                    date text NOT NULL,
                                                    createTime text NOT NULL,
                                                    title text NOT NULL,
                                                    deadline text NOT NULL,
                                                    description text,
                                                    done integer NOT NULL
                                                    );''')
        conn.commit()
        conn.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyOrganizer"))
        self.go_to_plan_btn.setText(_translate("MainWindow", "Добавить/посмотреть план"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
