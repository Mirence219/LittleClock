from PySide6.QtGui import QColor, QPainter, QPen, Qt
from PySide6.QtWidgets import QWidget

from src.logger import Logger


class TimeboardManager:
    '''时间面板对象管理器'''
    def __init__(self, paint):
        self.paint = paint

    def _update(self):
        '''刷新时间面板'''
        self.paint.update()

    def set_time(self, render_data:list):
        '''修改渲染元数据并刷新时间'''
        self.paint.set_render_data(render_data)
        self._update()



class Timeboard(QWidget):
    '''时间面板对象（提升自wgtTimeboard控件）'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_style()
        self._render_data = [{"pos": {1, 2, 3, 4, 5, 6, 7}},
                            {"pos": {1, 2, 3, 4, 5, 6, 7}},
                            {"pos": {9}},                   #冒号
                            {"pos": {1, 2, 3, 4, 5, 6, 7}},
                            {"pos": {1, 2, 3, 4, 5, 6, 7}}]
        self._full = True
        self._mode = "digital"
        self._num_count = 5


    def _init_style(self):
        '''初始化画板样式'''
        self.setAttribute(Qt.WA_TranslucentBackground)  #启用透明背景
        self.setAutoFillBackground(False)               #关闭自动背景填充
        self.pen_style = QPen(QColor(255, 255, 255), 4)
        self.bg_style = QColor(0, 0, 0, 0)


    def set_render_data(self, render_data:dict):
        '''设置渲染元数据'''
        self._mode = render_data[0]
        self._full = render_data[1]
        self._render_data = render_data[2:]


    def paintEvent(self, event):
        '''设置画板逻辑'''
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)  #启用抗锯齿
        painter.fillRect(self.rect(), self.bg_style)
        painter.setPen(self.pen_style)

        rect = self.rect()
        canvas_w = rect.width()
        canvas_h = min(rect.height(), canvas_w // self._num_count * 2)

        # 2. 动态计算数码管尺寸（按画布比例）
        global seg_h
        seg_h = canvas_h * 0.55             # 数字高度 = 画布高度60%
        seg_w = seg_h * 0.6                 # 数字宽度按高度比例
        gap = seg_h * 0.12                  # 段间隙自适应
        digit_gap = seg_w * 0.7             # 数字之间间距
        colon_gap = seg_w * 0.6             # 数字与冒号间距
        dot_r = seg_h * 0.08                # 冒号圆点大小
        pen_width = seg_h / 15
        self.pen_style.setWidthF(pen_width)

        # 3. 计算整体总宽度，实现整体水平居中
        total_w = seg_w * 4 + digit_gap * 2 + colon_gap * 2
        start_x = (canvas_w - total_w) / 2
        # 垂直居中
        start_y = (rect.height() - seg_h) / 2

        # 依次绘制 8 8 : 8 8
        # 第1个8
        self.draw_digit_8(painter, start_x, start_y, seg_w, seg_h, gap, self._render_data[0])
        # 第2个8
        x2 = start_x + seg_w + digit_gap
        self.draw_digit_8(painter, x2, start_y, seg_w, seg_h, gap, self._render_data[1])
        # 冒号
        colon_x = x2 + seg_w + colon_gap
        colon_y = start_y + seg_h * 0.2
        self.draw_colon(painter, colon_x, colon_y, dot_r, self._render_data[2])
        # 第3个8
        x3 = colon_x + dot_r + colon_gap
        self.draw_digit_8(painter, x3, start_y, seg_w, seg_h, gap, self._render_data[3])
        # 第4个8
        x4 = x3 + seg_w + digit_gap
        self.draw_digit_8(painter, x4, start_y, seg_w, seg_h, gap, self._render_data[4])

        painter.end()   #销毁画笔

    def draw_digit_8(self, painter, x, y, seg_w, seg_h, gap, render_data):
        """绘制单个数码管，根据 render_data 点亮对应段"""
        # 顶部横段 3
        if 3 in render_data["pos"]:
            painter.drawLine(x + gap, y, x + seg_w, y)
        # 右上竖段 2
        if 2 in render_data["pos"]:
            painter.drawLine(x + seg_w, y + gap, x + seg_w, y + seg_h // 2 - gap)
        # 右下竖段 7
        if 7 in render_data["pos"]:
            painter.drawLine(x + seg_w, y + seg_h // 2 + gap, x + seg_w, y + seg_h - gap)
        # 底部横段 6
        if 6 in render_data["pos"]:
            painter.drawLine(x + gap, y + seg_h, x + seg_w, y + seg_h)
        # 左下竖段 5
        if 5 in render_data["pos"]:
            painter.drawLine(x, y + seg_h // 2 + gap, x, y + seg_h - gap)
        # 左上竖段 4
        if 4 in render_data["pos"]:
            painter.drawLine(x, y + gap, x, y + seg_h // 2 - gap)
        # 中间横段 1
        mid_y = y + seg_h // 2
        if 1 in render_data["pos"]:
            painter.drawLine(x + gap, mid_y, x + seg_w, mid_y)

    def draw_colon(self, painter, x, y, dot_r, render_data):
        """绘制冒号圆点，大小动态适配"""
        if 9 in render_data["pos"]:
            painter.drawEllipse(x, y, dot_r, dot_r)
            painter.drawEllipse(x, y + seg_h * 0.4, dot_r, dot_r)


