from typing import Any
from PySide6.QtWidgets import QApplication
import sys

from view.main_window import MainWindowManager
from view.signal import ViewerSignalReceiver, ViewerSignalSender

class Viewer():
    '''前端主控类'''
    def __init__(self):
        self._init_signal_manager()
        self._init_main_window_manager()

    def _init_main_window_manager(self):
        '''窗口管理器初始化'''
        self.app = QApplication(sys.argv)
        self.main_window_manager = MainWindowManager(self.signal_sender)

    def _init_signal_manager(self):
        '''信号管理器初始化(与后端通信)'''
        self.signal_sender = ViewerSignalSender()
        self.signal_receiver = ViewerSignalReceiver(self.receive)

    def run(self):
        self.main_window_manager.show()
        sys.exit(self.app.exec())

    def connect_signal(self, func):
        '''添加前端信号发送器的订阅者（接收者）'''
        self.signal_sender.connect(func)

    def receive(self, signal:str, data:Any):
        '''接受来自前端信号接收器的转发信号'''
        print(f"[INFO]前端主控接收到转发 信号:{signal}, 内容:{data}")
        if signal == "time_update":
            self.update_time(data)

    def update_time(self, render_data:list):
        '''设置时间面板'''
        self.main_window_manager.timeboard.set_time(render_data)
