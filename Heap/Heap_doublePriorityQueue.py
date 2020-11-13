def solution(operations):
    answer = []
    _list = []
    
    for x in operations:
        if "I" in x:
            x.replace("I ", "")
            _list.append(float(x))
        elif "D 1" in x:
            _list.remove(max(_list))
        else:
            _list.remove(min(_list))
    
    if len(_list) == 0:
        return [0,0]
    else:
        answer = [max(_list), min(_list)]
    return answer