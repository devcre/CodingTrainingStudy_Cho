def solution(numbers):
    answer = ''
    
    def compare(left, right):
        lstr = str(left)
        rstr = str(right)
        
        if int(lstr + rstr) > int(rstr + lstr):
            return left
        else:
            return right
        
    def merge_method_sort(arr):
        if len(arr) < 2:
            return arr
        
        mid = len(arr) // 2
        left = merge_method_sort(arr[:mid])
        right = merge_method_sort(arr[mid:])
        
        merged_arr = []
        x = y = 0
        
        while x < len(left) and y < len(right):
            if compare(left[x], right[y]) == left[x]:
                merged_arr.append(left[x])
                x += 1
            else:
                merged_arr.append(right[y])
                y += 1
        merged_arr += left[x:]
        merged_arr += right[y:]
        return merged_arr
    
    sortedArray = merge_method_sort(numbers)
    if sortedArray[0] == 0:
        return '0'
    else:
        for e in sortedArray:
            answer = answer + str(e)
    return answer