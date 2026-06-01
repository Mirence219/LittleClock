from PySide6.QtCore import QThread, QObject, Signal

from control.signal import ControllerSignalReceiver, ControllerSignalSender

class Controller(QObject):
    '''后端主控类'''
    def __init__(self):
        super().__init__()
        self._init_signal_manager()
        self._init_controller_mediater()

    def _init_signal_manager(self):
        '''后端信号管理器初始化'''
        self.signal_sender = ControllerSignalSender()
        self.signal_receiver = ControllerSignalReceiver(self.receive)

    def _init_controller_mediater(self):
        '''后端中介者初始化'''
        pass

    def connect_signal(self, func:callable):
        '''添加后端信号发送器的订阅者（接收者）'''
        self.signal_sender.connect(func)

    def receive(self, signal:str, data:str):
        '''接收来自后端信号接收器转发的信号'''
        print(f"[DEBUG]后端主控接收到转发 信号:{signal}, 内容:{data}")





