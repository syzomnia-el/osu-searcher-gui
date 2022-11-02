# -*- coding: utf-8 -*-
import json
from json.decoder import JSONDecodeError
from typing import Any, Dict, NewType


class Configuration:
    __CONFIG_PATH: str = 'config.json'
    __config: dict

    def __init__(self) -> None:
        try:
            with open(self.__CONFIG_PATH) as f:
                self.__config = json.load(f)
        except (IOError, JSONDecodeError):
            self.reset()

    def reset(self) -> None:
        self.__config = {
            'path': None,
            'size': {
                'width': 800,
                'height': 600
            }
        }
        with open(self.__CONFIG_PATH, 'w') as f:
            json.dump(self.__config, f)

    @property
    def path(self) -> str:
        return self.__config['path']

    @path.setter
    def path(self, path: str) -> None:
        path = path.strip()
        self.__config['path'] = None if path == '' else path
        with open(self.__CONFIG_PATH, 'w') as f:
            json.dump(self.__config, f)

    @property
    def size(self) -> NewType('WindowSize', Any):
        size = self.__config['size']
        width = size['width']
        height = size['height']
        return WindowSize(width, height)

    @size.setter
    def size(self, size: NewType('WindowSize', Any)):
        self.__config['size'] = size.to_dict()
        with open(self.__CONFIG_PATH, 'w') as f:
            json.dump(self.__config, f)


class WindowSize:
    __width: int
    __height: int

    def __init__(self, width: int, height: int):
        assert (width >= 0 and height >= 0), 'The width or height of the window cannot be negative.'
        self.__width = width
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @width.setter
    def width(self, width: int):
        assert width >= 0, 'The width of the window cannot be negative.'
        self.__width = width

    @height.setter
    def height(self, height: int):
        assert height >= 0, 'The height of the window cannot be negative.'
        self.__height = height

    def to_dict(self) -> Dict[str, int]:
        return {'width': self.__width, 'height': self.__height}
