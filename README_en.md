# osu!searcher

A local beatmap searcher for [osu!](https://osu.ppy.sh/), quick for downloaded beatmap searching without startup.

# Feature

- [x] View local beatmaps.
- [x] Filter beatmaps by keywords.
- [x] Check the duplicate beatmaps.
- [ ] Filter beatmaps by keywords for specific conditions such as sid, name, artist, mapper, etc.

# Usage

1. Install [Python 3](https://www.python.org/downloads/) .
2. Run with the following command: `py <PATH>/main.py`.
3. When using it for the first time, you need to enter the absolute path of the folder where your beatmaps are saved.

# Command

| Commands | Description                         |
|----------|-------------------------------------|
| check    | Check the duplicate beatmaps        | 
| exit     | Exit osu!searcher                   |
| find     | Filter beatmaps by keywords         |
| flush    | Flush the beatmap information cache |
| list     | View all local beatmaps             |
| path     | Reset the saved path of beatmaps    |