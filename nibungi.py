class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

def height(node):
    if node.left!=None:
        left_height = height(node.left)+1
    else:
        left_height = 0
    if node.right!=None:
        right_height = height(node.right)+1
    else:
        right_height = 0
    return max(left_height,right_height)
