# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_plan_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import datetime
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Create_Dialog(object):
    def setupUi(self, Dialog, selected_date):
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(284, 405)
        self.Dialog.setMinimumSize(QtCore.QSize(284, 405))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dialog.setFont(font)

        self.selected_date = selected_date

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.title_line_edit = QtWidgets.QLineEdit(self.Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.title_line_edit.setFont(font)
        self.title_line_edit.setText("")

        self.title_line_edit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.title_line_edit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.deadline_dateTime_edit = QtWidgets.QDateTimeEdit(self.Dialog)
        self.deadline_dateTime_edit.setObjectName("dateTimeEdit")
        dt = datetime.datetime.combine(self.selected_date.toPyDate(),
                                       datetime.time(hour=datetime.datetime.now().time().hour,
                                                     minute=datetime.datetime.now().time().minute + 1))
        if datetime.date.today().__eq__(self.selected_date.toPyDate()):
            self.deadline_dateTime_edit.setMinimumDateTime(dt)
        else:
            self.deadline_dateTime_edit.setMinimumDate(self.selected_date)
        self.verticalLayout_2.addWidget(self.deadline_dateTime_edit)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.description_text_edit = QtWidgets.QTextEdit(self.Dialog)
        self.description_text_edit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.description_text_edit)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.save_btn = QtWidgets.QPushButton(self.Dialog)
        self.save_btn.setObjectName("pushButton")
        self.save_btn.clicked.connect(self.save_plan)
        self.verticalLayout_5.addWidget(self.save_btn)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def save_plan(self):
        self.create_time = ".".join(str(datetime.datetime.now().date().today()).split("-")) + " " \
                           + str(datetime.datetime.now().time().hour) + ":" \
                           + str(datetime.datetime.now().time().minute) + ":" \
                           + str(datetime.datetime.now().time().second)
        conn = sqlite3.connect("organizer.db")
        cur = conn.cursor()
        if self.title_line_edit.text() != "":
            try:
                cur.execute("INSERT INTO plans VALUES (?,?,?,?,?,?)", (str(self.selected_date.toPyDate()),
                                                                       self.create_time,
                                                                       self.title_line_edit.text(),
                                                                       self.deadline_dateTime_edit.text(),
                                                                       str(self.description_text_edit.toPlainText()),
                                                                       0))
                QtWidgets.QDialog.close(self.Dialog)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('План добавлен')
                msg.setWindowTitle("Success")
                msg.exec_()

            except Exception:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Oops.. something went wrong!')
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Не введено название')
            msg.setWindowTitle("Error")
            msg.exec_()
        conn.commit()
        conn.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название"))
        self.label_2.setText(_translate("Dialog", "Дедлайн"))
        self.label_3.setText(_translate("Dialog", "Описание"))
        self.save_btn.setText(_translate("Dialog", "Сохранить"))
