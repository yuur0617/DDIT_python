import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

form_class = uic.loadUiType("myqt07.ui")[0]

class myWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def getStar(self, cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret

    def myclick(self):
        fs = self.sb_first.value()
        ls = self.sb_last.value()
        
        txt = ""
        
        # for i in range(fs, ls+1):
        #     for i in range(0, fs):
        #         txt +="*"
        #     fs += 1
        #     txt += "\n"
        # self.te.setText(txt)
        
        for i in range(fs, ls+1):
            txt += self.getStar(i)
        
        self.te.setText(txt)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
