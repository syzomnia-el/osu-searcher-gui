# -*- coding: utf-8 -*-
from cli.control import Control


class OSSApplication:
    __control: Control

    def __init__(self) -> None:
        self.__control = Control()

    def run(self):
        self.__control.run()
