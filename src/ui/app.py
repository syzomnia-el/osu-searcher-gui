# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication

from ui.form import OSSForm


class OSSApplication:
    __app: QApplication
    __form: OSSForm

    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.__form = OSSForm()

    def run(self):
        self.__form.show()
        sys.exit(self.__app.exec_())
