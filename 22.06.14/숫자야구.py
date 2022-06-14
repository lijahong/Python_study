#3번 문제 : 숫자 야구 게임 : 1 ~ 9 랜덤한 숫자 3개를 중복이 되지 않게 생성 및 리스트에 저장하여,
# 숫자와 자리에 따라 스트라이크, 볼, 아웃의 갯수를 출력하시오. 스트라이크가 3개면 게임 종료
from random import *

lst =[]
while(1): #정답 랜덤 생성
    if (len(lst) == 3):
        break
    i = randint(1,10)
    idx = 0;
    for j in range(0,len(lst)):
        if(i == lst[j]):
            idx = 1
    if(idx == 0):
        lst.append(i)
    elif(idx == 1) :
        j = 0
count = 0;
print(lst)
while(1):
    lst_user = []
    strike = 0
    ball = 0
    out = 0
    #사용자 3가지 입력
    num1, num2, num3 = map(int,input("3가지 수를 중복 없이 입력하세요 : ").split())
    lst_user.append(num1)
    lst_user.append(num2)
    lst_user.append(num3)
    #비교 구문
    for i in range(0,3):
        for j in range(0,3):
                if( lst_user[i]==lst[j] and i == j ):
                    strike += 1
                elif( lst_user[i]==lst[j]  and  i != j ):
                    ball += 1
    out = 3 - strike - ball


    print("strike : %d, ball : %d, out : %d" %(strike, ball, out))
    count += 1
    if(strike == 3):
        print("시도횟수 : %d"%count)
        break

