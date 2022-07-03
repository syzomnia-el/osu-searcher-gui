import os
from typing import Any, Dict

from data import SongList
from config import Configuration


class Control:
    __instance = None
    __config: Configuration
    __song_list: SongList
    __commands: Dict[str, Any]

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(Control, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__commands = {
            'exit': self.exit,
            'path': self.path,
            'flush': self.flush,
            'check': self.check,
            'find': self.find
        }
        self.flush()

    @property
    def config(self) -> Configuration:
        return self.__config

    @property
    def song_list(self) -> SongList:
        return self.__song_list

    @config.setter
    def config(self, config: Configuration):
        self.__config = config
        while self.__config.path is None:
            self.set_path()
        self.__song_list = SongList(self.__config.path)

    def flush(self):
        self.__config = Configuration()
        while self.__config.path is None:
            self.set_path()
        self.__song_list = SongList(self.__config.path)

    def set_path(self):
        os.system('cls')
        print('path:')
        self.__config.path = input()

    def find(self):
        print('keyword:')
        key = input()
        self.__song_list.find(key).show()
        os.system('pause')

    def exit(self):
        exit()

    def path(self):
        self.set_path()
        self.flush()

    def check(self):
        self.__song_list.check()
        os.system('pause')

    def prompt(self):
        print(f'path: {self.__config.path}')
        print('command:')
        print('-', end=' ')
        for i in self.__commands.keys():
            print(i, end=' | ')
        print()

    def parse(self):
        command = input()
        if command in self.__commands:
            self.__commands.get(command)()

    def run(self):
        try:
            while True:
                os.system('cls')
                self.prompt()
                self.parse()
        except (IOError, KeyboardInterrupt):
            pass
