# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


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

        self.verticalLayout.addWidget(self.go_to_plan_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def go_to_plan(self, MainWindow):
        print(self.calendar.selectedDate().toPyDate())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.go_to_plan_btn.setText(_translate("MainWindow", "Добавить/посмотреть план"))

