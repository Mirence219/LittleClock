import os

from littleclock import LittleClock
from __version__ import version, debug, os_platform
from logger import Logger

if __name__ == "__main__":
    if os_platform == "Linux":
        os.environ["QT_QPA_PLATFORM"] = "xcb"

    Logger.set_level("INFO" if debug else "WARNING")   #配置日志等级
    
    print(f"LittleClock版本：{version}，\
            模式：{"Debug"if debug else "Realse"}，\
            平台：{os_platform}，\
            日志等级：{Logger.level}",)
    
    application = LittleClock()
    application.run()