def solution(x):
    answer = True
    strx = str(x)
    
    sum = 0
    for i in range(0, len(strx)):
        sum += int(strx[i])
        
    if int(x) % sum == 0 :
        answer = True
    else:
        answer = False
    return answer