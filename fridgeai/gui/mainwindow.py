import os
import sqlite3
from fridgeai import camera, ai
from PyQt5 import QtCore, QtGui, QtWidgets
from fridgeai.gui.manual import Ui_Manual
from fridgeai.gui.predict import Ui_predict
from fridgeai.gui.testing import Ui_List


class Ui_MainWindow(object):
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
        self.inventory_wallpaper = QtWidgets.QLabel(self.centralwidget)
        self.inventory_wallpaper.setGeometry(QtCore.QRect(60, 40, 401, 531))
        self.inventory_wallpaper.setText("")
        self.inventory_wallpaper.setPixmap(QtGui.QPixmap("98adaa-2048x1536.png"))
        self.inventory_wallpaper.setObjectName("inventory_wallpaper")
        self.inventor_title = QtWidgets.QLabel(self.centralwidget)
        self.inventor_title.setGeometry(QtCore.QRect(170, 50, 171, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.inventor_title.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.inventor_title.setFont(font)
        self.inventor_title.setObjectName("inventor_title")
        self.vector = QtWidgets.QLabel(self.centralwidget)
        self.vector.setGeometry(QtCore.QRect(90, 140, 341, 2))
        self.vector.setStyleSheet("QLabel{\n"
                                  "background-color:black\n"
                                  "}")
        self.vector.setText("")
        self.vector.setObjectName("vector")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 160, 341, 411))
        self.tableWidget.setStyleSheet("QTableWidget {background: #98ADAA}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(10)

        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(600, 20, 291, 151))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(660, 190, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.temperature.setFont(font)
        self.temperature.setObjectName("temperature")
        self.gas = QtWidgets.QLabel(self.centralwidget)
        self.gas.setGeometry(QtCore.QRect(660, 260, 541, 191))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.gas.setFont(font)
        self.gas.setObjectName("gas")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(540, 460, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Add.setFont(font)
        self.Add.setStyleSheet("QPushButton {\n"
                               "    color: #FFFFFF;\n"
                               "    border: 4px solid #FFFFFF;\n"
                               "    border-radius: 50;\n"
                               "    }\n"
                               "")
        self.ListButton = QtWidgets.QPushButton(self.centralwidget)
        self.ListButton.setGeometry(QtCore.QRect(90, 160, 341, 411))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ListButton.setFont(font)
        self.ListButton.setStyleSheet("QPushButton {\n"
                                      "    \n"
                                      "    border: 0.1px solid #FFFFFF;\n"
                                      "   \n"
                                      "    }\n"
                                      "")
        self.ListButton.setText("")
        self.ListButton.setObjectName("ListButton")

        self.temperature_icon = QtWidgets.QLabel(self.centralwidget)
        self.temperature_icon.setGeometry(QtCore.QRect(550, 210, 101, 71))
        self.temperature_icon.setText("")
        self.temperature_icon.setPixmap(QtGui.QPixmap(os.path.join("data", "temperature-2-64.png")))
        self.temperature_icon.setObjectName("temperature_icon")
        self.pressure_icon = QtWidgets.QLabel(self.centralwidget)
        self.pressure_icon.setGeometry(QtCore.QRect(550, 320, 71, 71))
        self.pressure_icon.setText("")
        self.pressure_icon.setPixmap(QtGui.QPixmap(os.path.join("data", "pressure-64.png")))
        self.pressure_icon.setObjectName("pressure_icon")
        self.learn = QtWidgets.QPushButton(self.centralwidget)
        self.learn.setGeometry(QtCore.QRect(700, 460, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.learn.setFont(font)
        self.learn.setStyleSheet("QPushButton {\n"
                                 "    color: #FFFFFF;\n"
                                 "    border: 4px solid #FFFFFF;\n"
                                 "    border-radius: 50;\n"
                                 "    }\n"
                                 "")
        self.learn.setObjectName("Learn")
        self.Manual = QtWidgets.QPushButton(self.centralwidget)
        self.Manual.setGeometry(QtCore.QRect(860, 460, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Manual.setFont(font)
        self.Manual.setStyleSheet("QPushButton {\n"
                                  "    color: #FFFFFF;\n"
                                  "    border: 4px solid #FFFFFF;\n"
                                  "    border-radius: 50;\n"
                                  "    }\n"
                                  "")
        self.Manual.setObjectName("Manual")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Add.clicked.connect(self.addItem)
        self.learn.clicked.connect(self.learnItem)
        self.Manual.clicked.connect(self.addManual)
        self.ListButton.clicked.connect(self.showInventory)
        connection = sqlite3.connect(os.path.join('data', 'item.db'))
        query = "SELECT name FROM Inventory"
        result = connection.execute(query)
        # self.ListButton.clicked.connect(self.test)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number,
                                         QtWidgets.QTableWidgetItem(str(data)))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.reload)
        self.timer.setInterval(1000)
        self.timer.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inventor_title.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Inventory</span></p></body></html>"))
        self.Time.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">1:18 PM</span></p></body></html>"))
        self.temperature.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">37*F</span></p></body></html>"))
        self.gas.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">2.4psi</span></p></body></html>"))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.learn.setText(_translate("MainWindow", "Learn"))
        self.Manual.setText(_translate("MainWindow", "Manual"))

    def takeSnap(self):
        camera.get_frames(shape=(32, 32), count=5, interval=5)

    def addItem(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_predict()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def reload(self):
        connection = sqlite3.connect(os.path.join('data', 'item.db'))
        query = "SELECT name FROM Inventory"
        result = connection.execute(query)
        # self.ListButton.clicked.connect(self.test)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number,
                                         QtWidgets.QTableWidgetItem(str(data)))

    def learnItem(self):
        print("learn")

    def addManual(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Manual()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def showInventory(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_List()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
