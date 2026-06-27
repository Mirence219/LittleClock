from typing import Any
from PySide6.QtWidgets import QApplication
import sys

from src.logger import Logger
from src.view.main_window import MainWindowManager
from src.view.signal import ViewerSignalReceiver, ViewerSignalSender

class Viewer():
    '''前端主控类'''
    def __init__(self):
        self._init_signal_manager()
        self._init_main_window_manager()

    def _init_main_window_manager(self):
        '''窗口管理器初始化'''
        self.app = QApplication(sys.argv)
        self.main_window_manager = MainWindowManager(self.signal_sender, self.quit)

    def _init_signal_manager(self):
        '''信号管理器初始化(与后端通信)'''
        self.signal_sender = ViewerSignalSender()
        self.signal_receiver = ViewerSignalReceiver(self.receive)

    def run(self) -> int:
        self.main_window_manager.show()
        return self.app.exec()

    def connect_signal(self, func):
        '''添加前端信号发送器的订阅者（接收者）'''
        self.signal_sender.connect(func)

    def receive(self, signal:str, data:Any):
        '''接受来自前端信号接收器的转发信号'''
        if signal == "time_update":
            Logger.debug("前端主控接收到转发 信号:{}, 内容:{}", signal, data)
            self.update_time(data)
            return

        Logger.info("前端主控接收到转发 信号:{}, 内容:{}", signal, data)
        if signal == "finish-shutdown":
            self.main_window_manager.confirm_close()
        
        elif signal == "show-window":
            self.main_window_manager.show()


    def update_time(self, render_data:list):
        '''设置时间面板'''
        self.main_window_manager.timeboard.set_time(render_data)

    def quit(self):
        '''退出进程（回调函数）'''
        Logger.info("退出LittleClock程序")
        self.app.quit()