import sys

from PyQt5 import QtWidgets

from main_application import MainApplication

if __name__ == '__main__':
    application_for_window = QtWidgets.QApplication(sys.argv)
    app = MainApplication()
    app.create_main_window()
    application_for_window.exec_()
