from PySide6.QtCore import QSharedMemory

from src.logger import Logger

SHM_NAME = "LittleClock"
APP_SIGN = b"LittleClock_write_by_Mirence"
_shm = None


def check_repeat_start() -> bool:
    '''防多开检测，同时呼出已存在进程'''
    global _shm

    temp_shm = QSharedMemory(SHM_NAME)
    if temp_shm.attach():   #挂载成功（已创建）
        sign = temp_shm.data()
        if APP_SIGN == bytes(sign[:len(APP_SIGN)]):
            Logger.critical("检测到已存在的LittleClock进程，本进程即将退出！")
        else:
            Logger.critical("检测到不兼容的第三方进程，本进程即将退出！")
        return False

    if_create = temp_shm.create(64)
    if not if_create:   #创建失败（并发创建）
        Logger.critical("检测到已存在的LittleClock进程，本进程即将退出！")
        return False
    
    _shm = temp_shm
    sign_ptr = _shm.data()
    for idx, val in enumerate(APP_SIGN):    #写入签名
        sign_ptr[idx] = val
    Logger.info("已创建共享内存区")

    return True


def show_app():
    '''呼出已存在进程'''



def shutdown():
    '''程序退出'''
    global _shm
    if _shm is not None:
        if _shm.isAttached():
            _shm.detach()
    Logger.info("共享内存已清除")

if __name__ == "__main__":
    is_repeat = check_repeat_start()
    if is_repeat:
        print("未多开")
        while(1):pass
    else:
        print("多开")

    shutdown()




