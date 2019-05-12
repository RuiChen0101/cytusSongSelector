from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_picWindow(object):
    def setupUi(self, picWindow):
        picWindow.setObjectName("picWindow")
        picWindow.resize(1280, 720)
        self.pic = QtWidgets.QLabel(picWindow)
        self.pic.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("./img/超級聯賽3(720p).jpg"))
        self.pic.setObjectName("pic")

        self.retranslateUi(picWindow)
        QtCore.QMetaObject.connectSlotsByName(picWindow)

    def retranslateUi(self, picWindow):
        _translate = QtCore.QCoreApplication.translate
        picWindow.setWindowTitle(_translate("picWindow", "曲圖畫面"))
