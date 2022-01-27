import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random
from PyQt5.Qt import Qt

form_class = uic.loadUiType("pyMain05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btn.clicked.connect(self.btnClick)
        
    def btnClick(self):
        arr45 = [
            1,2,3,4,5,       6,7,8,9,10,
            11,12,13,14,15,  16,17,18,19,20,
            21,22,23,24,25,  26,27,28,29,30,
            31,32,33,34,35,  36,37,38,39,40,
            41,42,43,44,45
        ]
        
        arr6 = []
        
        while len(arr6) < 6 :
            rnd = int(random.random() * 45)
            if arr45[rnd] > 0 :
                arr6.append(arr45[rnd])
                arr45[rnd] = -1
            else :
                continue
        
        for i in range(len(arr6)) :
            for j in range(i, len(arr6)) :
                if arr6[i] > arr6[j] :
                    temp = arr6[i]
                    arr6[i] = arr6[j]
                    arr6[j] = temp
        
        self.le1.setText(str(arr6[0]))
        self.le2.setText(str(arr6[1]))
        self.le3.setText(str(arr6[2]))
        self.le4.setText(str(arr6[3]))
        self.le5.setText(str(arr6[4]))
        self.le6.setText(str(arr6[5]))
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return :
            self.btnClick()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    