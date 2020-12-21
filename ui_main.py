# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maintMqdkE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1404, 824)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_toggle = QPushButton(self.frame_toggle)
        self.Btn_toggle.setObjectName(u"Btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_toggle.sizePolicy().hasHeightForWidth())
        self.Btn_toggle.setSizePolicy(sizePolicy)
        self.Btn_toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: Opx solid;")

        self.verticalLayout_2.addWidget(self.Btn_toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.frame_left_menu)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        self.frame_top_menu.setFrameShape(QFrame.NoFrame)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_menu_1 = QPushButton(self.frame_top_menu)
        self.Btn_menu_1.setObjectName(u"Btn_menu_1")
        self.Btn_menu_1.setMinimumSize(QSize(0, 40))
        self.Btn_menu_1.setStyleSheet(u"QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"    border: Opx solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_menu_1)

        self.Btn_menu_2 = QPushButton(self.frame_top_menu)
        self.Btn_menu_2.setObjectName(u"Btn_menu_2")
        self.Btn_menu_2.setMinimumSize(QSize(0, 40))
        self.Btn_menu_2.setStyleSheet(u"QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"    border: Opx solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_menu_2)

        self.Btn_menu_3 = QPushButton(self.frame_top_menu)
        self.Btn_menu_3.setObjectName(u"Btn_menu_3")
        self.Btn_menu_3.setMinimumSize(QSize(0, 40))
        self.Btn_menu_3.setStyleSheet(u"QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"    border: Opx solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_menu_3)


        self.verticalLayout_3.addWidget(self.frame_top_menu, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.Pages_Widget.setStyleSheet(u"background-color: rgb(247, 242, 232);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMaximumSize(QSize(730, 16777215))
        self.page_1.setStyleSheet(u"")
        self.verticalLayoutWidget_2 = QWidget(self.page_1)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(850, 0, 491, 1171))
        self.rightLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightscrollArea = QScrollArea(self.verticalLayoutWidget_2)
        self.rightscrollArea.setObjectName(u"rightscrollArea")
        self.rightscrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 466, 3000))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 3000))
        self.frame.setStyleSheet(u"background-color: rgb(222, 206, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 461, 401))
        self.layout_R0 = QVBoxLayout(self.layoutWidget)
        self.layout_R0.setObjectName(u"layout_R0")
        self.layout_R0.setContentsMargins(0, 0, 0, 0)
        self.groupBox_R0 = QGroupBox(self.layoutWidget)
        self.groupBox_R0.setObjectName(u"groupBox_R0")
        self.textEdit_R0 = QTextEdit(self.groupBox_R0)
        self.textEdit_R0.setObjectName(u"textEdit_R0")
        self.textEdit_R0.setGeometry(QRect(10, 20, 441, 371))
        self.textEdit_R0.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_R0 = QPushButton(self.groupBox_R0)
        self.pushButton_R0.setObjectName(u"pushButton_R0")
        self.pushButton_R0.setGeometry(QRect(340, 360, 93, 28))

        self.layout_R0.addWidget(self.groupBox_R0)

        self.layoutWidget_2 = QWidget(self.frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 410, 461, 401))
        self.layout_R1 = QVBoxLayout(self.layoutWidget_2)
        self.layout_R1.setObjectName(u"layout_R1")
        self.layout_R1.setContentsMargins(0, 0, 0, 0)
        self.groupBox_R1 = QGroupBox(self.layoutWidget_2)
        self.groupBox_R1.setObjectName(u"groupBox_R1")
        self.textEdit_R1 = QTextEdit(self.groupBox_R1)
        self.textEdit_R1.setObjectName(u"textEdit_R1")
        self.textEdit_R1.setGeometry(QRect(10, 20, 441, 371))
        self.textEdit_R1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_R1 = QPushButton(self.groupBox_R1)
        self.pushButton_R1.setObjectName(u"pushButton_R1")
        self.pushButton_R1.setGeometry(QRect(340, 360, 93, 28))

        self.layout_R1.addWidget(self.groupBox_R1)

        self.layoutWidget_3 = QWidget(self.frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 820, 461, 401))
        self.layout_R2 = QVBoxLayout(self.layoutWidget_3)
        self.layout_R2.setObjectName(u"layout_R2")
        self.layout_R2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_R2 = QGroupBox(self.layoutWidget_3)
        self.groupBox_R2.setObjectName(u"groupBox_R2")
        self.textEdit_R2 = QTextEdit(self.groupBox_R2)
        self.textEdit_R2.setObjectName(u"textEdit_R2")
        self.textEdit_R2.setGeometry(QRect(10, 20, 441, 371))
        self.textEdit_R2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_R2 = QPushButton(self.groupBox_R2)
        self.pushButton_R2.setObjectName(u"pushButton_R2")
        self.pushButton_R2.setGeometry(QRect(340, 360, 93, 28))

        self.layout_R2.addWidget(self.groupBox_R2)

        self.layoutWidget_4 = QWidget(self.frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 1230, 461, 401))
        self.layout_R3 = QVBoxLayout(self.layoutWidget_4)
        self.layout_R3.setObjectName(u"layout_R3")
        self.layout_R3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_R3 = QGroupBox(self.layoutWidget_4)
        self.groupBox_R3.setObjectName(u"groupBox_R3")
        self.textEdit_R3 = QTextEdit(self.groupBox_R3)
        self.textEdit_R3.setObjectName(u"textEdit_R3")
        self.textEdit_R3.setGeometry(QRect(10, 20, 441, 371))
        self.textEdit_R3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_R3 = QPushButton(self.groupBox_R3)
        self.pushButton_R3.setObjectName(u"pushButton_R3")
        self.pushButton_R3.setGeometry(QRect(340, 360, 93, 28))

        self.layout_R3.addWidget(self.groupBox_R3)

        self.layoutWidget_5 = QWidget(self.frame)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 1640, 461, 401))
        self.layout_R4 = QVBoxLayout(self.layoutWidget_5)
        self.layout_R4.setObjectName(u"layout_R4")
        self.layout_R4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_R4 = QGroupBox(self.layoutWidget_5)
        self.groupBox_R4.setObjectName(u"groupBox_R4")
        self.textEdit_R4 = QTextEdit(self.groupBox_R4)
        self.textEdit_R4.setObjectName(u"textEdit_R4")
        self.textEdit_R4.setGeometry(QRect(10, 20, 441, 371))
        self.textEdit_R4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_R4 = QPushButton(self.groupBox_R4)
        self.pushButton_R4.setObjectName(u"pushButton_R4")
        self.pushButton_R4.setGeometry(QRect(340, 360, 93, 28))

        self.layout_R4.addWidget(self.groupBox_R4)

        self.layoutWidget_6 = QWidget(self.frame)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 2050, 461, 401))
        self.layout_R5 = QVBoxLayout(self.layoutWidget_6)
        self.layout_R5.setObjectName(u"layout_R5")
        self.layout_R5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_R5 = QGroupBox(self.layoutWidget_6)
        self.groupBox_R5.setObjectName(u"groupBox_R5")
        self.textEdit_R5 = QTextEdit(self.groupBox_R5)
        self.textEdit_R5.setObjectName(u"textEdit_R5")
        self.textEdit_R5.setGeometry(QRect(10, 20, 441, 371))
        self.textEdit_R5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_R5 = QPushButton(self.groupBox_R5)
        self.pushButton_R5.setObjectName(u"pushButton_R5")
        self.pushButton_R5.setGeometry(QRect(340, 360, 93, 28))

        self.layout_R5.addWidget(self.groupBox_R5)

        self.layoutWidget_7 = QWidget(self.frame)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 2460, 461, 401))
        self.layout_R6 = QVBoxLayout(self.layoutWidget_7)
        self.layout_R6.setObjectName(u"layout_R6")
        self.layout_R6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_R6 = QGroupBox(self.layoutWidget_7)
        self.groupBox_R6.setObjectName(u"groupBox_R6")
        self.textEdit_R6 = QTextEdit(self.groupBox_R6)
        self.textEdit_R6.setObjectName(u"textEdit_R6")
        self.textEdit_R6.setGeometry(QRect(10, 20, 441, 371))
        self.textEdit_R6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_R6 = QPushButton(self.groupBox_R6)
        self.pushButton_R6.setObjectName(u"pushButton_R6")
        self.pushButton_R6.setGeometry(QRect(340, 360, 93, 28))

        self.layout_R6.addWidget(self.groupBox_R6)


        self.verticalLayout_6.addWidget(self.frame)

        self.rightscrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.rightLayout.addWidget(self.rightscrollArea)

        self.gridLayoutWidget_3 = QWidget(self.page_1)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(9, -1, 701, 781))
        self.leftLayout = QGridLayout(self.gridLayoutWidget_3)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.gridLayoutWidget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(247, 241, 229);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 676, 5000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 5000))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 30, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.leftLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.Pages_Widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(126, 126, 126);")
        self.Pages_Widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMinimumSize(QSize(1307, 0))
        self.verticalLayoutWidget = QWidget(self.page_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 1391, 761))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1366, 5022))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget = QWidget(self.scrollAreaWidgetContents_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 5000))
        self.refreshButton = QPushButton(self.widget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(40, 20, 93, 28))
        self.refreshButton.setStyleSheet(u"background-color: rgb(103, 255, 133);")

        self.verticalLayout_11.addWidget(self.widget)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_2)

        self.Pages_Widget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.Btn_menu_1.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc2a4", None))
        self.Btn_menu_2.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.Btn_menu_3.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5\uc18c", None))
        self.groupBox_R0.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_R0.setText(QCoreApplication.translate("MainWindow", u"\ud655\ub300\ud558\uae30", None))
        self.groupBox_R1.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_R1.setText(QCoreApplication.translate("MainWindow", u"\ud655\ub300\ud558\uae30", None))
        self.groupBox_R2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_R2.setText(QCoreApplication.translate("MainWindow", u"\ud655\ub300\ud558\uae30", None))
        self.groupBox_R3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_R3.setText(QCoreApplication.translate("MainWindow", u"\ud655\ub300\ud558\uae30", None))
        self.groupBox_R4.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_R4.setText(QCoreApplication.translate("MainWindow", u"\ud655\ub300\ud558\uae30", None))
        self.groupBox_R5.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_R5.setText(QCoreApplication.translate("MainWindow", u"\ud655\ub300\ud558\uae30", None))
        self.groupBox_R6.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_R6.setText(QCoreApplication.translate("MainWindow", u"\ud655\ub300\ud558\uae30", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"\uc0c8\ub85c\uace0\uce68", None))
    # retranslateUi

