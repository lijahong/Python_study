#프로그레머스 Lv.1 ) 크레인 인형뽑기 게임
#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    lst = [] 
   
    for i in moves:
        for j in range(0,len(board)):
            if board[j][i-1] != 0: #인형이 있다면
                tdx = board[j][i-1] 
                lst.append(tdx)
                board[j][i-1] = 0
                break #인형을 집었으니 다음 순서로
                
        num = len(lst)
        if(num>=2): #인형이 2개 이상 있을 시 중복 검사
            if(lst[num-1]==lst[num-2]):
                lst.pop(num-1)
                lst.pop(num-2)
                answer += 2
                            
    return answer
