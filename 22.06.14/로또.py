#2번문제 : 로또 번호 : 0~45까지 숫자를 중복이 되지 않게 6개를 생성하여 리스트에 저장

from random import *

lst =[]
while(1):
    if(len(lst)==6):
            break
    i = randint(1,45)
    idx = 0
    for j in range(0,len(lst)):
            if(i==lst[j]):
                idx = 1
    if(idx == 0) :
            lst.append(i)
print(lst)
