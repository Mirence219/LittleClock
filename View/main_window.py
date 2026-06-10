from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from logger import Logger
from view.py_ui.ui_main_window import Ui_MainWindow
from view.timeboard import TimeboardManager

class MainWindowManager():
    '''主窗口对象管理器'''
    def __init__(self, signal_sender):
        self.signal_sender = signal_sender
        self._init_main_window()
        self._init_timeboard()
        self._connect_init()


    def _init_main_window(self):
        '''初始化主窗口'''
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.window.setWindowFlags(Qt.FramelessWindowHint)      #去掉窗口上方标题栏
        self.window.setAttribute(Qt.WA_TranslucentBackground)   #设置透明窗口


    def _init_timeboard(self):
        '''初始化时间面板管理器'''
        self.timeboard = TimeboardManager(self.ui.wgtTimeboard)


    def _connect_init(self):
        '''绑定按键事件'''
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
        Logger.info("点击关闭窗口")
        self.window.close()

    def on_MainWindow_clicked(self):
        '''点击主窗口（拖拽）'''
        Logger.info("点击主窗口")


    def on_bnt1_clicked(self):
        '''按钮1点击事件'''
        Logger.info("点击按钮1")
        self.send("按钮1", None)

    def on_bnt2_clicked(self):
        '''按钮2点击事件'''
        Logger.info("点击按钮2")
        self.send("按钮2", None)

    def on_bnt3_clicked(self):
        '''按钮3点击事件'''
        Logger.info("点击按钮3")
        self.send("按钮3", None)

    def on_bnt4_clicked(self):
        '''按钮4点击事件'''
        Logger.info("点击按钮4")
        self.send("按钮4", None)








