from video_editor.video_editor import VideoEditor
from windows.windows_visualization_part.merge_video_function_window import MergeVideoFunctionWindow


class MergeVideoFunction:
    def __init__(self):
        self.window = None

        self.video_editor = VideoEditor()

    def create_window(self):
        self.window = MergeVideoFunctionWindow()
        self.window.establish_communication({'start': self.start_split_video})
        self.window.setupUi()

    def start_split_video(self):
        path_to_first_video, path_to_second_video = self.read_data_from_the_window()
        if path_to_first_video != '' and path_to_second_video != '':
            self.video_editor.merge_video(
                path_to_first_video_file=path_to_first_video,
                path_to_second_video_file=path_to_second_video)
            self.display_loading_finish_on_window()

    def display_loading_finish_on_window(self):
        self.window.set_label_text(text='✓')

    def read_data_from_the_window(self):
        return self.window.transmit_data()

    def show_window(self):
        self.window.show()
