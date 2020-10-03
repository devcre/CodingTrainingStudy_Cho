def solution(bridge_length, weight, truck_weights):
    answer = 0
    
#     b_l = bridge_length
#     tob = []
#     col = 0
#     ctw = 0
#     while True:
#         for x in truck_weights:
#             if ctw + x < weight and col <= b_l:
#                 col += 1
#                 ctw += x
#                 tob.append(x)
#                 truck_weights.remove(x)
#             else:
#                 break
        
#         answer = answer + b_l + len(tob)
    
    class Truck:
        def __init__(self, w, t):
            self._weight = w
            self._time = t
    
    b_l = bridge_length
    t_w = truck_weights
    
    tob = [] # truck on bridge
    ctw = 0 # current truck weight
    col = 0 # current occupied length
    
    tik = 0
    while True:
        tik += 1
        # 다리를 건너는 트럭이 없고 대기 중인 트럭도 없으면 끝
        if len(t_w) == 0 and len(tob) == 0:
            break
        
        # 대기 중인 트럭은 없고 다리를 건너는 트럭이 있음
        if len(t_w) == 0:
            pass

        # 대기 중인 트럭을 추가해도 weight에 미치지 않고
        # 다리에 트럭이 건널 길이(공간)이 있으면
        # 같이 건너도 된다.
        elif ctw + t_w[0] < weight and col < b_l:
            ctw += t_w[0]
            col += 1
            newTruck = Truck(t_w[0], 0)
            tob.append(newTruck)
            del t_w[0]
        
        # 다리를 건너는 중인 트럭이 얼마나 이동했는지       
        for x in tob:
            x._time += 1
            if x._time == b_l:
                ctw -= x._weight
                tob.remove(x)
        
    
    answer = tik
    
    return answer