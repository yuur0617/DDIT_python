#===============================================================================
# 숫자를 입력하세요 40
# 40 : up입니다.
# 숫자를 입력하세요 60
# 60 : Down입니다.
# 숫자를 입력하세요 50
# 정답입니다.
# -------------------------
# 10번이내로 정답을 입력해야함.
#===============================================================================
from random import random

rnd = (random()*99)+1 #1부터 99까지 랜덤수
intRnd = int(rnd)

for i in range(1, 10+1):
    
    mine = input("숫자를 입력하세요 ")
    intMine = int(mine)

    if(intRnd == intMine):
        print("정답입니다.") 
        break;
    elif(intRnd > intMine):
        print("UP 입니다.")
        continue;
    elif(intRnd < intMine):
        print("Down 입니다.")
        continue;
