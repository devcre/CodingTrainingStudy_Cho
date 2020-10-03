def solution(prices):
    answer = []
    
    count = 0
    while count < len(prices):
        c = 1
        while (count+c) < len(prices):
            if prices[count] <= prices[count+c]:
                c += 1
            else:
                c += 1
                break
        
        answer.append(c-1)
        count += 1
                
            
    return answer