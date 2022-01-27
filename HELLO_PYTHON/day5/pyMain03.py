import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


form_class = uic.loadUiType("pyMain03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btn.clicked.connect(self.btnClick)

    def btnClick(self):
        a = self.li1.text()
        b = self.li2.text()
        aa = int(a)
        bb = int(b)
        self.li3.setText(str(aa - bb))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    