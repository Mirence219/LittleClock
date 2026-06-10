from littleclock import LittleClock
from __version__ import version, debug
from logger import Logger

if __name__ == "__main__":
    Logger.set_level("DEBUG" if debug else "WARNING")   #配置日志等级
    Logger.set_level("INFO")
    
    print(f"LittleClock版本：{version}，模式：{"Debug"if debug else "Realse"}，日志等级：{Logger.level}",)
    application = LittleClock()
    application.run()