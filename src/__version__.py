import os
import platform
import sys

#软件版本
version = "1.0"

#操作系统
if sys.platform == "win32":
    os_platform = "Windows"
elif sys.platform == "linux":
    os_platform = "Linux"
else:
    raise NotImplementedError(f"当前系统 {sys.platform} 暂未被本程序支持")


#开发者模式
debug = os.getenv("debug", "false") == "true"