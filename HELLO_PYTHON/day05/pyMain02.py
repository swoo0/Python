import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


form_class = uic.loadUiType("pyMain02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count = 1
        
        self.btn.clicked.connect(self.pbClick)

    def pbClick(self):
        a = self.lbl.text()
        aa = int(a)
        aa += 1
        self.lbl.setText(str(aa))

        # self.count += 1
        # self.lbl.setText(self.count)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    