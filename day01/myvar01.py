a = 1
b = 1.1
c = '6'
d = True
e = False

print (a+b)  #2.1
# print (a+c)  #'int' + 'str' 할수없음.
print (str(a)+c) #16
print (a+int(c)) #7
print (not d) #False
print(d and e) #False
print(d or e) #True