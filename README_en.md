# osu!searcher

[简体中文](README.md) | **English**

## Introduction

osu!searcher is a local beatmap searcher for [osu!](https://osu.ppy.sh), quick for downloaded beatmap searching without the
startup.

This is the version with GUI built on version 1.0.0.  
If you prefer command-line interaction, get the source code from
the [osu-searcher](https://github.com/syzomnia-el/osu-searcher) repository.

## Features

- [x] View local beatmaps
- [x] Filter beatmaps by keywords
- [x] Check the duplicate beatmaps
- [ ] Filter beatmaps by keywords for specific conditions such as sid, name, artist, mapper, etc.

## Requirements

- [Python 3.7](https://www.python.org/downloads) or later
- [PySide 6](https://doc.qt.io/qtforpython/quickstart.html)

## Download

- Clone the repository:
  ```bash
  git clone https://github.com/syzomnia-el/osu-searcher-gui.git
  ```
- You can also download the source code as a ZIP file.

## Usage

1. Navigate to the directory of osu!searcher.
2. Run the`startup.cmd`(or`startup.sh`) script.
3. When using it for the first time, you need to enter the **absolute** path of the directory where your beatmaps are
   saved.

## License

osu!searcher is licensed under [MIT License](https://opensource.org/licenses/MIT). Please view [license file](LICENSE)
for more information.