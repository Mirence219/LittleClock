import os
import platform
import sys

#软件版本
version = "1.1.1"

#操作系统
if sys.platform == "win32":
    os_platform = "Windows"
elif sys.platform == "linux":
    os_platform = "Linux"
else:
    os_platform = sys.platform


#开发者模式
debug = os.getenv("debug", "false") == "true"

#资源路径
if hasattr(sys, "_MEIPASS"):
    resource_path = sys._MEIPASS
else:
    resource_path = os.getcwd()