from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from windows.windows_visualization_part.window_create_helper import WindowCreateHelper
from work_with_confg.config_handler import ConfigHandler


class ChangeSpeedFunctionWindow(QMainWindow):
    def __init__(self, mode: str):
        self.mode = mode

        super().__init__()
        config_reader = ConfigHandler()
        self.window_config = config_reader.read_config_file(
            filename='config_function_window')

        self.window_create_helper = WindowCreateHelper()

        self.buttons = {}
        self.label = None
        self.spin_box = None

        self.methods_for_button_connect = None

        self.choice_file_name = ''

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

    def establish_communication(self, methods_for_button_connect):
        self.methods_for_button_connect = methods_for_button_connect

    def setupUi(self):
        self.methods_for_button_connect['choice'] = self.get_file_name
        self.customize_window()
        self.label = self.create_label()
        self.buttons = self.create_buttons()
        self.spin_box = self.create_spin_box()

    def transmit_data(self):
        return self.choice_file_name, self.spin_box.value()

    def create_buttons(self):
        buttons = {}
        data_for_buttons = self.window_config[self.mode]['button']
        for key in data_for_buttons:
            data = data_for_buttons[key]
            method_for_connect = self.methods_for_button_connect[key]
            button = self.window_create_helper.create_button(
                parent_widget=self.central_widget,
                data=data, method_for_connect=method_for_connect)
            buttons[key] = button
        return buttons

    def get_file_name(self) -> str:
        self.choice_file_name = QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '', 'Video (*.mp4)')[0]

    def set_label_text(self, text: str):
        self.label.setText(text)

    def create_label(self):
        data_for_label = self.window_config[self.mode]['label']
        return self.window_create_helper.create_label(
            parent=self.central_widget, data_for_label=data_for_label)

    def create_spin_box(self):
        data_for_spin_box = self.window_config[self.mode]['spin_box']
        x, y = data_for_spin_box['position']
        width, height = data_for_spin_box['size']
        spin_box = QtWidgets.QSpinBox(self.central_widget)
        spin_box.setGeometry(QtCore.QRect(x, y, width, height))
        font = QtGui.QFont()
        font.setPointSize(15)
        spin_box.setFont(font)
        spin_box.setAlignment(QtCore.Qt.AlignCenter)
        spin_box.setMinimum(1)
        spin_box.setMaximum(100)
        return spin_box

    def customize_window(self):
        data_for_customize = self.window_config[self.mode]['customize']
        self.window_create_helper.customize_window(
            window=self, data_for_customize=data_for_customize)
