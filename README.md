# osu!searcher

**简体中文** | [English](README_en.md)

## 介绍

osu!searcher 是一个为 [osu!](https://osu.ppy.sh) 开发的本地谱面查找工具，无需启动 osu! 即可快速查找已下载的谱面。

这是具有 GUI 的版本。  
如果你更喜欢命令行式交互操作，请从 [main](https://github.com/syzomnia-el/osu-searcher/tree/main) 分支中获取源码。

## 功能

- [x] 查看本地谱面
- [x] 按关键字筛选谱面
- [x] 检查重复的谱面
- [ ] 对特定条件，如谱面编号、歌名、艺术家、谱师等，按关键字筛选谱面

## 要求

- [Python 3.7](https://www.python.org/downloads) 或更高版本
- [PySide 6](https://doc.qt.io/qtforpython/quickstart.html)

## 下载

- 使用以下命令将本仓库复制到本地：
  ```bash
  git clone https://github.com/syzomnia-el/osu-searcher.git -b gui
  ```
- 你也可以通过下载压缩包来获取。

## 使用

1. 打开 osu!searcher 的所在目录。
2. 运行 `startup.cmd`（或 `startup.sh`）脚本。
3. 首次使用时，需要先输入谱面存储目录的**绝对路径**。

## 许可证

osu!searcher 基于 [MIT License](https://opensource.org/licenses/MIT) 授予许可。详情请见[许可证](LICENSE)。