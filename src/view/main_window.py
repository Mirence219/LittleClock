from PySide6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu
from PySide6.QtCore import QEvent, QObject, QPoint, Qt
from PySide6.QtGui import QAction, QIcon
import os

from logger import Logger
from view.py_ui.ui_main_window import Ui_MainWindow
from view.timeboard import TimeboardManager

class MainWindowManager(QObject):
    '''主窗口对象管理器'''
    def __init__(self, signal_sender):
        super().__init__()

        self.signal_sender = signal_sender
        self._init_main_window()
        self._init_timeboard()
        self._init_tray()
        self._connect_init()

        self._draging = False
        self._offset = QPoint(0, 0)


    def _init_main_window(self):
        '''初始化主窗口'''
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.window.setWindowFlags(Qt.FramelessWindowHint)      #去掉窗口上方标题栏
        self.window.setAttribute(Qt.WA_TranslucentBackground)   #设置透明窗口

        self.window.installEventFilter(self)    #给主窗口安装事件过滤器，拦截鼠标事件


    def _init_timeboard(self):
        '''初始化时间面板管理器'''
        self.timeboard = TimeboardManager(self.ui.wgtTimeboard)

    def _init_tray(self):
        '''初始化系统托盘'''
        # ========== 初始化托盘 ==========
        self.tray_icon = QSystemTrayIcon(self)
        # 托盘图标（必须设置，可放你的项目图标，没有就用系统默认）
        self.tray_icon.setIcon(QIcon(r"assets\LittleClock.ico"))
        # 鼠标悬浮托盘提示文字
        self.tray_icon.setToolTip("LittleClock")

        # 托盘右键菜单
        self.tray_menu = QMenu()
        # 显示窗口菜单项
        self.act_show = QAction("显示LittleClock", self.window)
        self.act_show.triggered.connect(self.show)
        # 退出程序菜单项
        self.act_quit = QAction("退出LittleClock", self)
        self.act_quit.triggered.connect(self.close)

        self.tray_menu.addAction(self.act_show)
        self.tray_menu.addSeparator()
        self.tray_menu.addAction(self.act_quit)
        self.tray_icon.setContextMenu(self.tray_menu)

        # 托盘双击事件：双击图标还原窗口
        self.tray_icon.activated.connect(self.show)

        # 启用托盘显示
        self.tray_icon.show()


    def _connect_init(self):
        '''绑定按键事件'''
        self.ui.bntClose.clicked.connect(self.on_bntClose_clicked)
        self.ui.bntMinimize.clicked.connect(self.on_bntMinimise_clicked)
        self.ui.bnt1.clicked.connect(self.on_bnt1_clicked)
        self.ui.bnt2.clicked.connect(self.on_bnt2_clicked)
        self.ui.bnt3.clicked.connect(self.on_bnt3_clicked)
        self.ui.bnt4.clicked.connect(self.on_bnt4_clicked)
    
    def show(self):
        '''启动窗口'''
        self.window.show()
        self.window.raise_()

    def close(self):
        '''关闭窗口（退出程序）'''
        Logger.info("退出LittleClock程序")
        self.tray_icon.hide()
        self.window.close()

    def send(self, signal:str, data):
        '''发送信号'''
        self.signal_sender.send(signal, data)


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
        '''直接关闭窗口（最小化到系统托盘）'''
        Logger.info("点击关闭窗口（最小化至系统托盘）")
        self.window.hide()
        # 弹出气泡提示（可选）
        self.tray_icon.showMessage(
            "LittleClock",
            "程序已最小化至系统托盘，单击图标恢复窗口",
            QSystemTrayIcon.Information,
            2000
        )

    def on_bntMinimise_clicked(self):
        ''''最小化窗口'''
        Logger.info("点击最小化窗口")
        self.window.setWindowState(Qt.WindowMinimized)
 

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


