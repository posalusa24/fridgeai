from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnterItem(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("enteritem_window")
        MainWindow.resize(401, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EnterItem = QtWidgets.QLabel(self.centralwidget)
        self.EnterItem.setGeometry(QtCore.QRect(50, 20, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.EnterItem.setFont(font)
        self.EnterItem.setObjectName("EnterItem")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(50, 190, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(200, 190, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.Itemname = QtWidgets.QLineEdit(self.centralwidget)
        self.Itemname.setGeometry(QtCore.QRect(60, 100, 261, 61))
        self.Itemname.setObjectName("Itemname")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.cancel.clicked.connect(lambda: self.closeWindow(MainWindow))
        self.add.clicked.connect(lambda: self.addItem(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EnterItem.setText(_translate("MainWindow", "Enter Item Name"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.add.setText(_translate("MainWindow", "Add"))

    def closeWindow(self, Form):
        Form.hide()

    def addItem(self, text):
        # inventory.add(text)
        text.hide()
