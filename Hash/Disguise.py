from itertools import combinations
from functools import reduce

def solution(clothes):
    answer = 0
    
    kind = []
    for x in clothes:
        if x[1] not in kind:
            kind.append(x[1])
    
    # EXAMPLE
    # dic2 = {'headgear: 2', 'eyewear': 1}
    dic = {}
    for x in kind:
        dic[x] = 0
    
    # fill values into dic2
    for x in clothes:
        dic[x[1]] = dic[x[1]] + 1
    
    # EXAMPLE
    # _list = [2, 1]
    _list = list(dic.values())
    
    c = 0
    while len(kind) >= c:
        c += 1
        l = list(map(list, combinations(_list, c))) # EXAMPLE [[2], [1]]
        for e in l:
            answer += reduce(lambda x, y: x*y, e)
    
    return answer