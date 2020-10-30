from itertools import combinations
import copy

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

def solution(distance, rocks, n):
    answer = 0
    
    delrocks = list(combinations(rocks, n))
    
    def maxdistance(delrocks, rocks, distance):
        maxdis = 0
        count = 0
        while count < len(delrocks):
            mindis = distance
            newr = list(rocks) # or newr = copy.deepcopy(rocks)
            # print(delrocks[count][0])
            # print(delrocks[count][1])
            # for x in newr:
            #   print("x: ", x)
            newr.remove(delrocks[count][0])
            newr.remove(delrocks[count][1])
            
            newr.append(0)
            newr.append(distance)
            newr.sort()
            
            t = 0
            while t+1 < len(newr):
                val = newr[t+1] - newr[t]
                if val < mindis:
                    mindis = val
                t += 1
            
            if maxdis < mindis:
                maxdis = mindis
            count += 1
        
        return maxdis
    
    answer = maxdistance(delrocks, rocks, distance)
    
    return answer

print(solution(distance, rocks, n))