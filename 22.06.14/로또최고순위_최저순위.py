#프로그래머스 lv.1) 로또의 최고 순위와 최저 순위 : 번호를 비교할때 알아볼 수 없는 번호를 0으로 입력하여,
#0이 정답일 가능성과 아닐 가능성을 비교해 최고 순위와 최저 순위를 출력하시오.

def solution(lottos, win_nums):
    count = 0
    zero_count = 0
    max_i = 0
    min_i = 0
    for i in range(0,6):
        for j in range(0,6):
            if(lottos[i] == 0):
                zero_count +=1
                break
            else:
                if(lottos[i] == win_nums[j]):
                    count += 1
                    break

    max_i = count + zero_count
    min_i = count
    max_i = 7 - max_i
    min_i = 7 - min_i
    if(max_i == 7): #min으로도 풀이 가능 min(6,7-max_i) 하면 작은 수가 나오므로 7이 나오지 않는다
        max_i = 6
    if(min_i == 7):
        min_i = 6
    answer = []
    answer.append(max_i)
    answer.append(min_i)
    
    return answer

#또 다른 풀이
"""
def solution(lottos, win_nums):
    num = [6,6,5,4,3,2,1]
    zero_count = lottos.count(0)
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    answer = []
    answer.append(num[zero_count+count])
    answer.append(num[count])    
    
    return answer
"""
