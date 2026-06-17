from ast import Try
from genericpath import isfile
import os
import psutil

from src.littleclock import LittleClock
from src.__version__ import *
from src.logger import Logger

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


def search_process(pid:int) -> str|None:
    '''获取指定进程名'''
    try:
        proc = psutil.Process(pid)
        proc_name = proc.name().lower()
    except psutil.NoSuchProcess:
        return None
    return proc_name


def creat_lock():
    '''创建锁文件'''
    try:
        with open(LOCK_PATH, "w") as lock_file:
            lock_file.write(str(os.getpid()))
    except PermissionError as e:    #权限不足
        Logger.exception("创建锁文件'{}'失败：权限不足", LOCK_PATH)
        sys.exit(1)
    except OSError as err:
        Logger.exception("创建锁文件'{}'失败：错误详情：{}", LOCK_PATH, err)
        sys.exit(1)


def remove_lock():
    '''删除锁文件'''
    try:
        os.remove(LOCK_PATH)
    except PermissionError as e:    #权限不足
        if e.winerror == 32:
            Logger.warning("删除锁文件'{}'失败：文件被其他进程被占用", LOCK_PATH)
        else:
            Logger.exception("删除锁文件'{}'失败：权限不足", LOCK_PATH)
        sys.exit(1)
    except OSError as err:
        Logger.exception("删除锁文件'{}'失败：错误详情：{}", LOCK_PATH, err)
        sys.exit(1)


def check_repeat_start():
    '''检查是否重复启动'''
    try:
        if os.path.isfile(LOCK_PATH):
            with open(LOCK_PATH, "r") as lock_file:
                pid = int(lock_file.read().strip())
                if search_process(pid) == PROC_NAME:
                    Logger.exception("进程'{}'多开", PROC_NAME)
                    sys.exit(2)

            os.remove(LOCK_PATH)    #删除锁文件残留
            Logger.warning("程序上一次可能异常退出，已清理锁文件残留")
        creat_lock()        #正常启动创建锁文件

    except PermissionError as e:    #权限不足
        if e.winerror == 32:
            Logger.warning("打开锁文件'{}'失败：文件被其他进程占用", LOCK_PATH)
        else:
            Logger.exception("打开锁文件'{}'失败：权限不足", LOCK_PATH)
        sys.exit(1)
    except OSError as err:
        Logger.exception("打开锁文件'{}'失败：错误详情：{}", LOCK_PATH, err)
        sys.exit(1)



if __name__ == "__main__":
    init()
    check_repeat_start()

    from PySide6.QtGui import QFontDatabase

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
    
    application = LittleClock()
    exit_code = application.run()

    remove_lock()
    Logger.info("程序退出码：{}", exit_code)
    Logger.quit()
    sys.exit(exit_code)