import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random
from PyQt5.Qt import Qt

form_class = uic.loadUiType("pyMain04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btn.clicked.connect(self.pbClick)
        self.leMine.returnPressed.connect(self.pbClick)

    def pbClick(self):
        mine = self.leMine.text()
        com = ""
        result = ""
        
        rnd = random.random()
        if rnd > 0.5:
            com = "홀"
        else :
            com = "짝"
        
        if mine == com:
            result = "승리!"
        else :
            result = "패배!"
        
        self.leCom.setText(com)
        self.leResult.setText(result)
        
    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Return :
    #         self.btnClipbClick      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    