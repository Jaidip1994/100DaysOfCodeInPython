Problem Description: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
![image](https://user-images.githubusercontent.com/11685096/155473139-22621cca-966d-41f8-8dfb-1adf9eea4770.png)

Solution 1
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast= slow.next
        
        while True:
            if not fast.next or not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
```

Solution 2
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        slow = temp
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return temp.next
```
