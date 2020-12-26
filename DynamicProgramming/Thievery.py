def solution(money):
    answer = 0
    
    houses = len(money)
    
    while houses > 0:
        _max = 0
        t = 0
        for i in range(len(money)):
            if i+1 == len(money):
                if _max < money[i] and money[i] >= money[i-1] + money[0]:
                    _max = money[i]
                    t = i
            else:
                if _max < money[i] and money[i] >= money[i-1] + money[i+1]:
                    _max = money[i]
                    t = i
        if t+1 == len(money):
            money[t-1] = 0
            money[t] = 0
            money[0] = 0
            houses -= 3
        else:
            money[t-1] = 0
            money[t] = 0
            money[t+1] = 0
            houses -= 3
        answer += _max
            
    return answer