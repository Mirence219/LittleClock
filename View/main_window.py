from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from view.py_ui.ui_main_window import Ui_MainWindow

class MainWindowManager():
    '''主窗口对象管理器'''
    def __init__(self, signal_sender):
        self.signal_sender = signal_sender

        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.window.setWindowFlags(Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)

        self._connect_init()

    def _connect_init(self):
        self.ui.bntClose.clicked.connect(self.on_bntClose_clicked)
        self.ui.bnt1.clicked.connect(self.on_bnt1_clicked)
        self.ui.bnt2.clicked.connect(self.on_bnt2_clicked)
        self.ui.bnt3.clicked.connect(self.on_bnt3_clicked)
        self.ui.bnt4.clicked.connect(self.on_bnt4_clicked)
    
    def show(self):
        '''启动窗口'''
        self.window.show()

    def send(self, signal:str, data):
        '''发送信号'''
        self.signal_sender.send(signal, data)

    def on_bntClose_clicked(self):
        '''关闭窗口'''
        print("[DEBUG]点击关闭窗口")
        self.window.close()

    def on_bnt1_clicked(self):
        '''按钮1点击事件'''
        print("[DEBUG]按钮1被点击")
        self.send("按钮1", "被点击")

    def on_bnt2_clicked(self):
        '''按钮2点击事件'''
        print("[DEBUG]按钮2被点击")
        self.send("按钮2", "被点击")

    def on_bnt3_clicked(self):
        '''按钮3点击事件'''
        print("[DEBUG]按钮3被点击")
        self.send("按钮3", "被点击")

    def on_bnt4_clicked(self):
        '''按钮4点击事件'''
        print("[DEBUG]按钮4被点击")
        self.send("按钮4", "被点击")






