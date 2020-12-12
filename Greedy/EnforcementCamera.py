from itertools import combinations

def solution(routes):
    answer = 0
    _sorted = routes[:]
    # _sorted = []
    # for i in range(0, len(routes)):
    #     if routes[i][0] > routes[i][1]:
    #         _sorted.append([routes[i][1], routes[i][0]])
    #     else:
    #         _sorted.append(routes[i])
    
    # x: [-20, 15], y: [-14, -5]
    def findCommon(x, y):
        if x[0] <= y[0]:
            if x[1] < y[0]:
                return 0
            elif y[0] <= x[1] and x[1] <= y[1]:
                return [y[0], x[1]]
            else:
                return [y[0], y[1]]
        else:
            if y[1] < x[0]:
                return 0
            elif x[0] <= y[1] and y[1] <= x[1]:
                return [x[0], y[1]]
            else:
                return [x[0], x[1]]
    
    
    ptr = 0
    # comb = [([-20,15], [-14,-15]), ([-20,15], [-18,-13]), ...]
    comb = list(combinations(_sorted, 2))
    count = len(comb)
    while count != 0:
        e = findCommon(comb[ptr][0], comb[ptr][1])
        if e == 0:
            ptr += 1
            count -= 1
        else:
            _sorted.remove(comb[ptr][0])
            _sorted.remove(comb[ptr][1])
            _sorted.append(e)
            comb = list(combinations(_sorted, 2))
            count = len(comb)
            ptr = 0

    answer = len(_sorted)

    return answer