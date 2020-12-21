################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from main import *

class UIFunctions(MainWindow):

    def SavetoggleMenu(self, enable):
        if enable:

            # GET WIDTH
            myGeo = self.ui.frame_3.geometry()
            
            maxGeo = QRect(11,11,541,681)
            
            standardGeo = QRect(11,11,541,340)
            
            # SET MAX WIDTH
            if myGeo == standardGeo:
                geoExtended = maxGeo
            else:
                geoExtended = standardGeo
               
            # ANIMATION
            # QPropertyAnimation은 PySide2에서 제공하는 함수인듯?
            self.animation = QPropertyAnimation(self.ui.frame_3, b"geometry")
            self.animation.setDuration(400)
            self.animation.setStartValue(myGeo)
            self.animation.setEndValue(geoExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            # QPropertyAnimation은 PySide2에서 제공하는 함수인듯?
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()