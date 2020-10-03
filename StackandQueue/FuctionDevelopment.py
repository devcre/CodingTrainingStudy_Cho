import math

def solution(progresses, speeds):
    answer = []
    disDay = []
    
    c = 0
    # 배포에 필요한 일수 리스트 만들기
    while c < len(progresses):
        x = math.ceil((100-progresses[c])/speeds[c])
        disDay.append(x)
        c += 1
    
    dis = 1
    count = 0
    ptr = disDay[0]
    # 몇 개의 기능이 배포되는지 
    while count < len(disDay):
        if count+1 == len(disDay):
            answer.append(dis)
        elif ptr < disDay[count+1]:
            answer.append(dis)
            ptr = disDay[count+1]
            dis = 1
        else:
            dis += 1
        count += 1
        
        
    return answer