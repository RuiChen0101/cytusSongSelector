import time, sys, random
from pygame import mixer
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore
from src.ui.controlPenalUI import Ui_controlPenal
from src.songScreen import picWindow

class controlPenal(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_controlPenal()
        self.ui.setupUi(self)
        self.ui.loadRound8.clicked.connect(self.setRound8)
        self.ui.loadRound4.clicked.connect(self.setRound4)
        self.ui.loadRoundFinal.clicked.connect(self.setRoundFinal)
        self.ui.startPick.clicked.connect(self.startPick)
        self.ui.clearTxt.clicked.connect(self.clearTxt)
        self.ui.removeFromList.clicked.connect(self.removeFromList)
        self.picW=picWindow()
        self.picW.show()
        self.pic=0
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
            self.list.append(line.rstrip())
        self.setTable()

    def setRound4(self):
        self.list=[]
        f=open("round4.txt","r")
        for line in f.readlines():
            self.list.append(line.rstrip())
        self.setTable()

    def setRoundFinal(self):
        self.list=[]
        f=open("roundfinal.txt","r")
        for line in f.readlines():
            self.list.append(line.rstrip())
        self.setTable()

    def setTable(self):
        self.ui.songList.setRowCount(0)
        for row_number,content in enumerate(self.list):
            self.ui.songList.insertRow(row_number)
            self.ui.songList.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(content)))

    def startPick(self):
        mixer.init()
        mixer.music.load("./song/opener.mp3")
        mixer.music.play()
        for i in range(0,62,2):
            self.callRandomPic()
            self.picW.updatePic(self.list[self.pic])
            QApplication.processEvents()
            print(self.list[self.pic])
            time.sleep(0.01*i)
        sound=mixer.Sound("./song/"+self.list[self.pic]+".wav")
        time.sleep(2)
        mixer.music.stop()
        self.ui.result.setText(self.list[self.pic])
        QApplication.processEvents()
        sound.play()
        f=open("result.txt","w")
        f.write(self.list[self.pic])
        f.close()
        time.sleep(sound.get_length())

    def callRandomPic(self):
        rand=random.randint(0,len(self.list)-1)
        while rand==self.pic:
            rand=random.randint(0,len(self.list)-1)
        self.pic=rand

    def clearTxt(self):
        self.picW.clearPic()
        self.ui.result.setText("")
        f=open("result.txt","w")
        f.write("")
        f.close()

    def removeFromList(self):
        pos=self.ui.songList.currentRow()
        del self.list[pos]
        self.setTable()
