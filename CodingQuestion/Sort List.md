Problem Description: https://leetcode.com/problems/sort-list/
![image](https://user-images.githubusercontent.com/11685096/155468259-795df488-9ccf-49bd-a263-eb8b59dd11ac.png)

Solution 1
Using a Separate List and then Creating a separate Linked List and returning the same
```python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        elem = []
        while head:
            elem.append(head.val)
            head = head.next
        elem.sort()
        sentinal = ListNode()
        temp = sentinal
        for e in elem:
            temp.next = ListNode(e)
            temp = temp.next
        return sentinal.next
        
```

Solution 2
Using Inplace replace and using iter object
```python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        elem = []
        temp = head
        while temp:
            elem.append(temp.val)
            temp = temp.next
        elem.sort()
        temp = head
        iter_obj = iter(elem)
        while temp:
            item = next(iter_obj)
            temp.val = item
            temp = temp.next
        return head
```
