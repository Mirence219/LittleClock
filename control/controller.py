from PySide6.QtCore import QThread, QObject, Signal

from control.signal import ControllerSignalReceiver, ControllerSignalSender
from control.controller_mediater import ControllerMediater
from control.render_meta_data import RenderMetaData

class Controller(QObject):
    '''后端主控类'''
    def __init__(self):
        super().__init__()
        self._init_signal_manager()
        self._init_controller_mediater()
        self._init_render_meta_data()

    def _init_signal_manager(self):
        '''后端信号管理器初始化'''
        self.signal_sender = ControllerSignalSender()
        self.signal_receiver = ControllerSignalReceiver(self.receive)

    def _init_controller_mediater(self):
        '''后端中介者初始化'''
        self.media = ControllerMediater()

    def _init_render_meta_data(self):
        '''渲染元数据初始化'''
        self.render_meta_data = RenderMetaData(self.send_signal)

    def connect_signal(self, func):
        '''添加后端信号发送器的订阅者（接收者）'''
        self.signal_sender.connect(func)

    def receive(self, signal:str, data):
        '''接收来自后端信号接收器转发的信号'''
        print(f"[DEBUG]后端主控接收到转发 信号:{signal}, 内容:{data}")

    def send_signal(self, signal:str, data):
        '''借助后端信号发送器发送信号'''
        self.signal_sender.send(signal, data)






