def solution(n, lost, reserve):
    n_reserve = reserve[:]
    for l in lost:
        if l in reserve:
            reserve.remove(l)
    
    for l in n_reserve:
        if l in lost:
            lost.remove(l)
    
    answer = n - len(lost)
    
    for x in reserve:
        if x-1 in lost:
            answer += 1
            lost.remove(x-1)
        elif x+1 in lost:
            answer += 1
            lost.remove(x+1)
    
    return answer