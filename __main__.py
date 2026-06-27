from ast import Try
from genericpath import isfile
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
import psutil

from src.littleclock import LittleClock
from src.__version__ import *
from src.logger import Logger
from src import app_sign
from src.ipc import IPCServer, IPCSocket

def init():
    '''LittleClock初始化'''
    #Linux系统配置X11
    if OS_PLATFORM == "Linux":
        os.environ["QT_QPA_PLATFORM"] = "xcb"


    #日志初始化
    Logger.init()
    Logger.set_level("INFO" if DEBUG else "WARNING")   
    
    #配置程序目录
    try:
        if not os.path.isdir(APP_DATA_DIR):
            os.makedirs(APP_DATA_DIR, exist_ok=True)
            Logger.info("创建程序目录'{}'", APP_DATA_DIR)
        if not os.path.isdir(LOG_DIR):
            os.makedirs(LOG_DIR, exist_ok=True)
            Logger.info("创建日志目录'{}'", LOG_DIR)
    except PermissionError as e:
        Logger.exception("访问目录'{}'失败：权限不足", APP_DATA_DIR)
        sys.exit(1)
    except OSError as err:
        Logger.exception("访问目录'{}'失败：目录初始化系统异常：{}", APP_DATA_DIR, err)
        sys.exit(1)

    #配置日志输出
    Logger.init_output()

if __name__ == "__main__":
    init()

    print(f"LittleClock已启动\t进程名称：{PROC_NAME}\tPID：{os.getpid()}\n\
            版本：{VERSION}，\n\
            模式：{"Debug"if DEBUG else "Realese"}，\n\
            平台：{OS_PLATFORM}，\n\
            日志等级：{Logger.level}，\n\
            资源目录：{RESOURCE_DIR}，\n\
            程序目录：{APP_DATA_DIR}")

    if OS_PLATFORM not in ("Windows", "Linux"):
        Logger.critical("当前系统 {} 暂未被本程序支持", OS_PLATFORM)
        raise NotImplementedError(f"当前系统 {OS_PLATFORM} 暂未被本程序支持")

    exit_code = 2

    if app_sign.check_repeat_start():
        ipc_server = IPCServer()
        application = LittleClock()
        ipc_server.connect(application.get_viewer_signal())
        exit_code = application.run()

        ipc_server.shutdown()
    else:
        ipc_socket = IPCSocket()
        ipc_socket.send()
        ipc_socket.shutdown()

    app_sign.shutdown()
    Logger.info("程序退出码：{}", exit_code)
    Logger.shutdown()
    sys.exit(exit_code)
    