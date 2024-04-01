#===============================================================================
# java파일을 참고하여 
# xi, putin class 만들기
#===============================================================================
class Xi :
    def __init__(self):
        self.money = 1000
        
    def spand(self, cost):
        self.money -= cost
        
class Putin:
    def __init__(self):
        self.cnt_nuclear = 100000
        
    def war(self):
        self.cnt_nuclear -= 1
        
class Minkyu(Xi, Putin) :
    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
    
if __name__ == '__main__':
    mk = Minkyu()
    print(mk.money)
    print(mk.cnt_nuclear)
    mk.spand(5)
    mk.war()
    print(mk.money)
    print(mk.cnt_nuclear)