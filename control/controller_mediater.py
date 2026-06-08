import sys

from PySide6.QtCore import QCoreApplication

from control.time_manager.system_time import SystemTimeManager
from control.time_manager.abstract_time_manager import AbstractTimeManager
from control.signal_bus import ControllerSignalBus
from control.signal import ControllerSignalSender

class ControllerMediater:
    '''后端中介者类'''
    def __init__(self):
        self.time_manager_mode = None
        self.signal_bus = ControllerSignalBus()
        self.signal_channel = "render_time"    #通信频道
        self.signal_bus.join_sender(self.get_time_signal, self.signal_channel)
        self.time_signal = {"signal": "render_time", "data": None}

    def set_time_mode(self, mode:AbstractTimeManager):
        if self.time_manager_mode is not None:
            self.time_manager_mode.work = False
        self.time_manager_mode = mode
        self.time_manager_mode.work = True

    def get_time_signal(self) -> tuple:
        '''返回要发送的时间信号'''
        return self.time_signal["signal"], self.time_signal["data"] 

    def send_time(self, time_str):
        '''发送时间信号（回调函数）'''
        self.time_signal["data"] = time_str
        self.signal_bus.send_signal(self.get_time_signal, self.signal_channel)

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)

    media = ControllerMediater();
    media.set_time_mode(SystemTimeManager(media.send_time))
    signal_sender = ControllerSignalSender()

    
    app.aboutToQuit.connect(lambda: media.time_manager_mode._time_thread.quit())
    sys.exit(app.exec())
