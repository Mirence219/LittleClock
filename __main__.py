from littleclock import LittleClock
from __version__ import version, debug
from logger import Logger

if __name__ == "__main__":
    print(f"LittleClock版本：{version}，模式：{"Debug"if debug else "Realse"}")
    Logger.set_level("DEBUG" if debug else "WARNING")
    Logger.set_level("INFO")
    application = LittleClock()
    application.run()