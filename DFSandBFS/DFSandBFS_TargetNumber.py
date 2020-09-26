def solution(numbers, target):
    answer = 0
    
    class Node:
        def __init__(self, item):
            self.data = item
            self.left = None
            self.right = None
    
    root = Node(0)
    
    def createTree(lists, count, ptr):
        ptr.left = Node(lists[count])
        x = 0
        x -= lists[count]
        ptr.right = Node(x)
        if count+1 < len(lists):
            createTree(lists, count+1, ptr.left)
            createTree(lists, count+1, ptr.right)
    
    createTree(numbers, 0, root)
    
    p = root
    
    
    return answer