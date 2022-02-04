import sys
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import time


form_class = uic.loadUiType("pyMain10.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbClick)

    def myRun(self):
        for i in range(9) :
            a = self.lbl.text()
            aa = int(a)
            aa += 1
            time.sleep(1)
            self.lbl.setText(str(aa))

    def pbClick(self):
        threading.Thread(target=self.myRun).start()
        

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()