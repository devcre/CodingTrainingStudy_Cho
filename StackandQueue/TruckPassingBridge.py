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
        if len(t_w) == 0 and len(tob) == 0:
            break
        
        if len(t_w) == 0:
            pass
        elif ctw + t_w[0] < weight and col < b_l:
            ctw += t_w[0]
            col += 1
            newTruck = Truck(t_w[0], 0)
            tob.append(newTruck)
            del t_w[0]
                
        for x in tob:
            x._time += 1
            if x._time == b_l:
                ctw -= x._weight
                tob.remove(x)
        
    
    answer = tik
    
    return answer