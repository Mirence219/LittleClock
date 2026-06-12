from typing import Callable

from PySide6.QtCore import QTime, QObject, QThread, QTimer, Slot, Signal

from logger import Logger

#时间对象刷新间隔(ms)
REFRESH_TIME = 100

class AbstractTime(QObject):
    '''时间对象接口
    接口具体用法：仅需重写_init_time()、_reflesh()和_get_time_str()'''

    time_update_signal = Signal(str)   #时间刷新信号

    def __init__(self):
        super().__init__()
        self._init_time()
        self._timer = None

    def _init_time(self):
        '''初始化QTime对象
        self._time: QTime()
        '''
        raise NotImplementedError(f"AbstractTime子类{self.__class__.__name__}未实现 _init_time()")

    def _init_timer(self):
        '''初始化QTimer对象'''
        self._timer = QTimer()    #定时器
        self._timer.setInterval(REFRESH_TIME)

    def _init_connect(self):
        '''初始化事件绑定'''
        self._timer.timeout.connect(self._refresh)

    def _refresh(self):
        '''刷新时间
        self.time_update.emit(self._last_time)
        '''
        raise NotImplementedError(f"AbstractTime子类{self.__class__.__name__}未实现 _refresh()")

    def _get_time_str(self) -> str:
        '''返回时间字符串
        time_str = self._time.toString()
        return time_str'''
        raise NotImplementedError(f"AbstractTime子类{self.__class__.__name__}未实现 _init_get_time_str()")

    def start(self):
        '''启用刷新计时器'''
        if self._timer is None:  #延迟创建timer
            self._init_timer()
            self._init_connect()
        if not self._timer.isActive(): # 只有没运行时才启动
            self._timer.start()
        else:
            Logger.warning("AbstractTime子类{self.__class__.__name__}重复创建_timer计时对象！")

    def stop(self):
        '''停用刷新计时器'''
        self._timer.stop()


class AbstractTimeManager:
    '''时间管理器接口'''

    def __init__(self, callback:Callable):
        self._last_time = "on content"    #最新获取的时间字符串
        self._init_time()
        self.work = False   #是否工作
        self.send_time = callback   #调用中介者的回调函数向前端发送信号

    def _init_time(self):
        '''初始化时间对象
        self._time = AbstractTime()
        self._time_thread = QThread()
        self._time.moveToThread(self._time_thread)
        self._time_thread.started.connect(self._time.start) #线程开/关控制刷新计时器
        self._time_thread.finished.connect(self._time.stop)
        self._time_thread.finished.connect(self._time.deleteLater)
        self._time.time_update.connect(self._on_received)  #信号连接
        self._time_thread.start()
        '''
        raise NotImplementedError(f"AbstractTimeManager子类{self.__class__.__name__}未实现 _init_time()")

    @Slot(str)
    def _on_received(self, time_str: str):
        '''接受来自时间对象的字符串输出刷新，并向前端推送'''
        self._last_time = time_str
        if self.work:
            self.send_time(self._get_time())


    def _get_time(self) -> str:
        '''返回时间的字符串输出'''
        return self._last_time




