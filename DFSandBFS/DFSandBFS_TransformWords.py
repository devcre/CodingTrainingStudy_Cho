def solution(begin, target, words):
    answer = 0
    
    class Node:
        def __init__(self, word):
            self.data = word
            self.child = []
    
    usedData = []
    usedData.append(begin)
    initNode = Node(begin)
    
    # 자식노드를 만들 w와
    # 이미 자식노드를 생성한 워드를 모은 배열 pData,
    # 그리고 자식노드에 넣을 word를 인자로 받아서
    # 상위노드의 하위노드 즉 child Node를 추가한다.
    def makeChild(newNode, uData, words):
        for x in words:
            # 한 개의 알파벳만 다른지 알기 위한 변수
            t = 0
            c = 0
            # newNode(의 data인 w)와 x를 비교
            while c < len(x):
                if newNode.data[c] != x[c]:
                    t += 1
                c += 1
            # 알파벳이 하나만 다르면 pData의 자식노드로 넣는다.
            # 부모노드를 자신의 자식노드로 넣지 않는다.
            if t == 1 and x not in uData:
                cNode = Node(x)
                newNode.child.append(cNode)
                uData.append(x)
        if len(uData) != len(words):
            for x in newNode.child:
                makeChild(x, uData, words)
        
    def countTrans(node, t, target):
        for x in node.child:
            if x.data == target:
                return t
        print(t)
        if len(node.child) > 0:
            for x in node.child:
                countTrans(x, t+1, target)
        else:
            return 0
    
    makeChild(initNode, usedData, words)
    t = 1
    answer = countTrans(initNode, t, target)
    
    return answer