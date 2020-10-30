def solution(n, times):
    answer = 0
    
    k = times[0]
    for x in times:
        if k > x:
            k = x
    
    t = 0
    while n != 0:
        t += k
        for x in times:
            if t % x == 0:
                n -= 1
    
    answer = t
        
    return answer