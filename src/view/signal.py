import ast
from typing import Any
from PySide6.QtCore import Slot, Signal, QObject

from src.logger import Logger
from src.view.signal_bus import ViewerSignalBus

class ViewerSignalSender(QObject):
    '''前端信号发送器'''
    
    _signal = Signal(str, str)

    def __init__(self):
        super().__init__()

    def connect(self, func):
        '''信号绑定（外部实现）'''
        self._signal.connect(func)
        self._signal_bus = ViewerSignalBus()
        self._channel = "to-control"
        self._signal_bus.join_receiver(self.receive, self._channel)

    def send(self, signal:str, data):
        '''发送信号'''
        self._signal.emit(signal, str(data))     #重要！发送前要转换为字符串！

    def receive(self, signal:str, data:Any):
        '''向后端发送来自前端组件发送的信号（通过前端信号总线连接）'''
        Logger.info("前端信号发送器接收到通过信号总线发送的信号：{}，内容{}", signal, data)
        self.send(signal, data)


class ViewerSignalReceiver:
    '''前端信号接收器'''
    def __init__(self, func):
        self.forword = func

    @Slot(str, str)
    def receive(self, signal:str, data:str):
        '''接收信号'''
        if signal == "time_update":
            Logger.debug("前端信号接收器接收到 信号:{},内容:{}", signal, data)
        else:
            Logger.info("前端信号接收器接收到 信号:{},内容:{}", signal, data)
        self.forword(signal, ast.literal_eval(data))  #将接收到的内容还原给前端主控









