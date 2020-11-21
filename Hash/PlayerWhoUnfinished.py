def solution(participant, completion):
    answer = ''
    
    
    # for x in completion:
    #     if x in participant:
    #         participant.remove(x)
    #     else:
    #         return x
    # answer = participant[0]
    
    participant.sort()
    completion.sort()
    
    count = 0
    while len(completion) > count:
        if participant[count] == completion[count]:
            count += 1
            # participant.remove(participant[count])
            # completion.remove(completion[count])
        else:
            return participant[count]
    
    answer = participant[count]

            
    
    return answer