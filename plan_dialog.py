# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plan_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from create_plan_dialog import Ui_Create_Dialog


class Ui_Dialog(object):
    def setupUi(self, Dialog, selected_date):
        self.selected_date = selected_date
        fselected_date = f"{self.selected_date.day()}" \
                         f".{self.selected_date.month()}" \
                         f".{self.selected_date.year()}"
        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon("calendar.png"))
        Dialog.resize(362, 311)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.go_to_create_plan_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.go_to_create_plan_btn.setFont(font)
        self.go_to_create_plan_btn.setObjectName("pushButton")
        self.gridLayout.addWidget(self.go_to_create_plan_btn, 1, 1, 1, 1)
        self.go_to_create_plan_btn.clicked.connect(self.go_to_create_plan)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(fselected_date)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 2, 1)
        self.comboBox.activated[str].connect(self.onActivated)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)
        conn = sqlite3.connect("organizer.db")
        cur = conn.cursor()
        self.data = cur.execute("SELECT * FROM plans WHERE date=?", (self.selected_date.toPyDate(),)).fetchall()
        self.add_data_to_list_widget(self.data)
        cur.close()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def onActivated(self):
        if self.comboBox.currentIndex() == 0:
            self.listWidget.clear()
            self.data = list(sorted(self.data, key=lambda x: x[1]))
            self.add_data_to_list_widget(self.data)
        elif self.comboBox.currentIndex() == 1:
            self.listWidget.clear()
            self.data = list(sorted(self.data, key=lambda x: x[1], reverse=True))
            self.add_data_to_list_widget(self.data)
        elif self.comboBox.currentIndex() == 2:
            self.listWidget.clear()
            self.data = list(sorted(self.data, key=lambda x: self.format_date(x[3])))
            self.add_data_to_list_widget(self.data)
        elif self.comboBox.currentIndex() == 3:
            self.listWidget.clear()
            self.data = list(sorted(self.data, key=lambda x: self.format_date(x[3]), reverse=True))
            self.add_data_to_list_widget(self.data)

    def format_date(self, date):
        date = date.split()
        date = ".".join(list(reversed(date[0].split(".")))) + date[1]
        return date

    def add_data_to_list_widget(self, data):
        for d in data:
            self.listWidget.addItem("Дедлайн: " + d[3]
                                    + "\n" + "Название: " + d[2]
                                    + "\n" + "Описание: " + d[4])

    def go_to_create_plan(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Create_Dialog()
        ui.setupUi(Dialog, self.selected_date)
        Dialog.show()
        Dialog.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Plan"))
        self.go_to_create_plan_btn.setText(_translate("Dialog", "+"))
        self.comboBox.setItemText(0, _translate("Dialog", "Сортировка по времени создания ↑"))
        self.comboBox.setItemText(1, _translate("Dialog", "Сортировка по времени создания ↓"))
        self.comboBox.setItemText(2, _translate("Dialog", "Сортировка по дедлайну ↑"))
        self.comboBox.setItemText(3, _translate("Dialog", "Сортировка по дедлайну ↓"))
