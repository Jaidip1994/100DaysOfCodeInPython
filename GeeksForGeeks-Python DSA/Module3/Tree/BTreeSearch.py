class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

def findElem(root, elem):
    if not root:
        return False
    elif root.data == elem:
        return True
    elif findElem(root.left, elem) == True:
        return True
    else:
        return findElem(root.right, elem)


root = NewNode(6)
root.left = NewNode(2)
root.right = NewNode(3)
root.left.left = NewNode(4)
root.left.right = NewNode(5)

print(findElem(root, 15))