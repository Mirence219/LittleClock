# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from src.view.timeboard import Timeboard

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(268, 221)
        MainWindow.setStyleSheet(u"background-color: rgba(80, 80, 80, 160);\n"
"border-radius: 10px;\n"
"color: white")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frmIndex = QFrame(self.centralWidget)
        self.frmIndex.setObjectName(u"frmIndex")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmIndex.sizePolicy().hasHeightForWidth())
        self.frmIndex.setSizePolicy(sizePolicy)
        self.frmIndex.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        self.horizontalLayout = QHBoxLayout(self.frmIndex)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbTitle = QLabel(self.frmIndex)
        self.lbTitle.setObjectName(u"lbTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbTitle.sizePolicy().hasHeightForWidth())
        self.lbTitle.setSizePolicy(sizePolicy1)
        self.lbTitle.setMinimumSize(QSize(0, 0))
        self.lbTitle.setMaximumSize(QSize(16777215, 30))
        self.lbTitle.setStyleSheet(u"font: 700 13pt \"Microsoft YaHei UI\";\n"
"padding-left:3px;\n"
"border-radius: 10px;\n"
"background-color: rgba(80, 80, 80, 160);")
        self.lbTitle.setMargin(0)

        self.horizontalLayout.addWidget(self.lbTitle)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frmTitleBtn = QFrame(self.frmIndex)
        self.frmTitleBtn.setObjectName(u"frmTitleBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frmTitleBtn.sizePolicy().hasHeightForWidth())
        self.frmTitleBtn.setSizePolicy(sizePolicy2)
        self.frmTitleBtn.setMaximumSize(QSize(16777215, 50))
        self.frmTitleBtn.setToolTipDuration(-1)
        self.frmTitleBtn.setStyleSheet(u"#frmTitleBtn {\n"
"	background: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"#frmTitleBtn QPushButton {\n"
"	background: rgba(0, 0, 0, 0);\n"
"	font: 20pt \"iconfont\";\n"
"	color: rgba(255, 255, 255, 255);\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"#frmTitleBtn QPushButton:hover {\n"
"    color: rgba(255,255,255,128);\n"
"}")
        self.frmTitleBtn.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmTitleBtn.setFrameShadow(QFrame.Shadow.Raised)
        self.frmTitleBtn.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frmTitleBtn)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnSetting = QPushButton(self.frmTitleBtn)
        self.btnSetting.setObjectName(u"btnSetting")
        sizePolicy2.setHeightForWidth(self.btnSetting.sizePolicy().hasHeightForWidth())
        self.btnSetting.setSizePolicy(sizePolicy2)
        self.btnSetting.setMaximumSize(QSize(16777215, 30))
        self.btnSetting.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnSetting)

        self.btnTophint = QPushButton(self.frmTitleBtn)
        self.btnTophint.setObjectName(u"btnTophint")
        sizePolicy2.setHeightForWidth(self.btnTophint.sizePolicy().hasHeightForWidth())
        self.btnTophint.setSizePolicy(sizePolicy2)
        self.btnTophint.setMaximumSize(QSize(16777215, 30))
        self.btnTophint.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnTophint.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnTophint)

        self.btnClose = QPushButton(self.frmTitleBtn)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy2.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy2)
        self.btnClose.setMaximumSize(QSize(16777215, 30))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.horizontalLayout.addWidget(self.frmTitleBtn, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.lbTitle.raise_()
        self.frmTitleBtn.raise_()

        self.verticalLayout.addWidget(self.frmIndex)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wgtTimeboard = Timeboard(self.centralWidget)
        self.wgtTimeboard.setObjectName(u"wgtTimeboard")
        self.wgtTimeboard.setMinimumSize(QSize(0, 100))
        self.wgtTimeboard.setStyleSheet(u"#wgtTimeboard {\n"
"	border: 2px solid #666; \n"
"	border-radius: 8px;\n"
"	background: rgba(255, 255, 255, 0)\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.wgtTimeboard)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_2.addWidget(self.wgtTimeboard)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.lbLine = QLabel(self.centralWidget)
        self.lbLine.setObjectName(u"lbLine")
        self.lbLine.setMaximumSize(QSize(16777215, 1))
        self.lbLine.setStyleSheet(u"background-color: #666")

        self.verticalLayout.addWidget(self.lbLine)

        self.frmControll = QFrame(self.centralWidget)
        self.frmControll.setObjectName(u"frmControll")
        sizePolicy.setHeightForWidth(self.frmControll.sizePolicy().hasHeightForWidth())
        self.frmControll.setSizePolicy(sizePolicy)
        self.frmControll.setStyleSheet(u"#frmControll {\n"
"	background: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"#frmControll QPushButton {\n"
"	background-color: rgba(80, 80, 80, 160);\n"
"}\n"
"\n"
"#frmControll QPushButton:hover{\n"
"	background-color: rgba(40, 40, 40, 160);\n"
"}")
        self.gridLayout = QGridLayout(self.frmControll)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, -1, 1, -1)
        self.btn3 = QPushButton(self.frmControll)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(0, 25))
        self.btn3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)

        self.btn2 = QPushButton(self.frmControll)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(0, 25))
        self.btn2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)

        self.btn1 = QPushButton(self.frmControll)
        self.btn1.setObjectName(u"btn1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy3)
        self.btn1.setMinimumSize(QSize(0, 25))
        self.btn1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)

        self.btn4 = QPushButton(self.frmControll)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(0, 25))
        self.btn4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frmControll)

        MainWindow.setCentralWidget(self.centralWidget)
        QWidget.setTabOrder(self.btn1, self.btn2)
        QWidget.setTabOrder(self.btn2, self.btn3)
        QWidget.setTabOrder(self.btn3, self.btn4)
        QWidget.setTabOrder(self.btn4, self.btnSetting)
        QWidget.setTabOrder(self.btnSetting, self.btnTophint)
        QWidget.setTabOrder(self.btnTophint, self.btnClose)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LittleClock", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindow", u"LittleClock", None))
        self.btnSetting.setText(QCoreApplication.translate("MainWindow", u"\ue663", None))
        self.btnTophint.setText(QCoreApplication.translate("MainWindow", u"\ue60f", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"\ue6e8", None))
        self.lbLine.setText("")
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e3", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e2", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e1", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e4", None))
    # retranslateUi

