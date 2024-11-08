class Node:
    def __init__(self,value,left=None,right=None) :
        self.value=value
        self.left=left
        self.right=right
def make_tree(n):
    if n<=0:
        return Node(n)
    node=Node(n)
    node.left=make_tree(n-1)
    node.right=make_tree(n-1)
    return node

def height(node):
    if node.left!=None:
        left_height=height(node.left)
    else:
        left_height=0
    if node.right!=None:
        right_height=height(node.right)
    else:
        right_height=0
    return max(left_height,right_height)+1

def count(node):
    if node.left!=None:
        left_count=count(node.left)
    else:
        left_count=0
    if node.right!=None:
        right_count=count(node.right)
    else:
        right_count=0
    return  left_count+right_count+1


tree=make_tree(2)
print(count(tree))