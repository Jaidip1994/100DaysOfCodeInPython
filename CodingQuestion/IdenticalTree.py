# Input:
#            1                        1
#         /     \                  /     \
#        2       3                2       3
#      /   \   /   \            /   \   /   \
#     4     5 6     7          4     5 6     7

# Output: True
# Explanation: Both binary trees have the same structure and contents.

# Input:
#            1                        1
#         /     \                  /     \
#        2       3                2       3
#      /   \   /   \            /   \   /
#     4     5 6     7          4     5 6

# Output: False
# Explanation: Both binary trees have different structures.

# Input:
#            1                        1
#         /     \                  /     \
#        2       3                2       3
#      /   \   /   \            /   \   /   \
#     4     5 6     7          4     5 6     8

# Output: False
# Explanation: Both binary trees have the same structure but differ in nodes’ values.

from os import sep


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def preOrderTraversal(root):
    if root:
        print(root.val, end="-->")
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)


def isIdentical(x, y):
    if x and y:
        return True
    return (x is not None and y is not None) and (x.val == y.val) and isIdentical(x.left, y.left) and isIdentical(x.right, y.right)


if __name__ == '__main__':

    # construct the first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)
    preOrderTraversal(x)
    print("")
    # construct the second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)
    preOrderTraversal(y)
    print("")
