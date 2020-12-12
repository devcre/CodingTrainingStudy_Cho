def solution(name):
    answer = 0
    
    dic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F":5,
           "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
           "M": 12, "N": 13, "O": 12, "P": 11, "Q": 10, "R": 9,
           "S": 8, "T": 7, "U": 6, "V": 5, "W": 4, "X": 3,
           "Y": 2, "Z": 1}
    
    _list = []
    
    for i in range(0, len(name)):
        _list.append("A")
    # alpha = ''.join(_list)
    name = list(name)
    alpha = _list[:]
    
    rightward = 0
    leftward = 0
    p = 0
    while True:
        if ''.join(alpha) == ''.join(name):
            break
        rightward += dic[name[p]]
        alpha[p] = name[p]
        if ''.join(alpha) == ''.join(name):
            break
        rightward += 1
        p += 1
    
    alpha = _list[:]
    p = 0
    while True:
        if ''.join(alpha) == ''.join(name):
            break
        leftward += dic[name[p]]
        alpha[p] = name[p]
        if ''.join(alpha) == ''.join(name):
            break
        leftward += 1
        p -= 1
        
    if rightward > leftward:
        answer = leftward
    else:
        answer = rightward
    
    return answer

# 중간에 방향을 틀어야 하는 경우 
# ex) "ABAAAAABAB"