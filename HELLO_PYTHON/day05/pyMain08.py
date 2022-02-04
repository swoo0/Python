import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("pyMain08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.pbClick)
        
    def drawStar(self, cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret


    def pbClick(self):
        a = self.lbs.Text()
        b = self.lbl.Text()
        aa = int(a)
        bb = int(b)
        txt = ""
        
        for i in range(aa,bb+1) :
            txt += self.drawStar(i)
        
        self.te.setText(txt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    