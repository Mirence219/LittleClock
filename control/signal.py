from PySide6.QtCore import Slot, Signal, QObject

class ControllerSignalSender(QObject):
    '''后端信号发送器'''
    
    _signal = Signal(str, str)

    def __init__(self):
        super().__init__()

    def connect(self, func:callable):
        '''信号绑定（外部实现）'''
        self._signal.connect(func)

    def send(self, signal:str, data:str):
        '''发送信号'''
        self._signal.emit(signal, data)


class ControllerSignalReceiver:
    '''后端信号接收器'''
    def __init__(self, func:callable):
        self.forward = func

    @Slot(str, str)
    def receive(self, signal:str, data:str):
        '''接收信号'''
        print(f"[DEBUG]后端信号接收器接收到 信号:{signal},内容:{data}")
        self.forward(signal, data)
        





