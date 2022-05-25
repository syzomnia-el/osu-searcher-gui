import json
from json.decoder import JSONDecodeError


class Configuration:
    __CONFIG_PATH: str = 'config.json'
    __config: dict

    def __init__(self):
        try:
            with open(self.__CONFIG_PATH) as f:
                self.__config = json.load(f)
        except (IOError, JSONDecodeError):
            self.reset()

    def reset(self):
        self.__config = {'path': None}
        with open(self.__CONFIG_PATH, 'w') as f:
            json.dump(self.__config, f)

    @property
    def path(self):
        return self.__config['path']

    @path.setter
    def path(self, path: str):
        self.__config['path'] = None if path.strip() == '' else path
        with open(self.__CONFIG_PATH, 'w') as f:
            json.dump(self.__config, f)
