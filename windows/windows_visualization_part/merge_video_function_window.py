from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from windows.windows_visualization_part.window_create_helper import WindowCreateHelper
from work_with_confg.config_handler import ConfigHandler


class MergeVideoFunctionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.function_purpose = 'merge_video'
        config_reader = ConfigHandler()
        self.window_config = config_reader.read_config_file(
            filename='config_function_window')

        self.window_create_helper = WindowCreateHelper()

        self.buttons = {}
        self.label = None

        self.methods_for_button_connect = None

        self.choice_first_file_name = ''
        self.choice_second_file_name = ''

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

    def establish_communication(self, methods_for_button_connect):
        self.methods_for_button_connect = methods_for_button_connect

    def transmit_data(self):
        return self.choice_first_file_name, self.choice_second_file_name

    def setupUi(self):
        self.methods_for_button_connect['choice_1'] = self.get_first_file_name
        self.methods_for_button_connect['choice_2'] = self.get_second_file_name

        self.customize_window()
        self.label = self.create_label()
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = {}
        data_for_buttons = self.window_config[self.function_purpose]['button']
        for key in data_for_buttons:
            data = data_for_buttons[key]
            method_for_connect = self.methods_for_button_connect[key]
            button = self.window_create_helper.create_button(
                parent_widget=self.central_widget,
                data=data, method_for_connect=method_for_connect)
            buttons[key] = button
        return buttons

    def get_first_file_name(self) -> str:
        self.choice_first_file_name = self.get_file_name()

    def get_second_file_name(self) -> str:
        self.choice_second_file_name = self.get_file_name()

    def get_file_name(self):
        return QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '', 'Video (*.mp4)')[0]

    def set_label_text(self, text: str):
        self.label.setText(text)

    def create_label(self):
        data_for_label = self.window_config[self.function_purpose]['label']
        return self.window_create_helper.create_label(
            parent=self.central_widget, data_for_label=data_for_label)

    def customize_window(self):
        data_for_customize = self.window_config[self.function_purpose]['customize']
        self.window_create_helper.customize_window(
            window=self, data_for_customize=data_for_customize)
