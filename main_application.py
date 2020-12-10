from typing import List

from windows.windows_logical_part.change_speed_function import ChangeSpeedFunction
from windows.windows_logical_part.merge_video_function import MergeVideoFunction
from windows.windows_logical_part.split_video_function import SplitVideoFunction
from windows.windows_visualization_part.main_window import MainWindow


class MainApplication:
    def __init__(self):
        self.main_window = None

        self.functions_windows = []

    def create_main_window(self):
        self.main_window = MainWindow()

        data = self.get_dict_with_between_str_and_create_function_window()
        self.main_window.establish_communication(match_between_str_and_method=data)

        self.main_window.setupUi()
        self.main_window.show()

    def get_dict_with_between_str_and_create_function_window(self):
        data = {
            "speed_up": self.create_speed_up_function_window,
            "slow_down": self.create_slow_down_function_window,
            "split_video": self.create_split_video_function_window,
            "merge_video": self.create_merge_videos_function_window
        }
        return data

    def create_speed_up_function_window(self):
        change_speed_function = ChangeSpeedFunction(mode='speed_up')
        change_speed_function.create_window()
        change_speed_function.show_window()
        self.functions_windows.append(change_speed_function)

    def create_slow_down_function_window(self):
        change_speed_function = ChangeSpeedFunction(mode='slow_down')
        change_speed_function.create_window()
        change_speed_function.show_window()
        self.functions_windows.append(change_speed_function)

    def create_split_video_function_window(self):
        split_video_function = SplitVideoFunction()
        split_video_function.create_window()
        split_video_function.show_window()
        self.functions_windows.append(split_video_function)

    def create_merge_videos_function_window(self):
        merge_video_function = MergeVideoFunction()
        merge_video_function.create_window()
        merge_video_function.show_window()
        self.functions_windows.append(merge_video_function)


if __name__ == '__main__':
    pass
