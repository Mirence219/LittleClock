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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(370, 234)
        MainWindow.setStyleSheet(u"background-color: rgba(80, 80, 80, 160);\n"
"border-radius: 10px;\n"
"color: white")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbTitle = QLabel(self.centralwidget)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setMinimumSize(QSize(0, 0))
        self.lbTitle.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"padding-left:1\n"
"0px;\n"
"")
        self.lbTitle.setMargin(0)

        self.horizontalLayout.addWidget(self.lbTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bntSetting = QPushButton(self.centralwidget)
        self.bntSetting.setObjectName(u"bntSetting")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.bntSetting.setIcon(icon)

        self.horizontalLayout.addWidget(self.bntSetting)

        self.bntMinimize = QPushButton(self.centralwidget)
        self.bntMinimize.setObjectName(u"bntMinimize")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.bntMinimize.setIcon(icon1)

        self.horizontalLayout.addWidget(self.bntMinimize)

        self.bntClose = QPushButton(self.centralwidget)
        self.bntClose.setObjectName(u"bntClose")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.bntClose.setIcon(icon2)

        self.horizontalLayout.addWidget(self.bntClose)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wgtTimeboard = QWidget(self.centralwidget)
        self.wgtTimeboard.setObjectName(u"wgtTimeboard")
        self.wgtTimeboard.setMinimumSize(QSize(0, 100))
        self.wgtTimeboard.setStyleSheet(u"border: 1px solid #666; \n"
"border-radius: 8px;")

        self.verticalLayout_2.addWidget(self.wgtTimeboard)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.bnt3 = QPushButton(self.centralwidget)
        self.bnt3.setObjectName(u"bnt3")
        self.bnt3.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.bnt3, 0, 2, 1, 1)

        self.bnt2 = QPushButton(self.centralwidget)
        self.bnt2.setObjectName(u"bnt2")

        self.gridLayout.addWidget(self.bnt2, 0, 1, 1, 1)

        self.bnt1 = QPushButton(self.centralwidget)
        self.bnt1.setObjectName(u"bnt1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bnt1.sizePolicy().hasHeightForWidth())
        self.bnt1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bnt1, 0, 0, 1, 1)

        self.bnt4 = QPushButton(self.centralwidget)
        self.bnt4.setObjectName(u"bnt4")

        self.gridLayout.addWidget(self.bnt4, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LittleClock", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindow", u"LittleClock", None))
        self.bntSetting.setText("")
        self.bntMinimize.setText("")
        self.bntClose.setText("")
        self.bnt3.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e3", None))
        self.bnt2.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e2", None))
        self.bnt1.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e1", None))
        self.bnt4.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e4", None))
    # retranslateUi

