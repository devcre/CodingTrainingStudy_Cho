def solution(genres, plays):
    answer = []
    _list = []
    
    # 장르 가려내기
    # dic = {500: 'classic', 600: 'pop', 150: 'classic', 800: 'classic', 2500: 'pop'}
    dic = {}
    for i in range(0, len(genres)):
        dic[plays[i]] = genres[i]
    
    # gen = ['classic', 'pop']
    gen = list(set(list(dic.values())))
    
    # playedGen = {'pop': 0, 'classic': 0}
    playedGen = {}
    for x in gen:
        playedGen[x] = 0
    # playedGen = {'classic': 1450, 'pop': 3100}
    for x in plays:
        playedGen[dic[x]] = playedGen[dic[x]] + x
    
    # genres = [1450, 3100, 1450, 1450, 3100]
    for i in range(0, len(genres)):
        genres[i] = playedGen[genres[i]]
    
    # _list = [[0, 1450, 500], [1, 3100, 600], [2, 1450, 150], [3, 1450, 800], [4, 3100, 2500]]
    for c in range(0, len(plays)): 
        _list.append([c, genres[c], plays[c]])
    
    # _list = [[4, 3100, 2500], [1, 3100, 600], [3, 1450, 800], [0, 1450, 500], [2, 1450, 150]]
    _list.sort(key=lambda x:(x[1], x[2], -x[0]), reverse=True)
    
    ptr = 0
    genres = sorted(set(genres), reverse=True)
    for x in genres:
        if _list[ptr][1] != _list[ptr+1][1]:
            answer.append(_list[ptr][0])
            ptr += 1
        else:
            answer.append(_list[ptr][0])
            answer.append(_list[ptr+1][0])
            while x == _list[ptr][1] and len(_list) > ptr+1:
                ptr += 1
        
    
    return answer