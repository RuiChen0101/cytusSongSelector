import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore , QtGui
from src.ui.controlPenalUI import Ui_controlPenal
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


class controlPenal(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_controlPenal()
        self.ui.setupUi(self)
        self.ui.loadRound8.clicked.connect(self.setRound8)
        self.ui.loadRound4.clicked.connect(self.setRound4)
        self.ui.loadRoundFinal.clicked.connect(self.setRoundFinal)
        self.picW= picWindow()
        self.picW.show()
        self.list=[]
        self.show()

    def closeEvent(self, event):
        self.__del__()

    def __del__(self):
        self.picW.close()

    def setRound8(self):
        self.list=[]
        f=open("round8.txt","r")
        for line in f.readlines():
            self.list.append(line)
        self.setTable()

    def setRound4(self):
        self.list=[]
        f=open("round4.txt","r")
        for line in f.readlines():
            self.list.append(line)
        self.setTable()

    def setRoundFinal(self):
        self.list=[]
        f=open("roundfinal.txt","r")
        for line in f.readlines():
            self.list.append(line)
        self.setTable()

    def setTable(self):
        self.ui.songList.setRowCount(0)
        for row_number,content in enumerate(self.list):
            self.ui.songList.insertRow(row_number)
            self.ui.songList.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(content)))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = controlPenal()
    w.show()
    sys.exit(app.exec_())
