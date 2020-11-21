def solution(phone_book):
    answer = True
    
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if i == j:
                continue
            elif phone_book[j].startswith(phone_book[i]):
                answer = False
    
    return answer