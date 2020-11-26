from PyQt5 import QtCore, QtGui, QtWidgets
from fridgeai import camera, ai


class Ui_Predicted(object):
    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 140, 381, 131))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.prediction = QtWidgets.QLabel(self.centralwidget)
        self.prediction.setGeometry(QtCore.QRect(320, 290, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.prediction.setFont(font)
        self.prediction.setObjectName("prediction")
        self.rescan = QtWidgets.QPushButton(self.centralwidget)
        self.rescan.setGeometry(QtCore.QRect(70, 410, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rescan.setFont(font)
        self.rescan.setObjectName("pushButton")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(310, 410, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(570, 410, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.add.clicked.connect(self.add)
        self.rescan.clicked.connect(self.rescanItem)
        self.cancel.clicked.connect(lambda: self.closeWindow(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Object Detected !"))
        self.prediction.setText(_translate("MainWindow", "TextLabel"))
        self.rescan.setText(_translate("MainWindow", "Rescan"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))

    def closeWindow(self, Form):
        Form.hide()

    def rescanItem(self):
        while True:
            print("Scanning...")
            label = ai.predict(camera.get_frames(
                (32, 32),
                count=5,
                interval=5))
            print("Scan result: {}".format(label))
            break
        self.prediction.setText(label)
