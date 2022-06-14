#프로그래머스 Lv.3 ) 추석 트래픽
#https://programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines):
    time_list = []
    for str in lines:  # 모든 수를 초단위로 변환하여 시작과 끝을 2차원 리스트에 저장
        st_sec, end_sec = str_slice(str) 
        time_list.append([st_sec, end_sec])
    answer = compareabout(time_list) # 비교 연산 실시
    return answer


def str_slice(line):  # 문자열을 받아 초단위로 계산 한 값 반환
    end_time = line[11:23]  # 종료 시간
    get_sec = line[24:-1]  # 걸린 시간
    end_sec = float(end_time[0:2]) * 3600 + float(end_time[3:5]) * 60 + float(end_time[6:]) # 초단위로 변환
    start_sec = end_sec - float(get_sec) + 0.001 #시작 시간은 걸린시간 -0.001
    return start_sec, end_sec


def compareabout(lst):  # 비교 연산
    maxi = 0
    lst_count = []
    for index in lst: #로그의 범위 기준을 각 로그데이터 시작과 끝으로 하기 위해 1차원 배열로 변환
        lst_count.append(index[0])
        lst_count.append(index[1])

    for i in lst_count:
        count = 0
        start_time = i #로그 시작
        end_time = round(i + 0.999,3) #구간이 1초가 아닌 0.999초 기준, 1을 더해주면 그 값은 포함하면 안되기에
        print(start_time, end_time)
        for j in lst: #해당 범위에서 로그 시간들 비교
            tmp_start = j[0]
            tmp_end = j[1]
            print(tmp_start, tmp_end)
            if(tmp_start > end_time or start_time > tmp_end): #이 범위에 해당 안되면 카운트 증가
                count += 1

        count = len(lst)-count #범위에 다 겹칠 확률 - 해당 안되는 확률
        print(count)
        if(maxi < count):
            maxi = count


    return maxi
