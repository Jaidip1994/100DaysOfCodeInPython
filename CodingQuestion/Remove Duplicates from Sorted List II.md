Problem Description: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
![image](https://user-images.githubusercontent.com/11685096/150519373-037de8ad-c080-497b-bab3-616371fab739.png)

Solution
Using a Set and List Approach
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        unq_elem = set()
        cur = head
        elem_to_remove = set()
        while cur:
            if cur.val not in unq_elem:
                unq_elem.add(cur.val)
            else:
                elem_to_remove.add(cur.val)
            cur = cur.next
        unq_elem -= elem_to_remove
        unq_elem = sorted(list(unq_elem))
        head_cpy = None
        cur = head_cpy
        for elem in unq_elem:
            if not head_cpy:
                head_cpy = ListNode(elem)
                cur = head_cpy
                continue
            else:
                temp = ListNode(elem)
                cur.next = temp
            cur = cur.next
        return  head_cpy
```
Using a Sentinal Node Concept
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinal = ListNode(0, head)
        pred = sentinal
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            
            head = head.next
        return sentinal.next
```
