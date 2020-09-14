def solution(citations):
    answer = -1

    n = len(citations)
    
    while answer <= n:
        answer += 1
        i = 0
        for x in citations:
            if x >= answer:
                i += 1
        if answer > i:
            answer -= 1
            break
        
    return answer