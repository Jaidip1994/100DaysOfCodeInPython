class NewNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

# count = 0

# def preOrder(root):
#     global count
#     if root:
#         print(root.data)
#         count += 1
#         preOrder(root.left)
#         preOrder(root.right)

def size(root):
    if not root:
        return 0
    else:
        return size(root.left) + size(root.right) + 1

root = NewNode(1)
root.left = NewNode(2)
root.right = NewNode(3)
root.left.left = NewNode(4)
root.left.right = NewNode(5)

# preOrder(root)
# print(f'Size of the Tree is {count}')
print(size(root))
