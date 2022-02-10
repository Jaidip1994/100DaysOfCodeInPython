Problem Description: https://leetcode.com/problems/reverse-linked-list/
![image](https://user-images.githubusercontent.com/11685096/153475312-19197780-b21e-4138-aabc-25e20f9100ea.png)

Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
```
