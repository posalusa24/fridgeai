"""Entry point of program."""
import sys


if len(sys.argv) == 2 and sys.argv[1] == "--shell":
    from fridgeai import shell
    shell.init()
else:
    from PyQt5 import QtWidgets, QtCore
    from fridgeai.gui.mainwindow import Ui_MainWindow
    import threading
    from fridgeai import training
    from fridgeai.microblue import MicroBlue
    from datetime import datetime
    import time
    with MicroBlue('cb:46:24:03:3b:2e') as microblue:
        app = QtWidgets.QApplication(sys.argv)
        fridgeai_window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(fridgeai_window)
        fridgeai_window.show()
        thread = threading.Thread(target=training.model_sync)
        thread.daemon = True
        thread.start()

        def microblue_sync():
            while True:
                water = microblue.get("water")
                if water and int(water) > 200:
                    ui.Water.setStyleSheet("QPushButton {\n"
                                           "    color: #FFFFFF;\n" "\n" "    border: 4px solid #FFFFFF;background-color:red;\n"
                                           "    border-radius: 20;\n"
                                           "    }\n"
                                           "")
                else:
                    ui.Water.setStyleSheet("QPushButton {\n""    color: #FFFFFF;\n" "\n" "    border: 4px solid #FFFFFF;\n"
                                           "    border-radius: 20;\n"
                                           "    }\n"
                                           "")
                _translate = QtCore.QCoreApplication.translate
                nowtime = datetime.now().strftime('%H:%M')
                ui.Time.setText(_translate(
                    "MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">{} PM</span></p></body></html>".format(nowtime)))
                temp = microblue.get("temperature")
                ui.temperature.setText(_translate(
                    "MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">{}*C</span></p></body></html>".format(temp)))
                gas = microblue.get("gas")
                ui.gas.setText(_translate(
                    "MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">{}ppm</span></p></body></html>".format(gas)))
                time.sleep(3)
        thread1 = threading.Thread(target=microblue_sync)
        thread1.daemon = True
        thread1.start()
        sys.exit(app.exec_())
