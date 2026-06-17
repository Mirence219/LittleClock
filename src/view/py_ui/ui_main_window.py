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
        MainWindow.resize(210, 222)
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
        self.frmTitleBtn.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        self.frmTitleBtn.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmTitleBtn.setFrameShadow(QFrame.Shadow.Raised)
        self.frmTitleBtn.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frmTitleBtn)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bntSetting = QPushButton(self.frmTitleBtn)
        self.bntSetting.setObjectName(u"bntSetting")
        sizePolicy2.setHeightForWidth(self.bntSetting.sizePolicy().hasHeightForWidth())
        self.bntSetting.setSizePolicy(sizePolicy2)
        self.bntSetting.setMaximumSize(QSize(16777215, 30))
        self.bntSetting.setStyleSheet(u"background: rgba(0, 0, 0, 0);\n"
"font: 20pt \"iconfont\";\n"
"color: rgba(255, 255, 255, 255);\n"
"padding-left: 5px;\n"
"\n"
"bntSetting::hover {\n"
"    background: rgba(255,255,255,128);\n"
"}")

        self.horizontalLayout_2.addWidget(self.bntSetting)

        self.bntTophint = QPushButton(self.frmTitleBtn)
        self.bntTophint.setObjectName(u"bntTophint")
        sizePolicy2.setHeightForWidth(self.bntTophint.sizePolicy().hasHeightForWidth())
        self.bntTophint.setSizePolicy(sizePolicy2)
        self.bntTophint.setMaximumSize(QSize(16777215, 30))
        self.bntTophint.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bntTophint.setStyleSheet(u"background: rgba(0, 0, 0, 0);\n"
"font: 20pt \"iconfont\";\n"
"color: rgba(255, 255, 255, 255);\n"
"padding-left: 5px;\n"
"\n"
"bntTophint::hover {\n"
"    background: rgba(255,255,255,128);\n"
"}")

        self.horizontalLayout_2.addWidget(self.bntTophint)

        self.bntClose = QPushButton(self.frmTitleBtn)
        self.bntClose.setObjectName(u"bntClose")
        sizePolicy2.setHeightForWidth(self.bntClose.sizePolicy().hasHeightForWidth())
        self.bntClose.setSizePolicy(sizePolicy2)
        self.bntClose.setMaximumSize(QSize(16777215, 30))
        self.bntClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bntClose.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"font: 20pt \"iconfont\";\n"
"color: rgba(255, 255, 255, 255);\n"
"padding-left: 5px;\n"
"\n"
"bntClose::hover {\n"
"    color: rgba(255,255,255,128);\n"
"}")

        self.horizontalLayout_2.addWidget(self.bntClose)


        self.horizontalLayout.addWidget(self.frmTitleBtn, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.lbTitle.raise_()
        self.frmTitleBtn.raise_()

        self.verticalLayout.addWidget(self.frmIndex)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wgtTimeboard = Timeboard(self.centralWidget)
        self.wgtTimeboard.setObjectName(u"wgtTimeboard")
        self.wgtTimeboard.setMinimumSize(QSize(0, 100))
        self.wgtTimeboard.setStyleSheet(u"border: 1px solid #666; \n"
"border-radius: 8px;\n"
"background: rgba(80, 80, 80, 160);")

        self.verticalLayout_2.addWidget(self.wgtTimeboard)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.frame = QFrame(self.centralWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, -1, 1, -1)
        self.bnt3 = QPushButton(self.frame)
        self.bnt3.setObjectName(u"bnt3")
        self.bnt3.setMinimumSize(QSize(0, 25))
        self.bnt3.setStyleSheet(u"background-color: rgba(80, 80, 80, 160);")

        self.gridLayout.addWidget(self.bnt3, 0, 2, 1, 1)

        self.bnt2 = QPushButton(self.frame)
        self.bnt2.setObjectName(u"bnt2")
        self.bnt2.setMinimumSize(QSize(0, 25))
        self.bnt2.setStyleSheet(u"background-color: rgba(80, 80, 80, 160);")

        self.gridLayout.addWidget(self.bnt2, 0, 1, 1, 1)

        self.bnt1 = QPushButton(self.frame)
        self.bnt1.setObjectName(u"bnt1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bnt1.sizePolicy().hasHeightForWidth())
        self.bnt1.setSizePolicy(sizePolicy3)
        self.bnt1.setMinimumSize(QSize(0, 25))
        self.bnt1.setStyleSheet(u"background-color: rgba(80, 80, 80, 160);")

        self.gridLayout.addWidget(self.bnt1, 0, 0, 1, 1)

        self.bnt4 = QPushButton(self.frame)
        self.bnt4.setObjectName(u"bnt4")
        self.bnt4.setMinimumSize(QSize(0, 25))
        self.bnt4.setStyleSheet(u"background-color: rgba(80, 80, 80, 160);")

        self.gridLayout.addWidget(self.bnt4, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralWidget)
        QWidget.setTabOrder(self.bnt1, self.bnt2)
        QWidget.setTabOrder(self.bnt2, self.bnt3)
        QWidget.setTabOrder(self.bnt3, self.bnt4)
        QWidget.setTabOrder(self.bnt4, self.bntSetting)
        QWidget.setTabOrder(self.bntSetting, self.bntTophint)
        QWidget.setTabOrder(self.bntTophint, self.bntClose)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LittleClock", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindow", u"LittleClock", None))
        self.bntSetting.setText(QCoreApplication.translate("MainWindow", u"\ue663", None))
        self.bntTophint.setText(QCoreApplication.translate("MainWindow", u"\ue60f", None))
        self.bntClose.setText(QCoreApplication.translate("MainWindow", u"\ue6e8", None))
        self.bnt3.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e3", None))
        self.bnt2.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e2", None))
        self.bnt1.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e1", None))
        self.bnt4.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e4", None))
    # retranslateUi

