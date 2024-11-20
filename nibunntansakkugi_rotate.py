class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        """
        右回転の実装
            y                   x
           / \                /   \
          x   T3    -->     T1    y
         / \                     /  \
        T1  T2                 T2   T3
        """
        x = y.left
        T2 = x.right

        # 回転の実行
        x.right = y
        y.left = T2

        # 高さの更新
        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        """
        左回転の実装
            x                   y
           / \                /   \
          T1  y     -->     x     T3
             / \          /  \
            T2  T3      T1   T2
        """
        y = x.right
        T2 = y.left

        # 回転の実行
        y.left = x
        x.right = T2

        # 高さの更新
        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        # 通常の二分探索木の挿入
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # 重複キーは許可しない

        self.update_height(root)
        return root

    def print_tree(self, root, level=0, prefix="Root: "):
        if not root:
            return
        print("  " * level + prefix + str(root.key))
        if root.left:
            self.print_tree(root.left, level + 1, "L--- ")
        if root.right:
            self.print_tree(root.right, level + 1, "R--- ")

# 使用例
def main():
    bst = BinarySearchTree()
    root = None
    
    # ツリーの作成
    keys = [10, 5, 15, 3, 7]
    for key in keys:
        root = bst.insert(root, key)
    
    print("元の木:")
    bst.print_tree(root)
    
    # 右回転のデモ（ノード10を中心に）
    if root and root.left:
        print("\n右回転後:")
        root = bst.right_rotate(root)
        bst.print_tree(root)
    
    # 左回転のデモ
    if root and root.right:
        print("\n左回転後:")
        root = bst.left_rotate(root)
        bst.print_tree(root)

if __name__ == "__main__":
    main()