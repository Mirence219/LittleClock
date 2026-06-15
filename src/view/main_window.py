from PySide6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu
from PySide6.QtCore import QEvent, QObject, QPoint, Qt
from PySide6.QtGui import QAction, QIcon
import os

from src.__version__ import resource_path
from src.logger import Logger
from src.view.py_ui.ui_main_window import Ui_MainWindow
from src.view.timeboard import TimeboardManager

class MainWindowManager(QObject):
    '''主窗口对象管理器'''
    def __init__(self, signal_sender):
        super().__init__()

        self.signal_sender = signal_sender

        self._init_main_window()
        self._init_timeboard()
        self._init_tray()
        self._connect_init()
        self._event_init()
        self._state_init()


    def _init_main_window(self):
        '''初始化主窗口'''
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.window.setWindowFlags(Qt.FramelessWindowHint      #去掉窗口上方标题栏
                                   |Qt.Tool)    #工具窗口
        self.window.setAttribute(Qt.WA_TranslucentBackground)   #设置透明窗口
        self.window.installEventFilter(self)    #给主窗口安装事件过滤器，拦截鼠标事件
        self.window_flags = self.window.windowFlags()    #获取窗口标记

    def _init_timeboard(self):
        '''初始化时间面板管理器'''
        self.timeboard = TimeboardManager(self.ui.wgtTimeboard)


    def _init_tray(self):
        '''初始化系统托盘'''
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(os.path.join(resource_path, "assets/LittleClock.ico")))
        self.tray_icon.setToolTip("LittleClock")

        self.tray_menu = QMenu()
        self.act_show = QAction("显示LittleClock", self.window)
        self.act_show.triggered.connect(self.show)
        self.act_quit = QAction("退出LittleClock", self)
        self.act_quit.triggered.connect(self.close)

        self.tray_menu.addAction(self.act_show)
        self.tray_menu.addSeparator()
        self.tray_menu.addAction(self.act_quit)
        self.tray_icon.setContextMenu(self.tray_menu)

        
        self.tray_icon.activated.connect(self.show)
        self.tray_icon.show()


    def _connect_init(self):
        '''绑定按键事件'''
        self.ui.bntClose.clicked.connect(self.on_bntClose_clicked)
        self.ui.bntTophint.clicked.connect(self.on_bntTophint_clicked)
        self.ui.bnt1.clicked.connect(self.on_bnt1_clicked)
        self.ui.bnt2.clicked.connect(self.on_bnt2_clicked)
        self.ui.bnt3.clicked.connect(self.on_bnt3_clicked)
        self.ui.bnt4.clicked.connect(self.on_bnt4_clicked)


    def _event_init(self):
        '''初始化事件变量'''
        self._draging = False       #鼠标是否按住
        self._offset = QPoint(0, 0) #计算偏移坐标


    def _state_init(self):
        '''屏幕与主窗口状态初始化'''
        self.screen_size = self.window.screen().availableGeometry()
        self.left_x = 0
        self.right_x = self.screen_size.width() - self.window_width
        self.top_y = 0
        self.button_y = self.screen_size.height() - self.window_height
        self.set_pos(self.right_x, self.top_y)  #默认右上角
        #self.set_pos(self.right_x, self.button_y)
        #self.set_pos(self.left_x, self.top_y)
        #self.set_pos(self.left_x, self.button_y)
        
        
    def send(self, signal:str, data):
        '''发送信号'''
        self.signal_sender.send(signal, data)


#========= 窗口控制 ===========

    def show(self):
        '''显示窗口'''
        self.window.setWindowState(Qt.WindowNoState)
        self.window.showNormal()
        self.window.raise_()
        self.window.activateWindow()

    def hide(self):
        '''隐藏窗口'''
        Logger.info("隐藏窗口")
        self.window.hide()


    def close(self):
        '''退出程序（关闭后端相关线程）'''
        Logger.info("请求后端终止计时。。。")
        self.send("shutdown", None)


    def confirm_close(self):
        '''确认退出程序（后端线程处理完毕）'''
        Logger.info("退出LittleClock程序")
        self.tray_icon.hide()
        self.window.close()


    def tophint(self):
        '''置顶窗口'''
        Logger.info("置顶窗口")
        self.window.setWindowFlags(self.window.windowFlags() | Qt.WindowStaysOnTopHint)
        self.window.show()


    def untophint(self):
        '''取消置顶窗口'''
        Logger.info("取消置顶窗口")
        self.window.setWindowFlags(self.window.windowFlags() &~ Qt.WindowStaysOnTopHint)
        self.window.show()


    def set_pos(self, x:int, y:int):
        '''设置窗口位置'''
        self.window.move(x, y)

