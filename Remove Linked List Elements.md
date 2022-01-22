Problem Description: https://leetcode.com/problems/remove-linked-list-elements/
![image](https://user-images.githubusercontent.com/11685096/150645557-3d53b3b8-e585-4d5b-9061-f493818cf387.png)

Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        sentinal = ListNode(0, head)
        pred = sentinal
        while head:
            if head and head.val == val:
                while head and head.val == val:
                    head = head.next
                pred.next = head
                continue

            pred = pred.next
            head = head.next
        return sentinal.next
```
