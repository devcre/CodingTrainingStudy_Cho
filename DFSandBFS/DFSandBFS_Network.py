def solution(n, computers):
    answer = 0
    
    class Node:
        def __init__(self, num):
            self.com = num
            self.child = []
    
    root = Node(n)
    c = 0
    while c < n:
        root.child.append(Node(c))
        c += 1
    
    # root Node인 rNode와 연결에 대한 정보가 담긴 2차원 배열을 원소로 받아서
    # root Node가 가지고 있는 child Node들의 child배열을 coms를 바탕으로 채우는 함수
    def fillNode(rNode, coms):
        t = 0
        ptrNode = rNode.child[t]
        
        # while t < len(rNode.child):
        #     c = 0
        #     while c < len(coms[t]):
        #         if coms[t][c] == 1 and c not in ptrNode.child:
        #             ptrNode.child.append(c)
        #         c += 1
        #     t += 1
        #     ptrNode = rNode.child[t]
        
        for xcom in coms:
            c = 0
            for conn in xcom:
                if conn == 1 and c not in ptrNode.child:
                    ptrNode.child.append(c)
                c += 1
            t += 1
            ptrNode = rNode.child[t]
    
    status = []
    
    
    return answer