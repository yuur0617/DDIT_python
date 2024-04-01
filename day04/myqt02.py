import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

form_class = uic.loadUiType("myqt02.ui")[0]

class myWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        # txt = self.le.text()
        # dob = str(int(txt) * 2)
        # self.le.setText(dob)
        # print(dob)
        a = self.le.text()
        ia = int(a)
        ia = ia*2
        self.le.setText(str(ia))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
