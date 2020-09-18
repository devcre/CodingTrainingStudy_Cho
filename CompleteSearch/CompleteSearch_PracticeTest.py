def solution(answers):
    answer = []
    n1 = 0
    n2 = 0
    n3 = 0
    count = 0
    count1 = 1
    count2 = 1
    count3 = 1
    
    for ans in answers:
        count += 1
        
        if count1 == ans:
            n1 += 1
        if count1 == 5:
            count1 = 1
        else:
            count1 += 1
            
        if count%2 == 0:
            if count2 == 2:
                count2 += 1
            if count2 == ans:
                n2 += 1
            if count2 == 5:
                count2 = 1
            else:
                count2 += 1
        else:
            if ans == 2:
                n2 += 1
        
        if (count3 == 1 or count3 == 2) and ans == 3:
            n3 += 1
        elif (count3 == 3 or count3 == 4) and ans == 1:
            n3 += 1
        elif (count3 == 5 or count3 == 6) and ans == 2:
            n3 += 1
        elif (count3 == 7 or count3 == 8) and ans == 4:
            n3 += 1
        elif (count3 == 9 or count3 == 10) and ans == 5:
            n3 += 1
        if count3 == 10:
            count3 = 1
        else:
            count3 += 1
    
    if n1 > n2 and n1 > n3:
        answer.append(1)
    elif n2 > n1 and n2 > n3:
        answer.append(2)
    elif n3 > n1 and n3 > n2:
        answer.append(3)
    elif n1 == n2 and n1 > n3:
        answer.append(1)
        answer.append(2)
    elif n2 == n3 and n3 > n1:
        answer.append(2)
        answer.append(3)
    elif n1 == n3 and n1 > n2:
        answer.append(1)
        answer.append(3)
    elif n1 == n2 and n2 == n3:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    
    return answer