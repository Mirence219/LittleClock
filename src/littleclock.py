from PySide6.QtCore import QThread

from src.view.viewer import Viewer
from src.control.controller import Controller

class LittleClock:
    '''程序入口'''
    def __init__(self):
        self.viewer = Viewer()   #前端主控类
        self.controller = Controller()  #后端主控类
        self.controller_thread = QThread()

        self._init_signal_connect()

        self._init_controller_thread()
        

    def _init_signal_connect(self):
        '''绑定前后端信号管理器'''
        self.viewer.connect_signal(self.controller.signal_receiver.receive)
        self.controller.connect_signal(self.viewer.signal_receiver.receive)


    def _init_controller_thread(self):
        '''初始化后端线程'''
        self.controller_thread.finished.connect(self.controller.emit_finish_signal) #后端终止时向前端发送确认
        self.controller.moveToThread(self.controller_thread)    #将后端移入子线程
        self.controller_thread.start()


    def run(self) -> int:
        exit_code = self.viewer.run()
        return exit_code

    def get_viewer_signal(self):
        '''返回前端信号接收器（用于建立连接）'''
        return self.viewer.signal_receiver.receive_from_out

    def get_controller_signal(self):
        '''返回后端信号接收器（用于建立连接）'''
        return self.controller.signal_receiver.receive

if __name__ == "__main__":
    app = LittleClock()
    print("[TEST]信号发送测试")
    app.viewer.signal_sender.send("Giao!", "giaogiaogiao")
    app.controller.signal_sender.send("Lala!","hahahaaaa ")





