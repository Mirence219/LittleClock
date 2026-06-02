from control.renderer.digital_tube import DigitalTubeRenderer

class RenderMetaData:
    '''渲染元数据管理器'''
    def __init__(self, send_signal_func):
        self.send_signal = send_signal_func #借助后端主控向前端通信

        self._meta_data = []        #返回的元数据列表组成[mode:str, patch:bool,meta1:dict, meta2:dict, ...]
        self._last_meta_data = []
        self._renderer_tuple = (DigitalTubeRenderer(), )
        self.select_render_mode("digital_tube")

    def select_render_mode(self, mode:str):
        '''选择渲染器模式'''
        if mode == "digital_tube":
            self._renderer = self._renderer_tuple[0]
            self._patch = self._renderer.patch
            self._mode = self._renderer.mode
            self._first_render = True   #每次切换模式都需要改为True

    def render(self, time_str:str) -> list | None:
        '''交由渲染器逐个渲染字符,并返回元数据列表'''
        if self._first_render:
            self._first_render = False
        meta_list = [self._mode, self._patch and not self._first_render]
        for i in range(len(time_str)):
            meta_list.append(self._renderer.render(time_str[i]))
        self._last_meta_data = self._meta_data.copy()
        self._meta_data = meta_list.copy()

        if meta_list[1]:        
            return self.get_meta_patch()    #差分输出
        
        return meta_list                    #全量输出

    def get_meta_patch(self) -> list | None:    
        '''查询元数据差异，返回值 patch_meta = [mode:str, patch:bool, patch_meta:tuple(add_meta:set, off_meta:set), ...]'''
        patch_meta = [None] * len(self._meta_data)
        patch_meta[:1] = self._meta_data[:1]
        modify = False                  #True变化，False不变（不变时不发送信号）                  
        
        for i in range(2, len(self._meta_data)):
            new_meta = self._meta_data[i]
            old_meta = self._last_meta_data[i]
            patch_meta[i] = self._renderer.meta_patch(old_meta, new_meta)
            if patch_meta[i] is not None:
                modify = True

        if modify:
            return patch_meta

        return None
            
    def on_receive(self, time_str:str):
        '''直接接收来自时间管理器的时间字符串，并发送给前端'''
        data = self.render(time_str)
        if data:
            self.send_signal("rendered_time", data) #向前端发送信号："rendered_time"，内容为元数据