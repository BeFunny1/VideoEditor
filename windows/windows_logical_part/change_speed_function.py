import time

from video_editor.video_editor import VideoEditor
from windows.windows_visualization_part.change_speed_function_window import ChangeSpeedFunctionWindow


class ChangeSpeedFunction:
    def __init__(self, mode: str):
        self.window = None
        self.mode = mode

        self.video_editor = VideoEditor()

    def create_window(self):
        self.window = ChangeSpeedFunctionWindow(mode=self.mode)
        self.window.establish_communication({'start': self.start_change_speed})
        self.window.setupUi()

    def start_change_speed(self):
        path_to_video, speed_coefficient = self.read_data_from_the_window()
        if path_to_video != '':
            if self.mode == 'speed_up':
                self.video_editor.speed_up_the_video(
                    path_to_video_file=path_to_video,
                    speed_coefficient=speed_coefficient)
            elif self.mode == 'slow_down':
                self.video_editor.slow_down_the_video(
                    path_to_video_file=path_to_video,
                    slow_coefficient=speed_coefficient)
            self.display_loading_finish_on_window()

    def display_loading_finish_on_window(self):
        self.window.set_label_text(text='✓')

    def read_data_from_the_window(self):
        return self.window.transmit_data()

    def show_window(self):
        self.window.show()



