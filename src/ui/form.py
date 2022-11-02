# -*- coding: utf-8 -*-
from typing import List

from PySide6.QtCore import QSize
from PySide6.QtGui import QCloseEvent, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget

from conf.config import Configuration, WindowSize
from data.data import Song, SongList
from ui.gui import Ui_Form


class OSSForm(QWidget):
    __HORIZONTAL_HEADER_LABELS: List[str]
    __ui: Ui_Form
    __config: Configuration
    __song_list: SongList

    def __init__(self) -> None:
        super().__init__()
        self.__HORIZONTAL_HEADER_LABELS = list(Song().to_dict().keys())
        self.load_ui()
        self.connect_actions()
        self.load_config()
        self.resize(QSize(self.__config.size.width, self.__config.size.height))

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
            self.select_path()
            self.set_path()
        self.__song_list = SongList(self.__config.path)

    def load_ui(self):
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)

    def connect_actions(self):
        self.__ui.pathButton.clicked.connect(self.select_path)
        self.__ui.flushButton.clicked.connect(self.flush)
        self.__ui.findButton.clicked.connect(self.find)
        self.__ui.showButton.clicked.connect(self.list)
        self.__ui.checkButton.clicked.connect(self.check)

    def load_config(self):
        self.config = Configuration()
        self.__ui.pathEdit.setText(self.__config.path)

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Warn', 'Exit?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if not self.isMaximized():
                self.__config.size = WindowSize(self.width(), self.height())
            event.accept()
        else:
            event.ignore()

    def set_path(self):
        self.__config.path = self.__ui.pathEdit.text().strip().lower()

    def select_path(self):
        path = QFileDialog.getExistingDirectory(self.__ui.gridLayoutWidget, u'Select the path of beatmaps saved')
        if path != '':
            self.__ui.pathEdit.setText(path.strip().lower())

    def reload_ui(self):
        self.__ui.findEdit.setText('')
        self.__ui.beatmapCountLabel.setText('(0)')
        self.__ui.beatmapView.setModel(QStandardItemModel())
        self.__ui.checkedBeatmapCountLabel.setText('(0)')
        self.__ui.checkedBeatmapView.setModel(QStandardItemModel())

    def flush(self):
        self.set_path()
        self.load_config()
        self.reload_ui()

    def load_beatmap(self, song_list: SongList):
        model = self.get_model(song_list)
        self.__ui.beatmapView.setModel(model)
        self.__ui.beatmapCountLabel.setText(f'({len(song_list)})')

    def find(self):
        keyword = self.__ui.findEdit.text()
        self.load_beatmap(self.__song_list.find(keyword))

    def list(self):
        self.reload_ui()
        self.load_beatmap(self.__song_list)

    def load_checked_beatmap(self, song_list: SongList):
        model = self.get_model(song_list)
        self.__ui.checkedBeatmapView.setModel(model)
        self.__ui.checkedBeatmapCountLabel.setText(f'({len(song_list)})')

    def check(self):
        self.flush()
        self.load_checked_beatmap(self.__song_list.check())

    def get_model(self, song_list: SongList) -> QStandardItemModel:
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(self.__HORIZONTAL_HEADER_LABELS)
        for i, v in enumerate(song_list.to_list()):
            for j, elem in enumerate(v.to_dict().values()):
                item = QStandardItem(elem)
                model.setItem(i, j, item)
        return model
