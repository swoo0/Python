import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.Qt import QIcon

form_class = uic.loadUiType("myOmok01.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cnt = 0
        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        self.cnt += 1
        self.pb.setIcon(QIcon('{}.png'.format(self.cnt%3)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()