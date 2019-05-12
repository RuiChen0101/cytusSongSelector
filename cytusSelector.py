import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore , QtGui
from src.controlPenal import controlPenal

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = controlPenal()
    w.show()
    sys.exit(app.exec_())
