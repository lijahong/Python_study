#4번 문제 : 슷자를 여러개 입력받고, 가장 큰 수는 max에 저장하고, 
#입력 받은 수에 더 큰 수가 있다면 max의 값을 바꾼다

def find_max(lst):
    max = 0
    for i in lst:
        if( max < i):
            max = i
    return i

lst2 = map(int,input("숫자 입력 : ").split(" "))
num = find_max(lst2)
print(num)
