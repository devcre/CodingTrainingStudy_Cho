import heapq

def solution(scoville, K):
    
    def mix(f1, f2):
        return f1 + (f2 * 2)
    
    def examineK(_list, k):
        ex = True
        for x in _list:
            if x < k:
                ex = False
        
        return ex
    
    heapq.heapify(scoville) # scoville.sort()
    
    food1 = 0
    food2 = 0
    
    count = 0
    while len(scoville) > 1: 
        food1 = heapq.heappop(scoville) # food1 = min(scoville) # scoville.remove(food1)
        food2 = heapq.heappop(scoville) # food2 = min(scoville) # scoville.remove(food2)

        newfood = mix(food1, food2)
        count += 1
        
        heapq.heappush(scoville, newfood)# scoville.append(newfood) # scoville.sort()
        if len(scoville) == 1 and examineK(scoville, K) == False:
            return -1
        elif examineK(scoville, K) == True:
            break
        
    answer = count
    return answer