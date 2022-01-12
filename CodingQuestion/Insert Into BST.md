Problem Description: https://leetcode.com/problems/insert-into-a-binary-search-tree/

![image](https://user-images.githubusercontent.com/11685096/149192823-935b0ee7-9fa4-4abc-8356-fcb93acf78e5.png)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        cur = root
        while True:
            if root.val > val:
                if root.left:
                    root = root.left  
                else: 
                    root.left = TreeNode(val)
                    break
            elif root.val < val:
                if root.right:
                    root = root.right  
                else: 
                    root.right = TreeNode(val)
                    break
        return cur
```
