import ast
from typing import Any, Callable
from PySide6.QtCore import Slot, Signal, QObject

from logger import Logger
from control.signal_bus import ControllerSignalBus

class ControllerSignalSender(QObject):
    '''后端信号发送器'''
    
    _signal = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.signal_bus = ControllerSignalBus()
        self.signal_bus.join_receiver(self.receive, "to_view")

    def connect(self, func):
        '''与前端信号绑定（外部实现）'''
        self._signal.connect(func)

    def send(self, signal:str, data:Any):
        '''向前端发送信号'''
        self._signal.emit(signal, str(data))    #重要！跨线程前要转化成字符串！

    def receive(self, signal:str, data:Any):
        '''向前端发送来自后端组件发送的信号（通过后端信号总线连接）'''
        if signal == "time_update":
            Logger.debug("后端信号发送器接收到通过信号总线发送的信号：{}，内容{}", signal, data)
        else:
            Logger.info("后端信号发送器接收到通过信号总线发送的信号：{}，内容{}", signal, data)
        self.send(signal, data)


class ControllerSignalReceiver:
    '''后端信号接收器'''
    def __init__(self, func:Callable):
        self.forward = func

    @Slot(str, str)
    def receive(self, signal:str, data:str):
        '''接收信号'''
        Logger.info("后端信号接收器接收到 信号:{},内容:{}", signal, data)
        self.forward(signal, ast.literal_eval(data))    #将接收到的内容还原
        





