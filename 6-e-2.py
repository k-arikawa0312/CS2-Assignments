class Node:
    def __init__(self,value,left=None,right=None) :
        self.value=value
        self.left=left
        self.right=right
    
    def __str__(self) -> str:
        return self.value


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

def compute(node,stack):
    if node.left!=None:
        compute(node.left,stack)
    if node.right!=None:
        compute(node.right,stack)
    if node.value=="+":
        r=stack.pop()
        l=stack.pop()
        stack.append(l+r)
    elif node.value=="-":
        r=stack.pop()
        l=stack.pop()
        stack.append(l-r)
    elif node.value=="*":
        r=stack.pop()
        l=stack.pop()
        stack.append(l*r)
    elif node.value=="/":
        r=stack.pop()
        l=stack.pop()
        stack.append(l/r)
    else:
        stack.append(node.value)
tree=Node("*",Node("+",Node("-",Node("/",Node(9),Node(3)),Node(5)),Node(1)),Node(6))
from collections import deque
stack=deque()
compute(tree,stack)
print(stack[0])
#(((9/3)-5)+1)*6