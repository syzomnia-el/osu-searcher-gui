# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'oss.ui'
#
# Created by: Qt User Interface Compiler version 6.3.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableView, QToolButton, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(800, 600)
        Form.setMinimumSize(QSize(800, 600))
        self.formGridLayout = QGridLayout(Form)
        self.formGridLayout.setObjectName(u"formGridLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.beatmapVerticalLayout = QVBoxLayout()
        self.beatmapVerticalLayout.setObjectName(u"beatmapVerticalLayout")
        self.beatmapLabel = QLabel(Form)
        self.beatmapLabel.setObjectName(u"beatmapLabel")
        self.beatmapLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

        self.beatmapVerticalLayout.addWidget(self.beatmapLabel)

        self.beatmapCountLabel = QLabel(Form)
        self.beatmapCountLabel.setObjectName(u"beatmapCountLabel")
        self.beatmapCountLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.beatmapVerticalLayout.addWidget(self.beatmapCountLabel)

        self.gridLayout.addLayout(self.beatmapVerticalLayout, 2, 0, 1, 1)

        self.pathLabel = QLabel(Form)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.pathLabel, 0, 0, 1, 1)

        self.checkedBeatmapView = QTableView(Form)
        self.checkedBeatmapView.setObjectName(u"checkedBeatmapView")
        self.checkedBeatmapView.setSortingEnabled(True)
        self.checkedBeatmapView.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.checkedBeatmapView, 3, 1, 1, 1)

        self.checkButton = QPushButton(Form)
        self.checkButton.setObjectName(u"checkButton")

        self.gridLayout.addWidget(self.checkButton, 3, 2, 1, 1)

        self.findLabel = QLabel(Form)
        self.findLabel.setObjectName(u"findLabel")
        self.findLabel.setMaximumSize(QSize(16777215, 16777215))
        self.findLabel.setLayoutDirection(Qt.LeftToRight)
        self.findLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.findLabel, 1, 0, 1, 1)

        self.findEdit = QLineEdit(Form)
        self.findEdit.setObjectName(u"findEdit")
        self.findEdit.setMinimumSize(QSize(464, 20))

        self.gridLayout.addWidget(self.findEdit, 1, 1, 1, 1)

        self.showButton = QPushButton(Form)
        self.showButton.setObjectName(u"showButton")

        self.gridLayout.addWidget(self.showButton, 2, 2, 1, 1)

        self.pathHorizontalLayout = QHBoxLayout()
        self.pathHorizontalLayout.setSpacing(5)
        self.pathHorizontalLayout.setObjectName(u"pathHorizontalLayout")
        self.pathEdit = QLineEdit(Form)
        self.pathEdit.setObjectName(u"pathEdit")

        self.pathHorizontalLayout.addWidget(self.pathEdit)

        self.pathButton = QToolButton(Form)
        self.pathButton.setObjectName(u"pathButton")
        self.pathButton.setPopupMode(QToolButton.InstantPopup)

        self.pathHorizontalLayout.addWidget(self.pathButton)

        self.gridLayout.addLayout(self.pathHorizontalLayout, 0, 1, 1, 1)

        self.beatmapView = QTableView(Form)
        self.beatmapView.setObjectName(u"beatmapView")
        self.beatmapView.setSortingEnabled(True)
        self.beatmapView.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.beatmapView, 2, 1, 1, 1)

        self.checkedBeatmapVerticalLayout = QVBoxLayout()
        self.checkedBeatmapVerticalLayout.setObjectName(u"checkedBeatmapVerticalLayout")
        self.checkedBeatmapLabel = QLabel(Form)
        self.checkedBeatmapLabel.setObjectName(u"checkedBeatmapLabel")
        self.checkedBeatmapLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

        self.checkedBeatmapVerticalLayout.addWidget(self.checkedBeatmapLabel)

        self.checkedBeatmapCountLabel = QLabel(Form)
        self.checkedBeatmapCountLabel.setObjectName(u"checkedBeatmapCountLabel")
        self.checkedBeatmapCountLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.checkedBeatmapVerticalLayout.addWidget(self.checkedBeatmapCountLabel)

        self.gridLayout.addLayout(self.checkedBeatmapVerticalLayout, 3, 0, 1, 1)

        self.findButton = QPushButton(Form)
        self.findButton.setObjectName(u"findButton")

        self.gridLayout.addWidget(self.findButton, 1, 2, 1, 1)

        self.flushButton = QPushButton(Form)
        self.flushButton.setObjectName(u"flushButton")
        self.flushButton.setEnabled(True)
        self.flushButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.flushButton, 0, 2, 1, 1)

        self.formGridLayout.addLayout(self.gridLayout, 0, 0, 1, 1)

        QWidget.setTabOrder(self.pathEdit, self.pathButton)
        QWidget.setTabOrder(self.pathButton, self.flushButton)
        QWidget.setTabOrder(self.flushButton, self.findEdit)
        QWidget.setTabOrder(self.findEdit, self.findButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"osu!searcher", None))
        self.beatmapLabel.setText(QCoreApplication.translate("Form", u"Beatmap:", None))
        self.beatmapCountLabel.setText(QCoreApplication.translate("Form", u"(0)", None))
        self.pathLabel.setText(QCoreApplication.translate("Form", u"Path:", None))
        self.checkButton.setText(QCoreApplication.translate("Form", u"Check", None))
        self.findLabel.setText(QCoreApplication.translate("Form", u"keyword:", None))
        self.findEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Input keywords to find.", None))
        self.showButton.setText(QCoreApplication.translate("Form", u"Show", None))
        self.pathEdit.setText("")
        self.pathEdit.setPlaceholderText(
            QCoreApplication.translate("Form", u"Input the path of beatmaps saved, like '<path>/osu!/Songs)' .", None))
        self.pathButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.checkedBeatmapLabel.setText(QCoreApplication.translate("Form", u"Duplicate:", None))
        self.checkedBeatmapCountLabel.setText(QCoreApplication.translate("Form", u"(0)", None))
        self.findButton.setText(QCoreApplication.translate("Form", u"Find", None))
        self.flushButton.setText(QCoreApplication.translate("Form", u"Flush", None))
    # retranslateUi
