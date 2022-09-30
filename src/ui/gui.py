# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'oss.ui'
#
# Created by: Qt User Interface Compiler version 6.3.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel,
                               QLayout, QLineEdit, QListView, QPushButton,
                               QToolButton, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(640, 480)
        Form.setMinimumSize(QSize(640, 480))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 621, 461))
        self.formGridLayout = QGridLayout(self.gridLayoutWidget)
        self.formGridLayout.setSpacing(10)
        self.formGridLayout.setObjectName(u"formGridLayout")
        self.formGridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formGridLayout.setContentsMargins(0, 0, 0, 0)
        self.findButton = QPushButton(self.gridLayoutWidget)
        self.findButton.setObjectName(u"findButton")

        self.formGridLayout.addWidget(self.findButton, 1, 2, 1, 1)

        self.beatmapView = QListView(self.gridLayoutWidget)
        self.beatmapView.setObjectName(u"beatmapView")

        self.formGridLayout.addWidget(self.beatmapView, 2, 1, 1, 1)

        self.checkedBeatmapVerticalLayout = QVBoxLayout()
        self.checkedBeatmapVerticalLayout.setObjectName(u"checkedBeatmapVerticalLayout")
        self.checkedBeatmapLabel = QLabel(self.gridLayoutWidget)
        self.checkedBeatmapLabel.setObjectName(u"checkedBeatmapLabel")
        self.checkedBeatmapLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

        self.checkedBeatmapVerticalLayout.addWidget(self.checkedBeatmapLabel)

        self.checkedBeatmapCountLabel = QLabel(self.gridLayoutWidget)
        self.checkedBeatmapCountLabel.setObjectName(u"checkedBeatmapCountLabel")
        self.checkedBeatmapCountLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.checkedBeatmapVerticalLayout.addWidget(self.checkedBeatmapCountLabel)

        self.formGridLayout.addLayout(self.checkedBeatmapVerticalLayout, 3, 0, 1, 1)

        self.findEdit = QLineEdit(self.gridLayoutWidget)
        self.findEdit.setObjectName(u"findEdit")
        self.findEdit.setMinimumSize(QSize(464, 20))

        self.formGridLayout.addWidget(self.findEdit, 1, 1, 1, 1)

        self.checkedBeatmapView = QListView(self.gridLayoutWidget)
        self.checkedBeatmapView.setObjectName(u"checkedBeatmapView")
        self.checkedBeatmapView.setMinimumSize(QSize(0, 0))

        self.formGridLayout.addWidget(self.checkedBeatmapView, 3, 1, 1, 1)

        self.checkButton = QPushButton(self.gridLayoutWidget)
        self.checkButton.setObjectName(u"checkButton")

        self.formGridLayout.addWidget(self.checkButton, 3, 2, 1, 1)

        self.beatmapVerticalLayout = QVBoxLayout()
        self.beatmapVerticalLayout.setObjectName(u"beatmapVerticalLayout")
        self.beatmapLabel = QLabel(self.gridLayoutWidget)
        self.beatmapLabel.setObjectName(u"beatmapLabel")
        self.beatmapLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

        self.beatmapVerticalLayout.addWidget(self.beatmapLabel)

        self.beatmapCountLabel = QLabel(self.gridLayoutWidget)
        self.beatmapCountLabel.setObjectName(u"beatmapCountLabel")
        self.beatmapCountLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.beatmapVerticalLayout.addWidget(self.beatmapCountLabel)

        self.formGridLayout.addLayout(self.beatmapVerticalLayout, 2, 0, 1, 1)

        self.findLabel = QLabel(self.gridLayoutWidget)
        self.findLabel.setObjectName(u"findLabel")
        self.findLabel.setMaximumSize(QSize(16777215, 16777215))
        self.findLabel.setLayoutDirection(Qt.LeftToRight)
        self.findLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.formGridLayout.addWidget(self.findLabel, 1, 0, 1, 1)

        self.flushButton = QPushButton(self.gridLayoutWidget)
        self.flushButton.setObjectName(u"flushButton")
        self.flushButton.setEnabled(True)
        self.flushButton.setAutoDefault(False)

        self.formGridLayout.addWidget(self.flushButton, 0, 2, 1, 1)

        self.pathHorizontalLayout = QHBoxLayout()
        self.pathHorizontalLayout.setSpacing(5)
        self.pathHorizontalLayout.setObjectName(u"pathHorizontalLayout")
        self.pathEdit = QLineEdit(self.gridLayoutWidget)
        self.pathEdit.setObjectName(u"pathEdit")

        self.pathHorizontalLayout.addWidget(self.pathEdit)

        self.pathButton = QToolButton(self.gridLayoutWidget)
        self.pathButton.setObjectName(u"pathButton")
        self.pathButton.setPopupMode(QToolButton.InstantPopup)

        self.pathHorizontalLayout.addWidget(self.pathButton)

        self.formGridLayout.addLayout(self.pathHorizontalLayout, 0, 1, 1, 1)

        self.pathLabel = QLabel(self.gridLayoutWidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.formGridLayout.addWidget(self.pathLabel, 0, 0, 1, 1)

        self.showButton = QPushButton(self.gridLayoutWidget)
        self.showButton.setObjectName(u"showButton")

        self.formGridLayout.addWidget(self.showButton, 2, 2, 1, 1)

        self.checkButton.raise_()
        self.checkedBeatmapView.raise_()
        self.pathLabel.raise_()
        self.findLabel.raise_()
        self.findEdit.raise_()
        self.findButton.raise_()
        self.beatmapView.raise_()
        self.showButton.raise_()
        self.flushButton.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"osu!searcher", None))
        self.findButton.setText(QCoreApplication.translate("Form", u"Find", None))
        self.checkedBeatmapLabel.setText(QCoreApplication.translate("Form", u"Duplicate:", None))
        self.checkedBeatmapCountLabel.setText(QCoreApplication.translate("Form", u"(0)", None))
        self.findEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Input keywords to find.", None))
        self.checkButton.setText(QCoreApplication.translate("Form", u"Check", None))
        self.beatmapLabel.setText(QCoreApplication.translate("Form", u"Beatmap:", None))
        self.beatmapCountLabel.setText(QCoreApplication.translate("Form", u"(0)", None))
        self.findLabel.setText(QCoreApplication.translate("Form", u"keyword:", None))
        self.flushButton.setText(QCoreApplication.translate("Form", u"Flush", None))
        self.pathEdit.setText("")
        self.pathEdit.setPlaceholderText(
            QCoreApplication.translate("Form", u"Input the path of beatmaps saved, like '<path>/osu!/Songs)' .", None))
        self.pathButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.pathLabel.setText(QCoreApplication.translate("Form", u"Path:", None))
        self.showButton.setText(QCoreApplication.translate("Form", u"Show", None))
    # retranslateUi
