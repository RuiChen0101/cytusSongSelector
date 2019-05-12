import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore , QtGui
from src.ui.songScreenUI import Ui_picWindow

class picWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_picWindow()
        self.ui.setupUi(self)
        self.show()

    def updatePic(self,fileName):
        self.ui.pic.setPixmap(QtGui.QPixmap("./img/songpool/"+fileName+".jpg"))

    def clearPic(self):
        self.ui.pic.setPixmap(QtGui.QPixmap("./img/超級聯賽3(720p).jpg"))
