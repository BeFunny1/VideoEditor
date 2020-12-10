from typing import Dict

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from windows.windows_visualization_part.window_create_helper import WindowCreateHelper
from work_with_confg.config_handler import ConfigHandler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.buttons: Dict[str, QtWidgets.QPushButton] = None

        self.match_between_str_and_method_button_connect = None

        config_reader = ConfigHandler()
        self.window_config = config_reader.read_config_file(
            filename='config_main_window')

        self.window_create_helper = WindowCreateHelper()

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

    def establish_communication(self, match_between_str_and_method: Dict):
        self.match_between_str_and_method_button_connect \
            = match_between_str_and_method

    def setupUi(self):
        self.customize_window()
        self.buttons = self.create_window_buttons()

    def customize_window(self):
        self.window_create_helper.customize_window(
            window=self,
            data_for_customize=self.window_config['customize'])

    def create_window_buttons(self) -> Dict[str, QtWidgets.QPushButton]:
        data_for_buttons = self.window_config['button']
        buttons: Dict[str, QtWidgets.QPushButton] = {}
        for key in data_for_buttons:
            button = self.create_button(
                parent_widget=self.central_widget,
                data=data_for_buttons[key],
                method_for_connect=self.match_between_str_and_method_button_connect[key]
            )
            buttons[key] = button
        return buttons

    def create_button(self, parent_widget, data: Dict, method_for_connect) -> QtWidgets.QPushButton:
        return self.window_create_helper.create_button(
            parent_widget=parent_widget, data=data,
            method_for_connect=method_for_connect)


if __name__ == "__main__":
    pass
