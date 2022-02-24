import math


class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def findmax(root):
    if not root:
        return -math.inf
    else:
        return max(root.data, findmax(root.left), findmax(root.right))


root = NewNode(6)
root.left = NewNode(2)
root.right = NewNode(3)
root.left.left = NewNode(4)
root.left.right = NewNode(5)

print(findmax(root))
