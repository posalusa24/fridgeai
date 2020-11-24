import sys
from PyQt5 import QtWidgets


def init():
    app = QtWidgets.QApplication([])
    sys.exit(app.exec_())
