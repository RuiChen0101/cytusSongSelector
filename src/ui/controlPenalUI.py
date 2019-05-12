# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/mainui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_controlPenal(object):
    def setupUi(self, controlPenal):
        controlPenal.setObjectName("controlPenal")
        controlPenal.resize(415, 412)
        self.loadRound8 = QtWidgets.QPushButton(controlPenal)
        self.loadRound8.setGeometry(QtCore.QRect(20, 42, 91, 41))
        self.loadRound8.setObjectName("loadRound8")
        self.loadRoundFinal = QtWidgets.QPushButton(controlPenal)
        self.loadRoundFinal.setGeometry(QtCore.QRect(20, 140, 91, 41))
        self.loadRoundFinal.setObjectName("loadRoundFinal")
        self.loadRound4 = QtWidgets.QPushButton(controlPenal)
        self.loadRound4.setGeometry(QtCore.QRect(20, 90, 91, 41))
        self.loadRound4.setObjectName("loadRound4")
        self.result = QtWidgets.QLabel(controlPenal)
        self.result.setGeometry(QtCore.QRect(140, 360, 251, 31))
        self.result.setObjectName("result")
        self.songList = QtWidgets.QTableWidget(controlPenal)
        self.songList.setGeometry(QtCore.QRect(140, 0, 256, 361))
        self.songList.setObjectName("songList")
        self.songList.setColumnCount(1)
        self.songList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.songList.setHorizontalHeaderItem(0, item)
        self.startPick = QtWidgets.QPushButton(controlPenal)
        self.startPick.setGeometry(QtCore.QRect(20, 190, 91, 41))
        self.startPick.setObjectName("startPick")
        self.stopMusic = QtWidgets.QPushButton(controlPenal)
        self.stopMusic.setGeometry(QtCore.QRect(20, 240, 91, 41))
        self.stopMusic.setObjectName("stopMusic")
        self.clearTxt = QtWidgets.QPushButton(controlPenal)
        self.clearTxt.setGeometry(QtCore.QRect(20, 290, 91, 41))
        self.clearTxt.setObjectName("clearTxt")

        self.retranslateUi(controlPenal)
        QtCore.QMetaObject.connectSlotsByName(controlPenal)

    def retranslateUi(self, controlPenal):
        _translate = QtCore.QCoreApplication.translate
        controlPenal.setWindowTitle(_translate("controlPenal", "控制台"))
        self.loadRound8.setText(_translate("controlPenal", "8強"))
        self.loadRoundFinal.setText(_translate("controlPenal", "冠亞"))
        self.loadRound4.setText(_translate("controlPenal", "4強"))
        self.result.setText(_translate("controlPenal", "<html><head/><body><p><span style=\" font-size:14pt;\">test</span></p></body></html>"))
        item = self.songList.horizontalHeaderItem(0)
        item.setText(_translate("controlPenal", "song"))
        self.startPick.setText(_translate("controlPenal", "startPick"))
        self.stopMusic.setText(_translate("controlPenal", "stopMusic"))
        self.clearTxt.setText(_translate("controlPenal", "clearTxt"))

