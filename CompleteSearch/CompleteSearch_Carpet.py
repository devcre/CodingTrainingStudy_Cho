from itertools import permutations

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    divisors = []
    k = 1
    while k <= total:
        if total%k == 0:
            divisors.append(k)
        k += 1
        
    l = len(divisors)
    comb = []
    i = 0
    
    while i < l/2:
        comb.append([divisors[i], divisors[l-1-i]])
        i += 1
    if l % 2 != 0:
        comb.append([divisors[l//2+1], divisors[l//2+1]])
        
    for s in comb:
        if (s[0]-2) * (s[1]-2) == yellow:
            answer.append(s[0])
            answer.append(s[1])
    
    if answer[0] < answer[1]:
        t = answer[0]
        answer[0] = answer[1]
        answer[1] = t
        
    return answer