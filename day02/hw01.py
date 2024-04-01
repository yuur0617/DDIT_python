#===============================================================================
# 가위바위보를 선택하세요. 가위
# 나 : 가위
# 컴 : 보
# 결과 : 승리
#===============================================================================
from random import random

mine = input("가위 바위 보 를 입력하세요 ")

com =""
result =""
rnd = random()*3 #0일떄 가위, 1일떄 바위, 2일떄 보

intRnd = int(rnd)

if(intRnd == 0):
    com = "가위"
    if(mine == "바위"):
        result = "승리"
    elif(mine == "보"):
        result ="패배"
elif(intRnd == 1):
    com = "바위"
    if(mine == "가위"):
        result = "패배"
    elif(mine == "보"):
        result ="승리"
elif(intRnd == 2):
    com = "보"
    if(mine == "가위"):
        result = "승리"
    elif(mine == "바위"):
        result ="패배"

if(com == mine):
    result="무승부"

print("나 : " + mine)
print("컴 : " + com)
print("결과 : "+ result)


