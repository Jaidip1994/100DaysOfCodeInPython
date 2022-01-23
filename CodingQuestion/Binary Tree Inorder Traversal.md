Problem Description: https://leetcode.com/problems/binary-tree-inorder-traversal/
![image](https://user-images.githubusercontent.com/11685096/150680040-62a03f3f-6a92-47ff-bbd4-b478bed94a17.png)

Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printInorder(self, root: Optional[TreeNode], elem: List[int]):
        if root:
            self.printInorder(root.left, elem)
            elem.append(root.val)
            self.printInorder(root.right, elem)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        final_list = []
        self.printInorder(root, final_list)
        return final_list
```
