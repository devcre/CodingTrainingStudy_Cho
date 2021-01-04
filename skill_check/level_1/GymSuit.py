def solution(n, lost, reserve):
    answer = 0
    
    c = 0
    while len(lost) > c:
        if lost[c] in reserve:
            reserve.remove(lost[c])
            lost.remove(lost[c])
        else:
            c += 1
    
    t = 0
    while len(lost) > t:
        if lost[t] - 1 in reserve:
            reserve.remove(lost[t]-1)
            lost.remove(lost[t])
        elif lost[t] + 1 in reserve:
            reserve.remove(lost[t]+1)
            lost.remove(lost[t])
        else:
            t += 1
    
    answer = n - len(lost)
    
    return answer