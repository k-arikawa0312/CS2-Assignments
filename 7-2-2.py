class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.value)

def print_inorder(node):
    if node.left != None:
        print_inorder(node.left)
        
    print(node, end=', ')
    
    if node.right != None:
        print_inorder(node.right)

def add(node, value):
    if node == None:
        return Node(value)
    
    if node.value == value:
        raise Exception('Already added.')
        
    if value < node.value:
        node.left = add(node.left, value)
        return node
    
    if value > node.value:
        node.right = add(node.right, value)
        return node

def contains(node, value):
    if node == None:
        return False
    
    if node.value == value:
        return True
    
    if value < node.value:
        return contains(node.left, value)
    
    if value > node.value:
        return contains(node.right, value)

def delete(node, value):
    if node == None:
        raise Exception('Not added.')
        
    if node.value == value:
        if node.left != None and node.right != None:
            (right_node, min_node) = delete_min(node.right)
            node.right = right_node
            node.value = min_node.value
            return node
        if node.left != None:
            return node.left
        if node.right != None:
            return node.right
        return None
    
    if value < node.value:
        node.left = delete(node.left, value)
        return node
    
    if value > node.value:
        node.right = delete(node.right, value)
        return node    

def delete_min(node):
    if node.left != None:
        (left_node, min_node) = delete_min(node.left)
        node.left = left_node
        return (node, min_node)
    
    return (node.right, node)

def find_min(node):
    result=node
    while result.left!=None:
        result=result.left
    return result

def find_max(node):
    result=node
    while result.right!=None:
        result=result.right
    return result
