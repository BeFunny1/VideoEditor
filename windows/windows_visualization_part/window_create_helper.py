from typing import Dict

from PyQt5 import QtWidgets, QtCore, QtGui


class WindowCreateHelper:
    @staticmethod
    def create_button(parent_widget, data: Dict, method_for_connect) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton(parent_widget)
        width, height = data['size']
        x, y = data['position']
        button.setGeometry(QtCore.QRect(x, y, width, height))
        button.setText(data['text'])
        button.clicked.connect(method_for_connect)
        return button

    @staticmethod
    def create_label(parent, data_for_label):
        x, y = data_for_label['position']
        width, height = data_for_label['size']
        label = QtWidgets.QLabel(parent)
        label.setGeometry(QtCore.QRect(x, y, width, height))
        font = QtGui.QFont()
        font.setPointSize(15)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    @staticmethod
    def customize_window(window, data_for_customize: Dict):
        window.setWindowTitle(data_for_customize['window_title'])

        width, height = data_for_customize['window_size']
        window.setFixedSize(width, height)
