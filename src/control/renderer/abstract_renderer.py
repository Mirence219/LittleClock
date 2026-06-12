class AbstractRenderer:
    '''渲染器接口'''
    def __init__(self):
        self._mode = ""
        self._patch = False    #True：启用差分模式 False：默认全量输出
        self._meta = {}
        self._init_meta()
        
    def _init_meta(self):
        '''初始化元数据'''
        raise NotImplementedError(f"AbstractRenderer子类{self.__class__.__name__}未实现 _init_meta()")

    def render(self, input_str:str) -> dict:
        '''返回字符的渲染元数据（字典）'''
        raise NotImplementedError(f"AbstractRenderer子类{self.__class__.__name__}未实现 render()")

    def meta_patch(self, old_meta:dict, new_meta:dict) -> tuple:
        '''比对元数据差异, 返回 元组(add:set, off:set) 或者 None(无变化)'''
        raise NotImplementedError(f"AbstractRenderer子类{self.__class__.__name__}未实现 meta_patch()")

    @property
    def mode(self) -> str:
        '''返回模式信号'''
        return self._mode

    @property
    def patch(self) -> bool:
        '''返回差分/全量模式信息'''
        return self._patch

    @property
    def first_render(self) -> bool:
        '''返回是否为第一次输出'''
        return self._first_render

    