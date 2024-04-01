import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from attr import ib

form_class = uic.loadUiType("myqt03.ui")[0]

class myWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        # a = self.le1.text()
        # b = self.le2.text()
        # result = str(int(a) - int(b))
        #
        # self.le3.setText(result)
        
        a = self.le1.text()
        b = self.le2.text()
        ia = int(a)
        ib = int(b)
        min = ia - ib
        
        self.le3.setText(str(min))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
