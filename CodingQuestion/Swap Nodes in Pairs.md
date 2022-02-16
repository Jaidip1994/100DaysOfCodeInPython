Problem Description: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
![image](https://user-images.githubusercontent.com/11685096/154201285-88f3ca95-3f48-4cc4-8f5e-6bd1a5c8e3bf.png)

Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        nxt = cur.next
        
        while True:
            cur.val, nxt.val = nxt.val, cur.val
            if not nxt.next or not nxt.next.next:
                break
            cur = nxt.next
            nxt = cur.next
        return head
```
