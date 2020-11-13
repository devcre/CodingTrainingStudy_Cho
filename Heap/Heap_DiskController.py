def solution(jobs):
    answer = 0
    _len = len(jobs)
    
#     def firstin(_list):
#         _max = _list[0]
#         for i in range(1, len(_list)):
#             if _max[0] < _list[i][0]:
#                 _max = _list[i]
#         _list.remove(_max)
#         return _max
    
#     def leasttime(_list):
#         _min = _list[0]
#         for j in range(1, len(_list)):
#             if _min[1] > _list[j][1]:
#                 _min = _list[j]
#         _list.remove(_min)
#         return _min
#     diskcon.append(firstin(jobs))
    jobs.sort(key=lambda x:x[1])
    
    exe = jobs.pop(0)
    endtik = exe[1]

    answer += exe[1]
    while len(jobs) > 0:
        exe = jobs.pop(0)
        # endtik = exe[1] - exe[0]
        
        if endtik > exe[0]:
            answer += exe[1] + (endtik - exe[0])
            endtik += exe[1]
        else:
            answer += exe[1]
            endtik += exe[1] + (exe[0] - endtik)

    return answer//_len