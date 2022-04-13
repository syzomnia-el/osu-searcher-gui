import os
from data import SongList
from config import Configuration

if __name__ == '__main__':
    config = Configuration()
    if config.path is None:
        print('path:')
        config.path = input()

    song_list = SongList(config.path)

    try:
        while True:
            os.system('cls')
            print(f'path: {config.path}')
            print('keyword:')
            keyword = input()
            exit() if keyword == 'exit' else song_list.find(keyword).show()
            os.system('pause')
    except (IOError, KeyboardInterrupt):
        pass
