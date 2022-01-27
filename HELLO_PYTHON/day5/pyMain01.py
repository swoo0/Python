import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


form_class = uic.loadUiType("pyMain01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count = 1
        
        self.btn.clicked.connect(self.btnClick)

    def btnClick(self):
        if self.count % 2 == 0:
            self.lbl.setText("Good Moning")
            self.count += 1
        
        else:
            self.lbl.setText("Good Evening")
            self.count -= 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    