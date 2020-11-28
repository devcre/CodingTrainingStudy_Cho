from itertools import combinations

def solution(number, k):
    answer = ''
    numlist = list(number)
    n = []
    _max = 0
    
    def removek(_list, k):
        _newlist = _list[:]
        for i in range(0,len(k)):
            del _newlist[k[i]-i]
        return ''.join(_newlist)
    
    for x in range(0,len(number)):
        n.append(x)
    
    nNumr = list(combinations(n, k))
    
    _max = removek(numlist, nNumr[0])
    for i in range(1, len(nNumr)):
        p = removek(numlist, list(nNumr[i]))
        if int(p) > int(_max):
            _max = p
    
    
    answer = _max
    return answer