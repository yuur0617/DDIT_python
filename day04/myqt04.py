import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

form_class = uic.loadUiType("myqt04.ui")[0]

class myWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        dan = self.te.toPlainText()
        idan = int(dan)
        
        txt = ""
        
        rng = range(1,9+1)
        
        for i in rng :
            # txt += str(idan)+" * "+str(i)+" = " +str(idan * i)+"\n"
            txt += ("{} * {} = {} \n".format(idan, i, idan*i))
            self.pte.setPlainText(txt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWindow()
    myWindow.show()
    app.exec_()
    
