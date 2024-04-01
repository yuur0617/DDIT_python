import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("myqt08.ui")[0]

class myWindow(QMainWindow, form_class):
        
    # global rnd
    def __init__(self):
        super().__init__()
        self.com = 0
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        self.setCom()

    def setCom(self):
        # global rnd
        # rnd = int(random()*99)+1
        self.com = int(random()*99)+1
        print("self.com",self.com)
        
    
    def myclick(self):
        # print(rnd)
        #
        # mine = self.le.text()
        # imine = int(mine)
        # print(imine)
        #
        # str_new=""
        #
        # if(rnd == imine):
        #     str_new = mine + " ANSWER \n"
        #     QMessageBox.about(self,'ANSWER',mine+' 정답입니다.')
        # elif(rnd > imine):
        #     str_new = mine + " UP \n"
        #
        # elif(rnd < imine):
        #     str_new = mine + " DOWN \n"
        #
        # str_old = self.pte.toPlainText()
        #
        # str = str_old + str_new
        #
        # self.pte.setPlainText(str)
        #
        # self.le.setText("")
        
        mine = self.le.text()
        imine = int(mine)
        
        str_new = ""
        
        if self.com>imine :
            str_new = mine +" UP\n"
        elif self.com<imine :
            str_new = mine +" DOWN\n"
        else :
            str_new = mine +" ANSWER\n"
            QMessageBox.about(self,'ANSWER',mine +" 정답입니다.")
            
        str_old =  self.pte.toPlainText()
        
        self.pte.setPlainText(str_old+str_new)
        self.le.setText("")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
