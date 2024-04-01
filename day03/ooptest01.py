class Animal:  
    def __init__(self):
        self.name = ""
        print("생성자")
        
    def named(self, name):
        self.name = name
     
    def __str__(self):
        return "[Animal][name] : " + self.name
        
    def __del__(self):
        print("소멸자")
        
class Human(Animal) :
    def __init__(self):
        super().__init__() 
        self.asset = 0;
        
    def goldspoon(self):
        self.asset = 100000000000

if __name__ == '__main__':
    # ani = Animal()
    # print(ani)
    # ani.named("멍멍이")
    # print(ani)
    
    hum = Human()
    print(hum.name)
    print(hum.asset)
    
    hum.named("전청조")
    hum.goldspoon()
    
    print(hum.name)
    print(hum.asset)
