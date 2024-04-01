from random import random
def getHoolJJak():

    ran = random()
    if(ran > 0.5) :
        return "홀"
    else : 
        return "짝"

com = getHoolJJak()
print ("com : ", com)