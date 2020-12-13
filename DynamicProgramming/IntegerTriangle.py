def solution(triangle):
    answer = 0
    
    # sum = []
    # for i in range(0, len(triangle)):
    #     sum.append([])
    sum = triangle[:]
    
    sum[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i-1])*2):
            if (j-1) < 0:
                sum[i][j] = sum[i-1][j-1]+triangle[i][j]
            elif (j-1) >= len(sum[i-1]):
                sum[i][j] = sum[i-1][j]+triangle[i][j]
            else:
                sum[i][j] = max(sum[i-1][j-1]+triangle[i][j], sum[i-1][j]+triangle[i][j])
    
    return answer