import os

from src.littleclock import LittleClock
from src.__version__ import version, debug, os_platform, resource_path
from src.logger import Logger

if __name__ == "__main__":
    if os_platform == "Linux":
        os.environ["QT_QPA_PLATFORM"] = "xcb"

    Logger.set_level("INFO" if debug else "WARNING")   #配置日志等级
    
    print(f"LittleClock\n\
            版本：{version}，\n\
            模式：{"Debug"if debug else "Realse"}，\n\
            平台：{os_platform}，\n\
            日志等级：{Logger.level}，\n\
            资源目录：{resource_path}")

    if os_platform not in ("Windows", "Linux"):
        Logger.critical("当前系统 {} 暂未被本程序支持", os_platform)
        raise NotImplementedError(f"当前系统 {os_platform} 暂未被本程序支持")
    
    application = LittleClock()
    application.run()