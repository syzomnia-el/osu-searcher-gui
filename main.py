import os
from data import SongList
from config import Configuration


def set_path(configuration: Configuration):
    os.system('cls')
    print('path:')
    configuration.path = input()


def init():
    configuration = Configuration()
    while configuration.path is None:
        set_path(configuration)
    return configuration, SongList(configuration.path)


if __name__ == '__main__':
    config, song_list = init()
    try:
        while True:
            os.system('cls')
            print(f'path: {config.path}')
            print('keyword:')
            keyword = input()
            if keyword == 'exit/.':
                exit()
            elif keyword == 'path/.':
                set_path(config)
                config, song_list = init()
                continue
            else:
                song_list.find(keyword).show()
            os.system('pause')
    except (IOError, KeyboardInterrupt):
        pass
