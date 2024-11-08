from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_bfs(top):
    if top is None:
        return
    
    queue = deque([top])
    
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)    

# テスト用の二分木を作成
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# 幅優先探索の結果を表示
print_bfs(root)