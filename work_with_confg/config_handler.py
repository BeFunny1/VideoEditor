import json
import os
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class ConfigHandler:
    path_to_dir_with_config: ClassVar[str] = './configs/'
    config_default_backup: ClassVar = {
        'config_main_window':
            {
                "customize": {
                    "window_title": "Окно выбора функции",
                    "window_size": [400, 400]
                },
                "button": {
                    "speed_up": {
                        "text": "Ускорить видео",
                        "position": [100, 60],
                        "size": [200, 50]
                    },
                    "slow_down": {
                        "text": "Замедлить видео",
                        "position": [100, 120],
                        "size": [200, 50]
                    },
                    "split_video": {
                        "text": "Разрезать видео",
                        "position": [100, 180],
                        "size": [200, 50]
                    },
                    "merge_video": {
                        "text": "Склеить видео",
                        "position": [100, 240],
                        "size": [200, 50]
                    }
                }
            },
        'config_function_window':
            {
                "speed_up": {
                    "customize": {
                        "window_title": "Ускорение видео",
                        "window_size": [400, 400]
                    },
                    "button": {
                        "choice": {
                            "text": "Выбрать видео",
                            "position": [100, 60],
                            "size": [200, 50]
                        },
                        "start": {
                            "text": "Начать",
                            "position": [100, 240],
                            "size": [200, 50]
                        }
                    },
                    "spin_box": {
                        "position": [100, 120],
                        "size": [200, 50]
                    },
                    "label": {
                        "position": [100, 180],
                        "size": [200, 50]
                    }
                },
                "slow_down": {
                    "customize": {
                        "window_title": "Замедление видео",
                        "window_size": [400, 400]
                    },
                    "button": {
                        "choice": {
                            "text": "Выбрать видео",
                            "position": [100, 60],
                            "size": [200, 50]
                        },
                        "start": {
                            "text": "Начать",
                            "position": [100, 240],
                            "size": [200, 50]
                        }
                    },
                    "spin_box": {
                        "position": [100, 120],
                        "size": [200, 50]
                    },
                    "label": {
                        "position": [100, 180],
                        "size": [200, 50]
                    }
                },
                "split_video": {
                    "customize": {
                        "window_title": "Разрезать видео",
                        "window_size": [400, 400]
                    },
                    "button": {
                        "choice": {
                            "text": "Выбрать видео",
                            "position": [100, 60],
                            "size": [200, 50]
                        },
                        "start": {
                            "text": "Начать",
                            "position": [100, 240],
                            "size": [200, 50]
                        }
                    },
                    "time_edit": {
                        "position": [100, 120],
                        "size": [200, 50]
                    },
                    "label": {
                        "position": [100, 180],
                        "size": [200, 50]
                    }
                },
                "merge_video": {
                    "customize": {
                        "window_title": "Разрезать видео",
                        "window_size": [400, 400]
                    },
                    "button": {
                        "choice_1": {
                            "text": "Выбрать первое видео",
                            "position": [100, 60], "size": [200, 50]
                        },
                        "choice_2": {
                            "text": "Выбрать второе видео",
                            "position": [100, 120],
                            "size": [200, 50]
                        },
                        "start": {
                            "text": "Начать",
                            "position": [100, 240],
                            "size": [200, 50]
                        }
                    },
                    "label": {
                        "position": [100, 180],
                        "size": [200, 50]
                    }
                }
            }
    }

    def read_config_file(self, filename: str):
        link = self.path_to_dir_with_config + filename
        if not os.path.exists(link):
            try:
                self.create_config_file(link, filename)
            except IOError:
                return self.config_default_backup[filename]
        with open(link, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config

    def create_config_file(self, link: str, filename: str) -> None:
        with open(link, 'w') as file:
            config_content = self.config_default_backup[filename]
            text = json.dumps(config_content)
            file.write(text)
