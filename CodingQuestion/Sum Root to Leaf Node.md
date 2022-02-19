ProblemDescription: https://leetcode.com/problems/sum-root-to-leaf-numbers/

![image](https://user-images.githubusercontent.com/11685096/154812929-1ac5ef77-b557-44cf-bff2-ccf1e2263aa9.png)

Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        final_sum = []
        self.preorder(root, '', final_sum)
        return sum(final_sum)
        
    def preorder(self, root, val, final_sum):
        if root:
            temp_sum =val+str(root.val) 
            if not root.left and not root.right:
                final_sum.append(int(temp_sum))
                return
            self.preorder(root.left,temp_sum, final_sum)
            self.preorder(root.right,temp_sum, final_sum)
```
