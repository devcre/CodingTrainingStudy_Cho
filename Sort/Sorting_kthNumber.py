def solution(array, commands):
    answer = []
    
    def merge_sort(arr):
        if len(arr) < 2:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        merged_arr = []
        x = y = 0
        while (x < len(left)) & (y < len(right)):
            if left[x] < right[y]:
                merged_arr.append(left[x])
                x += 1
            else:
                merged_arr.append(right[y])
                y += 1
        
        merged_arr += left[x:]
        merged_arr += right[y:]
        return merged_arr
    
    for smallc in commands:
        unsortedArray = array[smallc[0]-1:smallc[1]]
        sortedArray = merge_sort(unsortedArray)
        answer.append(sortedArray[smallc[2]-1])
        
    return answer