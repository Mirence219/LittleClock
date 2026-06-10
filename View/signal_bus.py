from typing import Callable

from logger import Logger

class ViewerSignalBus():
    '''前端信号总线（全局唯一单例）'''
    _instance = None
    _inited = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if self._inited:
            return
        self.signal_channel = {}    #信号频段，格式{{"频段名1": { "sender":[发送者1, 发送者2],"receiver": [接收者1, 接收者2] },...}
        self._inited = True

    def join_sender(self, send_func:Callable, channel_name:str):
        '''作为发送者加入频段（若频段不存在则会创建）'''
        if not self._if_channel_live(channel_name):
            self._create_channel(channel_name)

        if self._if_send_func_live(send_func, channel_name):
            raise ValueError(f"'{send_func.__name__}'试图作为发送者重复加入前端频段'{channel_name}'")

        Logger.info("前端创建频段'{}", channel_name)
        self.signal_channel[channel_name]["sender"].append(send_func)
        Logger.info("前端频段'{}'添加成员'{}'", channel_name, send_func.__name__)


    def leave_sender(self, send_func:Callable, channel_name:str):
        '''作为发送者退出频段'''
        self._if_channel_live(channel_name, False)

        if not self._if_send_func_live(send_func, channel_name):
            raise ValueError(f"'{send_func.__name__}'试图作为发送者退出尚未加入的前端频段'{channel_name}'")

        self.signal_channel[channel_name]["sender"].remove(send_func)
        Logger.info("前端频段'{}'删除成员'{}'", channel_name, send_func.__name__)


    def join_receiver(self, receive_func:Callable, channel_name:str):
        '''作为接收者加入频段（若频段不存在则会创建）'''
        if not self._if_channel_live(channel_name):
            self._create_channel(channel_name)
        if self._if_receive_func_live(receive_func, channel_name):
            raise ValueError(f"'{receive_func.__name__}'试图作为接收者重复加入前端频段'{channel_name}'")

        Logger.info("创建前端频段'{}", channel_name)
        self.signal_channel[channel_name]["receiver"].append(receive_func)
        Logger.info("前端频段'{}'添加成员'{}'", channel_name, receive_func.__name__)


    def leave_receiver(self, receive_func:Callable, channel_name:str):
        '''作为接收者退出频段'''
        self._if_channel_live(channel_name, False)

        if not self._if_receive_func_live(receive_func, channel_name):
            raise ValueError(f"'{receive_func.__name__}'试图作为接收者退出尚未加入的前端频段'{channel_name}'")

        self.signal_channel[channel_name]["receiver"].remove(receive_func)
        Logger.info("前端频段'{}'删除成员'{}'", channel_name, receive_func.__name__)


    def send_signal(self, send_func:Callable, channel_name:str):
        '''发送者通过频段向接收者发送信号'''
        self._if_channel_live(channel_name, False)

        if not self._if_send_func_live(send_func, channel_name):
            raise ValueError(f"'{send_func.__name__}'未作为发送者加入前端频段'{channel_name}'")

        signal, data = send_func()
        for receive_func in self.signal_channel[channel_name]["receiver"]:
            receive_func(signal, data)

    def _create_channel(self, channel_name):
        '''创建新频段'''
        self.signal_channel.update({channel_name: {"sender": [],"receiver": []}})


    def _if_channel_live(self, channel_name:str, mode=True) -> bool:    #True（默认）- 布尔模式，False- 报错模式
        '''判断频段是否存在'''
        if channel_name in self.signal_channel:
            return True
        if not mode:
            raise KeyError(f"不存在的前端频段'{channel_name}'")
        return False
            

    def _if_send_func_live(self, send_func:Callable, channel_name:str) -> bool:
        '''判断发送者是否在指定频段内'''
        return send_func in self.signal_channel[channel_name]["sender"]
        

    def _if_receive_func_live(self, receive_func:Callable, channel_name:str) -> bool:
        '''判断接收者是否在指定频段内'''
        return receive_func in self.signal_channel[channel_name]["receiver"]



if __name__ == "__main__":
    bus = ViewerSignalBus()
    bus2 = ViewerSignalBus()
    def send1() -> tuple:
        signal = "haha"
        data = "aaaaa!"
        return signal, data

    def receive1(signal, data):
        print(f"信号{signal}, 内容{data}")

    bus.join_sender(send1, "频道1")
    bus2.join_receiver(receive1, "频道1")
    bus2.send_signal(send1, "频道1")
        





