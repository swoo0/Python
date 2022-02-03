import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random
from PyQt5.Qt import Qt

form_class = uic.loadUiType("pyMain04.UI")[0]

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
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else :
            com = "보"    
        
        if mine == com : result = "무승부!"
        if mine == "가위" and com == "보" : result = "승리!"
        if mine == "가위" and com == "바위" : result = "패배!"
        if mine == "바위" and com == "가위" : result = "승리!"
        if mine == "바위" and com == "보" : result = "패배!"
        if mine == "보" and com == "바위" : result = "승리!"
        if mine == "보" and com == "가위" : result = "패배!"
        
        
        self.leCom.setText(com)
        self.leResult.setText(result)
        
    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Return :
    #         self.btnClick()
        
if __name__ pbClickin__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    