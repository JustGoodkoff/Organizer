# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plan_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from create_plan_dialog import Ui_Create_Dialog
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog, selected_date):
        self.selected_date = selected_date
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 253)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(Dialog)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 240, 85))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 240, 85))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout.addWidget(self.toolBox, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        fselected_date = f"{self.selected_date.day()}" \
                         f".{self.selected_date.month()}" \
                         f".{self.selected_date.year()}"
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(fselected_date)
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.go_to_create_plan_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.go_to_create_plan_btn.setFont(font)
        self.go_to_create_plan_btn.setObjectName("pushButton")
        self.gridLayout.addWidget(self.go_to_create_plan_btn, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)

        self.go_to_create_plan_btn.clicked.connect(self.go_to_create_plan)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def go_to_create_plan(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Create_Dialog()
        ui.setupUi(Dialog, self.selected_date)
        Dialog.show()
        Dialog.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "Page 2"))
        self.go_to_create_plan_btn.setText(_translate("Dialog", "+"))
        self.comboBox.setItemText(0, _translate("Dialog", "Сортировка по времени создания ↑"))
        self.comboBox.setItemText(1, _translate("Dialog", "Сортировка по времени создания ↓"))
        self.comboBox.setItemText(2, _translate("Dialog", "Сортировка по дедлайну ↑"))
        self.comboBox.setItemText(3, _translate("Dialog", "Сортировка по дедлайну ↓"))
