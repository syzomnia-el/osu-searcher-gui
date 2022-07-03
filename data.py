import os
from collections import Counter
from typing import Dict, List


class Song:
    __sid: str
    __author: str
    __name: str

    def __str__(self) -> str:
        return self.to_dict().__str__()

    def __hash__(self) -> int:
        return hash(self.sid)

    def __eq__(self, other) -> bool:
        return self.__sid == other.__sid

    def __contains__(self, x: str) -> bool:
        x = x.lower()
        sid = self.__sid.lower()
        author = self.__author.lower()
        name = self.__name.lower()
        return x in sid or x in author or x in name

    @property
    def sid(self) -> str:
        return self.__sid

    @property
    def author(self) -> str:
        return self.__author

    @property
    def name(self) -> str:
        return self.__name

    @sid.setter
    def sid(self, sid: str):
        self.__sid = sid

    @author.setter
    def author(self, author: str):
        self.__author = author

    @name.setter
    def name(self, name: str):
        self.__name = name

    def to_dict(self) -> Dict[str, str]:
        return {'sid': self.__sid, 'author': self.__author, 'name': self.__name}


class SongList(List[Song]):
    def __init__(self, path: str = None):
        super().__init__()
        if path is not None and os.path.exists(path):
            for i in os.listdir(path):
                try:
                    song = Song()
                    tmp, song.name = i.split(' - ', 1)
                    song.sid, song.author = tmp.split(' ', 1)
                    self.append(song)
                except ValueError:
                    pass

    def __len__(self) -> int:
        return super().__len__()

    def __str__(self) -> str:
        return self.to_list().__str__()

    def __contains__(self, x: str) -> bool:
        for i in self:
            if x in i:
                return True
        return False

    def to_list(self):
        return [i.to_dict() for i in self]

    def show(self):
        print('list:')
        for i in self:
            print(i)
        print(f'total: {len(self)}')

    def find(self, key: str = ''):
        res = SongList()
        for i in self:
            if key in i:
                res.append(i)
        return res

    def check(self):
        counter = dict(Counter(self))
        count = 0
        print('list:')
        for k, v in counter.items():
            if v > 1:
                count += 1
                print(f'{{{k}: {v}}}')
        print(f'total: {count}')
