import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.Qt import Qt

form_class = uic.loadUiType("pyMain06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.pbClick)
        self.le.returnPressed.connect(self.pbClick)

    def pbClick(self):
        dan = self.le.text()
        idan = int(dan)
        gop = 10
        txt = "";

        txt += dan + "단" + "\n"
        for i in range(1, gop) :
            txt += str(idan) + " * " + str(i) + " = " + str(idan * i) + "\n"
            
        self.te.setText(txt)
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return :
            self.bpbClick)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    