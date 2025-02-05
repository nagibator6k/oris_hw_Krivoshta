# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 260)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bg1 = QLabel(self.centralwidget)
        self.bg1.setObjectName(u"bg1")
        self.bg1.setGeometry(QRect(0, 0, 463, 260))
        self.bg1.setPixmap(QPixmap(u":/image/images/background.jpg"))
        self.bg1.setScaledContents(False)
        self.bg2 = QLabel(self.centralwidget)
        self.bg2.setObjectName(u"bg2")
        self.bg2.setGeometry(QRect(463, 0, 463, 260))
        self.bg2.setPixmap(QPixmap(u":/image/images/background.jpg"))
        self.player = QLabel(self.centralwidget)
        self.player.setObjectName(u"player")
        self.player.setGeometry(QRect(0, 160, 121, 101))
        self.player.setPixmap(QPixmap(u":/image/images/player.png"))
        self.player.setScaledContents(True)
        self.rocket = QLabel(self.centralwidget)
        self.rocket.setObjectName(u"rocket")
        self.rocket.setGeometry(QRect(490, 210, 41, 41))
        self.rocket.setPixmap(QPixmap(u":/image/images/rocket.png"))
        self.rocket.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bg1.setText("")
        self.bg2.setText("")
        self.player.setText("")
        self.rocket.setText("")
    # retranslateUi