#========= 状态查询 ===========

    @property
    def is_tophint(self) -> bool:
        '''窗口是否开启置顶'''
        return bool(self.window.windowFlags() & Qt.WindowStaysOnTopHint)
    

    @property
    def is_visible(self) -> bool:
        """Qt内部标记：窗口是否设置为可见（hide之后为False，Win+D遮挡仍为True）"""
        return self.window.isVisible()


    @property
    def is_hidden(self) -> bool:
        """窗口是否被主动hide隐藏"""
        return self.window.isHidden()


    @property
    def is_minimized(self) -> bool:
        """窗口是否处于最小化状态（未启用）"""
        return self.window.windowState() == Qt.WindowMinimized


    @property
    def is_maximized(self) -> bool:
        """窗口是否最大化（未启用）"""
        return self.window.windowState() == Qt.WindowMaximized


    @property
    def is_fullscreen(self) -> bool:
        """是否全屏（未启用）"""
        return self.window.windowState() == Qt.WindowFullScreen


    @property
    def is_normal(self) -> bool:
        """窗口是否普通正常模式（非最小/最大/全屏）"""
        return self.window.windowState() == Qt.WindowNoState


    @property
    def is_active(self) -> bool:
        """当前窗口是否是系统前台激活窗口（拿到焦点）"""
        return self.window.isActiveWindow()


    @property
    def window_width(self) -> int:
        """窗口当前宽度"""
        return self.window.width()


    @property
    def window_height(self) -> int:
        """窗口当前高度"""
        return self.window.height()


    @property
    def window_pos_x(self) -> int:
        """窗口左上角X坐标"""
        return self.window.x()


    @property
    def window_pos_y(self) -> int:
        """窗口左上角Y坐标"""
        return self.window.y()


#========= 事件回调 ===========

    def eventFilter(self, obj, event):
        '''鼠标事件拦截，由管理器处理业务'''
        # 只监听主窗口的事件
        if obj == self.window:
            # 鼠标左键按下
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self._draging = True
                # 计算偏移：全局鼠标坐标 - 窗口左上角
                self._offset = event.globalPosition().toPoint() - self.window.frameGeometry().topLeft()
                Logger.info("鼠标左键点击主窗口")

            # 鼠标移动
            elif event.type() == QEvent.MouseMove and self._draging:
                # 移动顶层窗口
                new_pos = event.globalPosition().toPoint() - self._offset
                self.window.move(new_pos)

            # 鼠标左键释放
            elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self._draging = False
                Logger.info("鼠标左键松开主窗口")

        # 必须返回，继续传递原有事件（保证按钮正常点击）
        return False


    def on_bntClose_clicked(self):
        '''关闭窗口（最小化到系统托盘）'''
        Logger.info("点击关闭窗口按钮（最小化至系统托盘）")
        self.hide()
        # 弹出气泡提示
        self.tray_icon.showMessage(
            "LittleClock",
            "程序已最小化至系统托盘，单击图标恢复窗口",
            QSystemTrayIcon.Information,
            2000
        )


    def on_bntTophint_clicked(self):
        '''置顶窗口'''
        Logger.info("点击置顶按钮")
        if not self.is_tophint:
            self.tophint()
        else:
            self.untophint()
            

    def on_bnt1_clicked(self):
        '''按钮1点击事件'''
        Logger.info("点击按钮1")
        self.send("按钮1", None)


    def on_bnt2_clicked(self):
        '''按钮2点击事件'''
        Logger.info("点击按钮2")
        self.send("按钮2", None)


    def on_bnt3_clicked(self):
        '''按钮3点击事件'''
        Logger.info("点击按钮3")
        self.send("按钮3", None)


    def on_bnt4_clicked(self):
        '''按钮4点击事件'''
        Logger.info("点击按钮4")
        self.send("按钮4", None)


