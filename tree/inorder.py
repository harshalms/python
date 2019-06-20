class Node:    
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
    # def inorder(self):
def inorder(a):
    if a == None:
        return None
    inorder(a.left)
    print(a.value, end=",")
    inorder(a.right)
    

root = Node(1)
# print(root.value)
# print(root.left)
root.left = Node(4)
root.left.right = Node(6)
# print(root.left.value)
root.left.left = Node(5)
# print(root.right.value)
inorder(root)
