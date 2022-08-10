import os
from typing import Any, Dict, Tuple

from config import Configuration
from data import SongList


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
            'check': self.check,
            'exit': self.exit,
            'find': self.find,
            'flush': self.flush,
            'list': self.list,
            'path': self.path
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

    def run(self):
        try:
            while True:
                self.clear_screen()
                self.prompt()
                self.parse()
        except (IOError, KeyboardInterrupt):
            exit(1)

    def prompt(self):
        self.print_path()
        print('command:')
        print('-', end=' ')
        for i in self.__commands.keys():
            print(f'{i} <keyword>' if i == 'find' else i, end=' | ')
        print()

    def parse(self):
        command, key = self.read_command()
        if command in self.__commands:
            if command == 'find':
                self.__commands.get(command)(key)
            else:
                self.__commands.get(command)()

    def check(self):
        self.__song_list.check()
        self.pause()

    def find(self, key: str = ''):
        self.__song_list.find(key).show()
        self.pause()

    def flush(self):
        self.__config = Configuration()
        while self.__config.path is None:
            self.set_path()
        self.__song_list = SongList(self.__config.path)

    def list(self):
        self.__song_list.show()
        self.pause()

    def print_path(self):
        print(f'path: {self.__config.path}')

    def set_path(self):
        self.clear_screen()
        self.print_path()
        print('switch to (enter `q` to cancel):')
        args = input().lower()
        if args != 'q':
            self.__config.path = args

    def path(self):
        self.set_path()
        self.flush()

    @staticmethod
    def clear_screen():
        os.system('cls')

    @staticmethod
    def exit():
        exit(0)

    @staticmethod
    def pause():
        os.system('pause')

    @staticmethod
    def read_command() -> Tuple[str, str]:
        args = input().strip().lower().split(' ', 1)
        command = args[0]
        key = args[1].strip() if len(args) == 2 else ''
        return command, key
