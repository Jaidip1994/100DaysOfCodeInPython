Problem Description: https://leetcode.com/problems/delete-node-in-a-linked-list/
![image](https://user-images.githubusercontent.com/11685096/150645909-dca47636-5f5c-4654-975d-d8762426416a.png)

Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
