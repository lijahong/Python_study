#1번 문제. 업 앤 다운 : 1부터 50까지 랜덤한 숫자를 하나 생성하고,
#사용자한테 숫자를 입력받아 랜덤한 숫자보다 크면 다운, 작으면 업, 일치하면 정답을 출력하여, 정답이 나오면 종료하시오.

from random import *
num = randint(1,101)
while(1):
    i = int(input())
    if( i > num):
        print("down")
    elif( i < num):
        print("up")
    elif( i == num):
        print("correct")
        break
