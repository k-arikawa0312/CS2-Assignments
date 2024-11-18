##行きがけ

def print_preorder(node):
    print(node,end=",")

    if node.left != None:
        print_preorder(node.left)

    if node.right != None:
        print_preorder(node.right)

##帰りがけ

def print_postorder(node):
    if node.left != None:
        print_postorder(node.left)

    if node.right != None:
        print_postorder(node.right)

    print(node,end=",")

##通りがけ

def print_inorder(node):
    if node.left != None:
        print_inorder(node.left)

    print(node,end=",")

    if node.right != None:
        print_inorder(node.right)
        