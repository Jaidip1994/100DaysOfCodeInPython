Problem description: https://leetcode.com/problems/maximum-depth-of-binary-tree/
![image](https://user-images.githubusercontent.com/11685096/153814648-7b479de6-b671-41fb-b5a8-1fb2c1936ba2.png)

Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```
