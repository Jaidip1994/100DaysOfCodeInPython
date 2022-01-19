Problem Description: https://leetcode.com/problems/linked-list-cycle-ii/

![image](https://user-images.githubusercontent.com/11685096/150166584-e68d83f8-dc6c-4273-8836-0f2bcd6c6d92.png)

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd’s Cycle-Finding Algorithm
        fast = slow = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while head:
                    if head == slow:
                        return head
                    head, slow = head.next, slow.next
        return None
```
