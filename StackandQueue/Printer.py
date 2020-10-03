def solution(priorities, location):
    answer = 0
    _flag = 0
    
#     ptr = priorities[0]
#     del priorities[0]
    
#     for x in priorities:
#         if ptr < x:
#             _flag = 1
    
#     if _flag == 1:
#         priorities.append(ptr)
#         _flag = 0
#     else:
#         answer += 1
        
    class Numb:
        def __init__(self, num, loc):
            self._num = num
            self._loc = loc
    
    c = 0
    numbPri = []
    for x in priorities:
        numNumb = Numb(x, c)
        numbPri.append(numNumb)
        c += 1
    
    while True:
        ptr = numbPri[0]
        del numbPri[0]
        
        for x in numbPri:
            if ptr._num < x._num:
                _flag = 1
                break
        
        if _flag == 1:
            numbPri.append(ptr)
            _flag = 0
        else:
            answer += 1
            if ptr._loc == location:
                break
    
    return answer