from datetime import datetime
from typing import Tuple

import ffmpeg
import uuid


class VideoEditor:
    def speed_up_the_video(
            self, path_to_video_file: str,
            speed_coefficient: int) -> None:
        self.change_video_speed(
            path_to_video_file=path_to_video_file,
            speed_coefficient=speed_coefficient)

    def slow_down_the_video(
            self, path_to_video_file: str,
            slow_coefficient: int) -> None:
        normalized_coefficient = (
            1 / slow_coefficient if slow_coefficient != 0
            else 1)
        self.change_video_speed(
            path_to_video_file=path_to_video_file,
            speed_coefficient=normalized_coefficient)

    def change_video_speed(
            self, path_to_video_file: str,
            speed_coefficient: int) -> None:
        stream = ffmpeg.input(path_to_video_file)
        accelerated_audio_sequence = self.speed_up_the_audio_sequence(
            audio_sequence=stream.audio, speed_coefficient=speed_coefficient)
        accelerated_video_sequence = self.speed_up_the_video_sequence(
            video_sequence=stream.video, speed_coefficient=speed_coefficient)
        video_output = self.connect_video_and_audio_sequences(
            video_sequence=accelerated_video_sequence,
            audio_sequence=accelerated_audio_sequence)
        ffmpeg.run(video_output)

    def connect_video_and_audio_sequences(self, video_sequence, audio_sequence):
        connected_sequences = ffmpeg.concat(video_sequence, audio_sequence, v=1, a=1)
        title_for_video_output = self.generate_title_for_video()
        return ffmpeg.output(connected_sequences, title_for_video_output)

    @staticmethod
    def generate_title_for_video():
        path_to_directory_with_videos = '.\output_videos'
        video_title = str(uuid.uuid4())
        return f'{path_to_directory_with_videos}\\{video_title}.mp4'

    @staticmethod
    def speed_up_the_audio_sequence(audio_sequence, speed_coefficient: int):
        accelerated_audio_sequence = ffmpeg.filter_(audio_sequence, 'atempo', str(speed_coefficient))
        return accelerated_audio_sequence

    def speed_up_the_video_sequence(self, video_sequence, speed_coefficient: int):
        argument_for_setpts = self.form_argument_for_setpts(speed_coefficient=speed_coefficient)
        accelerated_video_sequence = ffmpeg.setpts(video_sequence, argument_for_setpts)
        return accelerated_video_sequence

    @staticmethod
    def form_argument_for_setpts(speed_coefficient: int):
        return str(1 / speed_coefficient) + '*PTS'

    def split_video(
            self, path_to_video_file: str,
            cutting_time: str) -> None:
        stream = ffmpeg.input(path_to_video_file)
        video_duration = self.get_video_duration(path_to_video_file=path_to_video_file)
        cutting_time_in_seconds = self.get_number_seconds_in_time(time_full_format=cutting_time)
        first_part_video = self.crop_video(stream=stream, time_interval=(float(0), cutting_time_in_seconds))
        second_part_video = self.crop_video(stream=stream, time_interval=(cutting_time_in_seconds, video_duration))
        ffmpeg.run(first_part_video)
        ffmpeg.run(second_part_video)

    def crop_video(self, stream, time_interval: Tuple[float, float]):
        video, audio = stream.video, stream.audio
        cropped_video_sequence = ffmpeg.trim(video, start=time_interval[0], end=time_interval[1])
        cropped_video_sequence = ffmpeg.setpts(cropped_video_sequence, 'PTS-STARTPTS')

        cropped_audio_sequence = ffmpeg.filter_(audio, 'atrim', start=time_interval[0], end=time_interval[1])
        cropped_audio_sequence = ffmpeg.filter_(cropped_audio_sequence, 'asetpts', 'PTS-STARTPTS')
        crop_video = self.connect_video_and_audio_sequences(
            video_sequence=cropped_video_sequence, audio_sequence=cropped_audio_sequence)
        return crop_video

    @staticmethod
    def get_video_duration(path_to_video_file: str) -> float:
        return float(ffmpeg.probe(path_to_video_file)["streams"][0]["duration"])

    @staticmethod
    def get_number_seconds_in_time(time_full_format: str) -> int:
        time = datetime.strptime(time_full_format, '%H:%M:%S')
        return float(time.second + time.minute * 60 + time.hour * 3600)

    def merge_video(
            self, path_to_first_video_file: str,
            path_to_second_video_file: str) -> None:
        first_stream = ffmpeg.input(path_to_first_video_file)
        second_stream = ffmpeg.input(path_to_second_video_file)
        merged_videos = ffmpeg.concat(
            first_stream.video, first_stream.audio,
            second_stream.video, second_stream.audio, v=1, a=1)
        title_for_video_output = self.generate_title_for_video()
        merged_video = ffmpeg.output(merged_videos, title_for_video_output)
        ffmpeg.run(merged_video)
