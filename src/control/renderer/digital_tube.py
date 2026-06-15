from src.control.renderer.abstract_renderer import AbstractRenderer

class DigitalTubeRenderer(AbstractRenderer):
    '''数码管渲染器'''

    #各个数字在数码管的显示位置（1-7）
    DIGITAL_TUBE_DIC = {
        "0":{2, 3, 4, 5, 6, 7},
        "1":{2, 7},
        "2":{3, 2, 1, 5, 6},
        "3":{3, 2, 1, 7, 6},
        "4":{4, 1, 2, 7},
        "5":{3, 4, 1, 7, 6},
        "6":{3, 4, 1, 5, 6, 7},
        "7":{3, 2, 7},
        "8":{1, 2, 3, 4, 5, 6, 7},
        "9":{1, 2, 3, 4, 6, 7},
        ".":{8},
        ":":{9}
    }


    def _init_meta(self):
        self._meta.update({
            "pos": set(),
            #"type":""       #number | colon | port
            })
        self._mode = "digital"


    def render(self, input_str:str, count:int = 0) -> dict:
        if input_str not in self.DIGITAL_TUBE_DIC: 
            raise ValueError("无法渲染非法的字符")

        self._meta["pos"] = self.DIGITAL_TUBE_DIC[input_str]
        if input_str == ":" and count > 5:    #实现冒号闪烁
            self._meta["pos"] = set()

        return self._meta.copy()

    def meta_patch(self, old_meta:dict, new_meta:dict) -> tuple | None:
        add_meta =  new_meta["pos"] - old_meta["pos"]   #通过差集运算快速得出变化的数码管位置
        remove_meta = old_meta["pos"] - new_meta["pos"]
        if add_meta or remove_meta:
            return (add_meta, remove_meta)
        else:
            return None





