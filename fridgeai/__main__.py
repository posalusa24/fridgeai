"""Entry point of program."""
import sys
from PyQt5 import QtWidgets
from fridgeai import shell
from fridgeai.gui.mainwindow import Ui_MainWindow

if len(sys.argv) == 2 and sys.argv[1] == "--shell":
    shell.init()
else:
    app = QtWidgets.QApplication(sys.argv)
    fridgeai_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup(fridgeai_window)
    fridgeai_window.show()
    sys.exit(app.exec_())
