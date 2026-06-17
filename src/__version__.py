import os
import platform
import sys
import psutil

#软件名称
APP_NAME = "LittleClock"

#软件版本
VERSION = "1.2"

#进程名称
_proc = psutil.Process(os.getpid())
PROC_NAME = _proc.name()

#操作系统
if sys.platform == "win32":
    OS_PLATFORM = "Windows"
elif sys.platform == "linux":
    OS_PLATFORM = "Linux"
else:
    OS_PLATFORM = sys.platform


#开发者模式
DEBUG = os.getenv("debug", "false") == "true"

#资源路径
if hasattr(sys, "_MEIPASS"):
    RESOURCE_DIR = sys._MEIPASS
else:
    RESOURCE_DIR = os.getcwd()

#程序数据目录
APP_DATA_DIR_NAME = "LittleClock"
LOCK_NAME = ".lock"
LOG_DIR_NAME = "log"

if OS_PLATFORM == "Windows":
    USER_APP_DATA_DIR = os.getenv("LOCALAPPDATA", os.path.expanduser("~/AppData/Local"))
elif OS_PLATFORM == "Linux":
    USER_APP_DATA_DIR = os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))

APP_DATA_DIR = os.path.join(USER_APP_DATA_DIR, APP_DATA_DIR_NAME) #程序数据目录
LOG_DIR = os.path.join(APP_DATA_DIR, LOG_DIR_NAME)                  #日志目录
LOCK_PATH = os.path.join(APP_DATA_DIR, LOCK_NAME)                   #锁文件目录                                              #锁文件目录