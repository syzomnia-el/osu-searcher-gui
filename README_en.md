# osu!searcher

A local beatmap searcher for [osu!](https://osu.ppy.sh/), quick for downloaded beatmap searching without startup.


# Feature

- [x] View local beatmaps.
- [x] Filter beatmaps by a keyword.
- [x] Check the duplicate beatmaps.
- [ ] Filter beatmaps by keyword for specific conditions such as sid, name, artist, mapper, etc.

# Usage

1. Install [Python 3](https://www.python.org/downloads/) .
2. Run with the following command: `python <PATH>/main.py`.
3. When using it for the first time, you need to enter the absolute path of the folder where your beatmaps are saved.

# Command

| Commands | Description                                                                            |
|----------|----------------------------------------------------------------------------------------|
| exit     | Exit osu!searcher.                                                                     |
| path     | Reset the saved path of beatmaps.                                                      |
| flush    | Flush the beatmap information cache.                                                   |
| find     | Filter beatmaps by a keyword. If the keyword is empty, all beatmaps will be displayed. |
| check    | Check and display the duplicate beatmaps                                               | 