from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from view.py_ui.ui_main_window import Ui_MainWindow

class MainWindowManager():
    '''主窗口对象管理器'''
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.window.setWindowFlags(Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)
    
    def show(self):
        '''启动窗口'''
        self.window.show()




