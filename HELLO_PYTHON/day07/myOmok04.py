import sys

from PyQt5 import uic
from PyQt5.Qt import QIcon, QPushButton, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

form_class = uic.loadUiType("myOmok04.UI")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cnt = 0
        self.flagWb = True
        self.flagEnd = False
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],

            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],

            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],

            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
        ]
        self.pb2D = []
        
        for i in range(19):
            line = []
            for j in range(19):
                pb_one = QPushButton(self)
                pb_one.setText('')
                pb_one.setIcon(QIcon('0.png'))
                pb_one.setIconSize(QSize(40,40))
                pb_one.setGeometry(10+(40*j), 10+(i*40), 40, 40)
                pb_one.clicked.connect(self.myClick)
                pb_one.setToolTip('{},{}'.format(i, j))
                line.append(pb_one)
            self.pb2D.append(line)
            
        self.pb.clicked.connect(self.myReset)
        self.myRander()
        
    
    def myReset(self):
        for i in range(19):
            for j in range(19):
                self.arr2D[i][j] = 0
        self.myRander()
        self.flagEnd = False
        self.flagWb = True

        
    def myRander(self):    
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QIcon('2.png'))
        
        
    def myClick(self):
        
        if self.flagEnd:
            return
        
        btn = self.sender()
        ij = btn.toolTip().split(",")
        i = int(ij[0])
        j = int(ij[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        if self.flagWb == True:
            self.arr2D[i][j] = 1
            stone = 1
        elif self.flagWb == False:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.checkUP(i, j, stone)
        dw = self.checkDW(i, j, stone)
        
        le = self.checkLE(i, j, stone)
        ri = self.checkRI(i, j, stone)
        
        ul = self.checkUL(i, j, stone)
        dr = self.checkDR(i, j, stone)
            
        ur = self.checkUR(i, j, stone)
        dl = self.checkDL(i, j, stone)
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = ul + dr + 1  
        d4 = ur + dl + 1    
        
        self.myRander()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            if self.flagWb :
                QMessageBox.information(self,'Omok','백돌 승리 !')
            else :
                QMessageBox.information(self,'Omok','흑돌 승리 !')
            self.flagEnd = True
    
        self.flagWb = not self.flagWb
    
    
    def checkUP(self, i, j, stone):    
        cnt = 0;
        try :
            while True:
                i -= 1
                if i < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
    
    def checkDW(self, i, j, stone):    
        cnt = 0;
        try :
            while True:
                i += 1
                if i < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt 
     
    
    def checkLE(self, i, j, stone):
        cnt = 0;
        try :
            while True:
                j -= 1
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
    
    def checkRI(self, i, j, stone):
        cnt = 0;
        try :
            while True:
                j += 1
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt 
     
     

    def checkDR(self, i, j, stone):
        cnt = 0;
        try :
            while True:
                i += 1
                j += 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
        
    def checkUL(self, i, j, stone):
        cnt = 0;
        try :
            while True:
                i -= 1
                j -= 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
        
    
    def checkUR(self, i, j, stone):
        cnt = 0;
        try :
            while True:
                i -= 1
                j += 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
        
    def checkDL(self, i, j, stone):
        cnt = 0;
        try :
            while True:
                i += 1
                j -= 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
     
     



     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    