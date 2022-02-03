import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic


form_class = uic.loadUiType("pyMain09.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.pbClick)
        self.pb2.clicked.connect(self.pbClick)
        self.pb3.clicked.connect(self.pbClick)
        self.pb4.clicked.connect(self.pbClick)
        self.pb5.clicked.connect(self.pbClick)
        self.pb6.clicked.connect(self.pbClick)
        self.pb7.clicked.connect(self.pbClick)
        self.pb8.clicked.connect(self.pbClick)
        self.pb9.clicked.connect(self.pbClick)
        self.pb0.clicked.connect(self.pbClick)
        self.pbCall.clicked.connect(self.callClick)
                
    def pbClick(self):
        oldNum = self.le.text()
        btn = self.sender()
        newNum = btn.text()
        self.le.setText(oldNum + newNum)

    def callClick(self):
        callNum = self.le.text() 
        QMessageBox.information(self, "calling...", callNum + "\n연결중...", QMessageBox.Yes, QMessageBox.Cancel)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    