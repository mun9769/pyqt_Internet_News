################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
import time
import os
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QTimer,QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from datetime import datetime
from NewsThread import threading_lst,flag
import sqlite3
# GUI FILE
from ui_main import Ui_MainWindow
from ui_otherWindow import Ui_otherWindow
# IMPORT FUNCTIONS
from ui_functions import *

      
class MainWindow(QMainWindow):
    def __init__(self,lst):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.Boxes = []
        self.newlist =[]
        self.today_news_list = lst

        self.Refresh()

        self.show()
        

    def de(self):
        for Box in self.Boxes:
            Box.deleteLater()
        self.Boxes = []
            

    def Refresh(self):
        self.newlist = []
        self.Boxes = []
        self.ui.setupUi(self)

        for ele in self.today_news_list:
            if len(ele) <100:
                continue
            new = news(ele)
            self.newlist.append(new)
        
        conn = sqlite3.connect("Opinion.db") 
        cur = conn.cursor()
        cur.execute("SELECT * FROM Box")
        rows = cur.fetchall()
        
        all_len = 0
        for idx,row in enumerate(rows):
            if len(row[1])< 100:
                all_len += 60
            elif len(row[1])< 300:
                all_len += 200
            else:
                all_len += 500
            all_len += 20    
        # print(all_len)

        for idx, row in enumerate(rows):
            if len(row[1])< 100:
                all_len -= 80
            elif len(row[1])< 300:
                all_len -= 220
            else:
                all_len -= 520 
            Box(self.ui.widget,idx,row[0],row[1],all_len+50)
        
        conn.commit()
        conn.close()

        for new in self.newlist:
            self.ui.verticalLayout_7.addLayout(new.layout)
        
        self.ui.Btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        
        self.ui.refreshButton.clicked.connect(self.Refresh)
    
        self.ui.Btn_menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        self.ui.Btn_menu_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2))
        self.ui.Btn_menu_3.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))


        

class Box(QWidget):
    def __init__(self,_some,_idx,_news,_thought,_pos):
        self.pos = _pos
        self.thought_len = 0
        self.idx = _idx
        
        
        QWidget.__init__(self,_some) 
        if len(_thought)<100:
            self.thought_len = 60
        elif len(_thought)< 300 :
            self.thought_len = 200
        else:
            self.thought_len = 500
        
        self.setGeometry(10,self.pos,320,self.thought_len+40)

        self.thought = QTextEdit(self)
        self.thought.setGeometry(QRect(20, 20, 300, self.thought_len))
        self.thought.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.thought.setText(str(_thought))

        self.news = QTextEdit(self) 
        self.news.setGeometry(QRect(340, 20, 600, 1400))
        self.news.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.news.setText(str(_news))

        self.openbtn = QPushButton("∇",self)
        self.openbtn.setGeometry(QRect(290, self.thought_len, 30, 30))
        self.openbtn.clicked.connect(self.openAndclose) #얘는 왜 lambda 안붙여줘야하냐?

        self.modifybtn = QPushButton("m",self)
        self.modifybtn.setGeometry(QRect(250, self.thought_len, 30, 30))
        self.modifybtn.clicked.connect(lambda: self.modifyBox(_thought))

        self.deletebtn = QPushButton("d",self)
        self.deletebtn.setGeometry(QRect(30, self.thought_len, 14, 14))
        # self.deletebtn.setIcon(QIcon('bin.jpg'))
        # self.deletebtn.setIconSize(QSize(400,400))
        self.deletebtn.clicked.connect(lambda: self.deleteBox(_thought)) # 왜 self.str_thought로 하고 Refresh()호출하면 화면갱신이 안되지

    def openAndclose(self):
        myGeo = self.geometry()
        maxGeo = QRect(10,self.pos,961,1400)
        standardGeo = QRect(10,self.pos,320,self.thought_len+40)
        
        if myGeo == standardGeo:
            geoExtended = maxGeo
        else:
            geoExtended = standardGeo
        self.animation = QPropertyAnimation(self,b"geometry")
        self.animation.setDuration(400)
        self.animation.setStartValue(myGeo)
        self.animation.setEndValue(geoExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()        
    
    def modifyBox(self,_thought):
        conn = sqlite3.connect("Opinion.db") 
        cur = conn.cursor()
        cur.execute("UPDATE Box SET thought = '{}' WHERE thought = '{}';".format(self.thought.toPlainText(),_thought))
        conn.commit()
        conn.close()
        msg = QMessageBox()
        msg.setWindowTitle("Modify")
        msg.setText("Successfully Modify")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)

        x = msg.exec_()
    def deleteBox(self,_thought):
        conn = sqlite3.connect("Opinion.db") 
        cur = conn.cursor()
        cur.execute("DELETE FROM Box WHERE thought = '{}';".format(_thought))
        conn.commit()
        conn.close()
        msg = QMessageBox()
        msg.setWindowTitle("Delete")
        msg.setText("Successfully Delete")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)

        x = msg.exec_()
    
        


class news(QMainWindow) : 
    def __init__(self,_news):
        QMainWindow.__init__(self)
        
        self.btn = QPushButton("확대하기")
        self.layout = QHBoxLayout()
        self.Innerlayout = QGridLayout()
        self.groupbox = QGroupBox("news")
        self.textedit = QTextEdit()
        self.textedit.setText(_news)
        self.textedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        
        
        self.layout.addWidget(self.groupbox)
        self.groupbox.setLayout(self.Innerlayout)
        self.Innerlayout.addWidget(self.textedit)
        self.Innerlayout.addWidget(self.btn)   #btn을 이쁘게 넣고싶은데

        self.btn.clicked.connect(lambda: self.openSubwindow())

    def openSubwindow(self):
        self.mySub = subwindow(self.textedit.toPlainText())

class subwindow(MainWindow):
    def __init__(self,_text):
        QMainWindow.__init__(self)
        
        self.ui = Ui_otherWindow()
        self.ui.setupUi(self)


        self.ui.news.setText(str(_text))
        self.ui.pushButton_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.actionExit.triggered.connect(lambda: self.deleteLater())
        self.ui.savebtn.clicked.connect(self.save)
        self.ui.savebtn.clicked.connect(self.show_popup)

        self.show()

    def save(self):
        conn = sqlite3.connect("Opinion.db") 
        cur = conn.cursor()
        cur.execute("INSERT INTO Box VALUES(?,?)",[self.ui.news.toPlainText(),self.ui.mine.toPlainText()])        
        conn.commit()
        conn.close()
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Save")
        msg.setText("Successfully Save")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)

        x = msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # splash screen
    lbl = QLabel('<font color=Green size=48><b> Web Crawling... </b></font>')
    lbl.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    lbl.show()

    while True:
        if flag[0]*flag[1]*flag[2] == 1 :
            break
        time.sleep(1)

    # 저장된 뉴스데이터 가져오기
    # path = "C:\\Users\\문희찬\\Desktop\\scraping\\{}".format(datetime.today().strftime("%Y-%m-%d"))
    # file_list = os.listdir(path)
    # lst = []

    # for i in range(0,len(file_list)):
    #     filepath = os.path.join(path, file_list[i])
    #     fid = open(filepath, "r",encoding="utf8")
    #     todayNews = fid.read()
    #     lst.append(todayNews)
      
    window = MainWindow(threading_lst)
    sys.exit(app.exec_())


