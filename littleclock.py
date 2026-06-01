from PySide6.QtCore import QThread

from view.viewer import Viewer
from control.controller import Controller

class LittleClock:
    '''程序入口'''
    def __init__(self):
        self.viewer = Viewer()   #前端主控类
        self.controller = Controller()  #后端主控类
        self.controller_thread = QThread()

        self._init_signal_connect()

        self.controller.moveToThread(self.controller_thread)    #将后端移入子线程
        self.controller_thread.start()
        

    def _init_signal_connect(self):
        '''绑定前后端信号管理器'''
        self.viewer.connect_signal(self.controller.signal_receiver.receive)
        self.controller.connect_signal(self.viewer.signal_receiver.receive)

    def run(self):
        self.viewer.run()

if __name__ == "__main__":
    app = LittleClock()
    print("[TEST]信号发送测试")
    app.viewer.signal_sender.send("Giao!", "giaogiaogiao")
    app.controller.signal_sender.send("Lala!","hahahaaaa ")





