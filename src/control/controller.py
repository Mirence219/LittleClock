from PySide6.QtCore import QThread, QObject, Signal

from src.logger import Logger
from src.control.signal import ControllerSignalReceiver, ControllerSignalSender
from src.control.controller_mediater import ControllerMediater
from src.control.render_meta_data import RenderMetaData
from src.control.time_manager.system_time import SystemTimeManager

class Controller(QObject):
    '''后端主控类'''
    def __init__(self):
        super().__init__()
        
        self._init_controller_mediater()
        self._init_signal_manager()
        self._init_render_meta_data()
        self._init_time_manager()

    def _init_controller_mediater(self):
        '''后端中介者初始化'''
        self.media = ControllerMediater()

    def _init_signal_manager(self):
        '''后端信号管理器初始化'''
        self.signal_sender = ControllerSignalSender()
        self.signal_receiver = ControllerSignalReceiver(self.receive)

    def _init_render_meta_data(self):
        '''渲染元数据初始化'''
        self.render_meta_data = RenderMetaData()

    def _init_time_manager(self):
        '''时间管理器初始化'''
        self.time_manager_list = {"system_time": SystemTimeManager(self.media.send_time )}
        self.media.set_time_mode(self.time_manager_list["system_time"]) #设置默认模式


    def set_time_mode(self, time_mode:str):
        '''设置时间模式'''
        self.media.set_time_mode(self.time_manager_list[time_mode])

    def connect_signal(self, func):
        '''添加后端信号发送器的订阅者（接收者）'''
        self.signal_sender.connect(func)

    def receive(self, signal:str, data):
        '''接收来自后端信号接收器转发的信号'''
        Logger.info("后端主控接收到转发 信号:{}, 内容:{}", signal, data)
        if signal == "shutdown":
            self._quit()

    def send_signal(self, signal:str, data):
        '''借助后端信号发送器发送信号'''
        self.signal_sender.send(signal, data)

    def _quit(self):
        '''终止后端线程'''
        self.media.quit()       #显式暂停计时器，方便保存信息
        self.thread().quit()
        Logger.info("正在终止后端线程……")

    def emit_finish_signal(self):
        '''终止线程发送完成信号'''
        self.send_signal("finish-shutdown", None)






