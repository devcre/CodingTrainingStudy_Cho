import math
from itertools import permutations

def solution(numbers):
    answer = 0
    
    def isPrime(num):
        if num == 1 or num == 0:
            return False
        
        ct = 2
        while ct <= math.sqrt(num):
            if num % ct == 0:
                return False
            ct += 1
            
        return True
    
    l = list(numbers)
    coml = []
    
    ct = 0
    length = 1
    while length <= len(l):
        newlist = list(permutations(l,length))
        for y in newlist:
            inty = ''.join(list(y))
            if int(inty) not in coml:
                coml.append(int(inty))
        length += 1
    
    for s in coml:
        if isPrime(s) == True:
            answer += 1
        
    return answer