from PySide6.QtCore import QThread, QObject, QTime, QCoreApplication
import time
import sys

from control.time_manager.abstract_time_manager import AbstractTimeManager, AbstractTime

#时间字符串格式
TIME_FORMAT = "hh:mm:ss"

class SystemTime(AbstractTime):
    '''系统时间对象'''

    def _init_time(self):
        self._time = QTime.currentTime()

    def _refresh(self):
        self._time = QTime.currentTime()
        self.time_update.emit(self._get_time_str())

    def _get_time_str(self) -> str:
        '''返回时间字符串'''
        time_str = self._time.toString(TIME_FORMAT)
        return time_str


class SystemTimeManager(AbstractTimeManager):
    '''系统时间管理器'''

    def _init_time(self):
        '''初始化时间对象'''
        self._time = SystemTime()
        self._time_thread = QThread()
        self._time.moveToThread(self._time_thread)
        self._time_thread.started.connect(self._time.start) #线程开/关控制刷新计时器
        self._time_thread.finished.connect(self._time.stop)
        self._time_thread.finished.connect(self._time.deleteLater)
        self._time.time_update.connect(self._on_received)  #信号连接
        self._time_thread.start()




if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    time_manager = SystemTimeManager()    

    def console_print(t_str: str):
        print(f"\r{t_str}", end="")

    time_manager._time.time_update.connect(console_print)
    app.aboutToQuit.connect(lambda: time_manager._time_thread.quit())
    sys.exit(app.exec())