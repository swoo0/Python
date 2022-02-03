import sys

from PyQt5 import uic
from PyQt5.Qt import QIcon, QPushButton, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("myOmok02.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cnt = 0
        
        for j in range(10):
            for i in range(10):
                btn = QPushButton(self)
                btn.setText('')
                btn.setIcon(QIcon('0.png'))
                btn.setIconSize(QSize(40,40))
                btn.setGeometry(10+(40*i), 10+(j*40), 40, 40)
                btn.clicked.connect(self.myClick)
        
    def myClick(self):
        self.cnt += 1
        btn = self.sender()
        btn.setIcon(QIcon('{}.png'.format(self.cnt % 3)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()