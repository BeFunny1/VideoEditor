from video_editor.video_editor import VideoEditor
from windows.windows_visualization_part.split_video_function_window import SplitVideoFunctionWindow


class SplitVideoFunction:
    def __init__(self):
        self.window = None

        self.video_editor = VideoEditor()

    def create_window(self):
        self.window = SplitVideoFunctionWindow()
        self.window.establish_communication({'start': self.start_split_video})
        self.window.setupUi()

    def start_split_video(self):
        path_to_video, time_to_split = self.read_data_from_the_window()
        if path_to_video != '' and time_to_split != '00:00:00':
            self.video_editor.split_video(path_to_video_file=path_to_video, cutting_time=time_to_split)
            self.display_loading_finish_on_window()

    def display_loading_finish_on_window(self):
        self.window.set_label_text(text='✓')

    def read_data_from_the_window(self):
        return self.window.transmit_data()

    def show_window(self):
        self.window.show()
