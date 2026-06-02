from control.time_manager.system_time import SystemTimeManager

class ControllerMediater:
    '''后端中介者类'''
    def __init__(self):
        self.time_manager = {"system_time": SystemTimeManager()}    #时间管理器
