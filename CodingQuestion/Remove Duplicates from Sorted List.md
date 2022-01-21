Problem Description: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
![image](https://user-images.githubusercontent.com/11685096/150512165-2d6660eb-a45c-492a-a292-73232572e286.png)

Solution
```python
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = head
        curr = prev.next
        
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return head
```
