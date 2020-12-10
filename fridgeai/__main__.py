"""Entry point of program."""
import sys

if len(sys.argv) == 2 and sys.argv[1] == "--shell":
    from fridgeai import shell
    shell.init()
else:
    from PyQt5 import QtWidgets
    from fridgeai.gui.mainwindow import Ui_MainWindow
    app = QtWidgets.QApplication(sys.argv)
    fridgeai_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(fridgeai_window)
    fridgeai_window.show()
    sys.exit(app.exec_())
