from PySide6.QtWidgets import QApplication
import sys

from view.main_window import MainWindowManager

class Viewer():
    '''前端主控类'''
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window_manager = MainWindowManager()
        self.main_window_manager.show()
        sys.exit(self.app.exec())