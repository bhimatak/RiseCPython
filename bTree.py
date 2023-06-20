class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        
def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.item) + "->", end='')
        # Traverse right
        inorder(root.right)
    

def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.item) + "->", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.item) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")

inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)

"""
Inorder traversal 
4->2->5->1->3->
Preorder traversal 
1->2->4->5->3->
Postorder traversal 
4->5->2->3->1->
"""