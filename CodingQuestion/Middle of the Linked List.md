Problem Description: https://leetcode.com/problems/middle-of-the-linked-list/
![image](https://user-images.githubusercontent.com/11685096/155470421-e09ddc0a-f418-4660-acc4-6d3716f5adf2.png)

Solution
```python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```
