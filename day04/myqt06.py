import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import random

form_class = uic.loadUiType("myqt06.ui")[0]

class myWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        
        ran = random()
        if(ran > 0.5):
            com = "홀"
        else :
            com = "짝"
            
        if(com == mine):
            result = "승리"
        else :
            result = "패배"
            
        self.le_com.setText(com)
        self.le_result.setText(result);

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
