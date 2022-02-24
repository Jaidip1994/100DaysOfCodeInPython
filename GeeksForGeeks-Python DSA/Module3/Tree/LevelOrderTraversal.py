class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

# def levelOrder(root):
#     elem_list = [root]
#     while elem_list:
#         temp = []
#         for elem in elem_list:
#             print(elem.data, end = "-->")
#             if elem.left:
#                 temp.append(elem.left)
#             if elem.right:
#                 temp.append(elem.right)
#         print("")
#         elem_list = temp

def levelOrder(root):
    elem_list = [root]
    while elem_list:
        elem =  elem_list.pop(0)
        print(elem.data, end = "-->")
        if elem.left:
            elem_list.append(elem.left)
        if elem.right:
            elem_list.append(elem.right)

root = NewNode(6)
root.left = NewNode(2)
root.right = NewNode(3)
root.left.left = NewNode(4)
root.left.right = NewNode(5)
root.left.left.right = NewNode(15)
root.left.left.right.left = NewNode(25)
root.left.left.right.right = NewNode(35)

levelOrder(root)