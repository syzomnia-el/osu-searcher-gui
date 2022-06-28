import os
from data import SongList
from config import Configuration


def set_path(conf: Configuration):
    os.system('cls')
    print('path:')
    conf.path = input()


def init():
    conf = Configuration()
    while conf.path is None:
        set_path(conf)
    return conf, SongList(conf.path)


if __name__ == '__main__':
    config, song_list = init()
    try:
        while True:
            os.system('cls')
            print(f'path: {config.path}')
            print('keyword:')
            keyword = input()
            if keyword.endswith('/.'):
                control = keyword.removesuffix('/.')
                if control == 'exit':
                    exit()
                elif control == 'path':
                    set_path(config)
                    config, song_list = init()
                elif control == 'flush':
                    config, song_list = init()
                continue
            else:
                song_list.find(keyword).show()
            os.system('pause')
    except (IOError, KeyboardInterrupt):
        pass
