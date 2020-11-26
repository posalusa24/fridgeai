from fridgeai import camera, ai
from PyQt5 import QtCore, QtGui, QtWidgets
from fridgeai.gui.enteritem import Ui_EnterItem
from fridgeai.gui.predicted import Ui_Predicted


class Ui_MainWindow(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, -60, 511, 801))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setObjectName("listWidget")
        self.Snap = QtWidgets.QPushButton(self.centralwidget)
        self.Snap.setEnabled(True)
        self.Snap.setGeometry(QtCore.QRect(510, 0, 511, 171))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Snap.setFont(font)
        self.Snap.setObjectName("Snap")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setEnabled(True)
        self.Add.setGeometry(QtCore.QRect(510, 170, 511, 171))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Add.setFont(font)
        self.Add.setObjectName("Add")
        self.Scan = QtWidgets.QPushButton(self.centralwidget)
        self.Scan.setEnabled(True)
        self.Scan.setGeometry(QtCore.QRect(510, 330, 511, 171))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Scan.setFont(font)
        self.Scan.setObjectName("Scan")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Snap.clicked.connect(self.takeSnap)
        self.Add.clicked.connect(self.addItem)
        self.Scan.clicked.connect(self.scanObject)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Snap.setText(_translate("MainWindow", "Snap"))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.Scan.setText(_translate("MainWindow", "Scan"))

    def takeSnap(self):
        camera.get_frames(shape=(32, 32), count=5, interval=5)

    def addItem(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_EnterItem()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def scanObject(self):
        while True:
            print("Scanning...")
            label = ai.predict(camera.get_frames(
                (32, 32),
                count=5,
                interval=5))
            print("Scan result: {}".format(label))
            self.prediction = label
            break
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Predicted()
        self.ui.setupUi1(self.MainWindow)
        self.ui.prediction.setText(label)
        self.MainWindow.show()
