class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def height(root):
    if not root:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


root = NewNode(6)
root.left = NewNode(2)
root.right = NewNode(3)
root.left.left = NewNode(4)
root.left.right = NewNode(5)
root.left.left.right = NewNode(15)
root.left.left.right.left = NewNode(25)
root.left.left.right.right = NewNode(35)

print(height(root))
