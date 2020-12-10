# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draft.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os


class Ui_List(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wallpaper = QtWidgets.QLabel(self.centralwidget)
        self.wallpaper.setGeometry(QtCore.QRect(-7, -5, 1931, 1080))
        self.wallpaper.setStyleSheet("QLabel{\n"
                                     "    background-color:\"#1D283D\"\n"
                                     "}")
        self.wallpaper.setText("")
        self.wallpaper.setObjectName("wallpaper")
        self.inventory_list = QtWidgets.QListView(self.centralwidget)
        self.inventory_list.setGeometry(QtCore.QRect(10, 10, 1001, 581))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.inventory_list.setFont(font)
        self.inventory_list.setStyleSheet("QListView\n"
                                          "{background: #98ADAA}")
        self.inventory_list.setMidLineWidth(0)
        self.inventory_list.setTabKeyNavigation(False)
        self.inventory_list.setAlternatingRowColors(True)
        self.inventory_list.setProperty("isWrapping", False)
        self.inventory_list.setObjectName("inventory_list")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 55, 1001, 581))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")  # 98ADAA
        self.tableWidget.setStyleSheet("QTableWidget""{background:#98ADAA}")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(886, 9, 125, 46))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "QPushButton"
            "{background: #DD5145; color : #FFFFFF; font-size: 20px}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.closeWindow(MainWindow))

        self.TEST = QtWidgets.QLabel(self.centralwidget)
        self.TEST.setGeometry(QtCore.QRect(18, 15, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TEST.setFont(font)
        self.TEST.setObjectName("TEST")

        self.TEST1 = QtWidgets.QLabel(self.centralwidget)
        self.TEST1.setGeometry(QtCore.QRect(238, 15, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TEST1.setFont(font)
        self.TEST1.setObjectName("TEST1")

        self.TEST2 = QtWidgets.QLabel(self.centralwidget)
        self.TEST2.setGeometry(QtCore.QRect(450, 15, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TEST2.setFont(font)
        self.TEST2.setObjectName("TEST1")

        self.TEST3 = QtWidgets.QLabel(self.centralwidget)
        self.TEST3.setGeometry(QtCore.QRect(670, 15, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TEST3.setFont(font)
        self.TEST3.setObjectName("TEST1")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        connection = sqlite3.connect(os.path.join('data', 'item.db'))
        query = "SELECT * FROM Inventory"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number,
                                         QtWidgets.QTableWidgetItem(str(data)))
                self.tableWidget.setColumnWidth(colum_number, 219)
                self.btn = QtWidgets.QPushButton(self.tableWidget)
                self.btn.setText('X')
                self.btn.setStyleSheet(
                    "QPushButton"
                    "{background: #DD5145; color : #FFFFFF; font-size: 25px}")
                self.tableWidget.setCellWidget(row_number, 4, self.btn)
                self.btn.clicked.connect(lambda: self.test(
                    self.tableWidget.currentRow(), MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.TEST.setText(_translate("MainWindow", "ID"))
        self.TEST1.setText(_translate("MainWindow", "Name"))
        self.TEST2.setText(_translate("MainWindow", "EntryDate"))
        self.TEST3.setText(_translate("MainWindow", "EndDate"))

    def test(self, data, form):
        item_id = (self.tableWidget.item(data, 0)).text()
        conn = sqlite3.connect(os.path.join('data', 'item.db'))
        c = conn.cursor()
        query = 'delete from Inventory where id='+item_id
        c.execute(query)
        conn.commit()
        form.hide()

    def closeWindow(self, Form):
        Form.hide()