#===============================================================================
# 홀/짝을 선택하시오. 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 승리
#===============================================================================
from random import random
mine = input("홀/짝을 선택하시오.")

com = ""
rnd = random()
result = ""

if(rnd >0.5):
    com = "홀"
else:
    com = "짝"
    
if(com == mine):
    result = "승리"
else:
    result = "패배"
    
print("나 : " + mine)
print("컴 : " + com)
print("결과 : " + result)

    
