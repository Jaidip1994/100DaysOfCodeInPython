Problem Description: https://leetcode.com/problems/linked-list-cycle/
![image](https://user-images.githubusercontent.com/11685096/153467708-e385dc03-1756-4615-a1f1-b0f0c058d8d6.png)

Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        cur = head
        nxt = cur.next.next
        while nxt and nxt.next:
            if nxt.next == cur:
                return True
            cur = cur.next
            nxt = nxt.next.next
        return False
```
