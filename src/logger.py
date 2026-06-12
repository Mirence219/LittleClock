import logging
from datetime import datetime

LEVEL_DIC = {
    "DEBUG": 0,
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "CRITICAL": 4,
    "EXCEPTION": 5
}

class classproperty(property):
    def __get__(self, instance, owner):
        return self.fget(owner)

class Logger:
    '''日志记录器（全局工具类）'''
    _level = 0  # 默认 DEBUG 级别

    @classmethod
    def set_level(cls, level_str: str):
        '''设置日志输出等级'''
        if level_str in LEVEL_DIC:
            cls._level = LEVEL_DIC[level_str]

    @classproperty
    def level(cls):
        return cls._level

    @classmethod
    def _format_msg(cls, msg: str, *args, **kwargs) -> str:
        """内部：拼接消息 + 时间戳"""
        # 格式化日志内容
        try:
            content = msg.format(*args, **kwargs)
        except (IndexError, KeyError):
            content = f"{msg} args={args} kwargs={kwargs}"
        # 拼接时间
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{time_str}]{content}"

    @classmethod
    def debug(cls, msg: str, *args, **kwargs):
        '''DEBUG级日志输出'''
        if LEVEL_DIC["DEBUG"] < cls._level:
            return
        log_str = cls._format_msg(f"[DEBUG]{msg}", *args, **kwargs)
        print(log_str)

    @classmethod
    def info(cls, msg: str, *args, **kwargs):
        '''INFO级日志输出'''
        if LEVEL_DIC["INFO"] < cls._level:
            return
        log_str = cls._format_msg(f"[INFO]{msg}", *args, **kwargs)
        print(log_str)

    @classmethod
    def warning(cls, msg: str, *args, **kwargs):
        '''WARNING级日志输出'''
        if LEVEL_DIC["WARNING"] < cls._level:
            return
        log_str = cls._format_msg(f"[WARNING]{msg}", *args, **kwargs)
        print(log_str)

    @classmethod
    def error(cls, msg: str, *args, **kwargs):
        '''ERROR级日志输出'''
        if LEVEL_DIC["ERROR"] < cls._level:
            return
        log_str = cls._format_msg(f"[ERROR]{msg}", *args, **kwargs)
        print(log_str)

    @classmethod
    def critical(cls, msg: str, *args, **kwargs):
        '''CRITICAL级日志输出'''
        if LEVEL_DIC["CRITICAL"] < cls._level:
            return
        log_str = cls._format_msg(f"[CRITICAL]{msg}", *args, **kwargs)
        print(log_str)

    @classmethod
    def exception(cls, msg: str, *args, **kwargs):
        '''EXCEPTION级日志输出（异常专用）'''
        if LEVEL_DIC["EXCEPTION"] < cls._level:
            return
        log_str = cls._format_msg(f"[EXCEPTION]{msg}", *args, **kwargs)
        print(log_str)

