# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otherWindowiqRIRh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_otherWindow(object):
    def setupUi(self, otherWindow):
        if not otherWindow.objectName():
            otherWindow.setObjectName(u"otherWindow")
        otherWindow.resize(1317, 797)
        self.actionExit = QAction(otherWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(otherWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.savebtn = QPushButton(self.centralwidget)
        self.savebtn.setObjectName(u"savebtn")
        self.savebtn.setGeometry(QRect(1010, 450, 161, 51))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 711, 721))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.news = QTextEdit(self.groupBox)
        self.news.setObjectName(u"news")

        self.horizontalLayout_2.addWidget(self.news)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(730, 120, 451, 331))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mine = QTextEdit(self.groupBox_2)
        self.mine.setObjectName(u"mine")

        self.horizontalLayout_3.addWidget(self.mine)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(740, 30, 431, 71))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.lineEdit = QLineEdit(self.page_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 371, 31))
        self.pushButton_1 = QPushButton(self.page_1)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(390, 20, 31, 28))
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lineEdit_2 = QLineEdit(self.page_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 20, 371, 31))
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 20, 31, 28))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 20, 371, 31))
        self.pushButton_3 = QPushButton(self.page_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(390, 20, 31, 28))
        self.stackedWidget.addWidget(self.page_3)
        otherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(otherWindow)
        self.statusbar.setObjectName(u"statusbar")
        otherWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(otherWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1317, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        otherWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionExit)

        self.retranslateUi(otherWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(otherWindow)
    # setupUi

    def retranslateUi(self, otherWindow):
        otherWindow.setWindowTitle(QCoreApplication.translate("otherWindow", u"otherWindow", None))
        self.actionExit.setText(QCoreApplication.translate("otherWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("otherWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.savebtn.setText(QCoreApplication.translate("otherWindow", u"\uc800\uc7a5\ud558\uae30", None))
        self.groupBox.setTitle(QCoreApplication.translate("otherWindow", u"\ub274\uc2a4", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("otherWindow", u"\ub0b4 \uc0dd\uac01", None))
        self.lineEdit.setText(QCoreApplication.translate("otherWindow", u"\uc2a4\uc2a4\ub85c \uc815\uc758\ud560 \uc218 \uc5c6\ub294 \ub2e8\uc5b4\ub97c \uac80\uc0c9\ud574\ubcf4\uc138\uc694", None))
        self.pushButton_1.setText(QCoreApplication.translate("otherWindow", u">", None))
        self.lineEdit_2.setText(QCoreApplication.translate("otherWindow", u"\ubb38\uc7a5\uc740 \uc9e7\uac8c \uc4f0\uc138\uc694", None))
        self.pushButton_2.setText(QCoreApplication.translate("otherWindow", u">", None))
        self.lineEdit_3.setText(QCoreApplication.translate("otherWindow", u"\uc790\uc2e0\uc758 \uacbd\ud5d8\uacfc \ub274\uc2a4\ub97c \uc5ee\uc5b4\ubcf4\uc138\uc694", None))
        self.pushButton_3.setText(QCoreApplication.translate("otherWindow", u">", None))
        self.menu.setTitle(QCoreApplication.translate("otherWindow", u"\ud30c\uc77c", None))
    # retranslateUi

