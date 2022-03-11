Problem Description: https://leetcode.com/problems/rotate-list/
![image](https://user-images.githubusercontent.com/11685096/157811558-1c460f48-2aba-480a-b7cc-67055e33da7a.png)

Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_elem = []
        if not head or k == 0:
            return head
        temp = head
        while temp:
            list_elem.append(temp.val)
            temp = temp.next
        index = k % len(list_elem)
        if index == 0:
            return head
        temp = head
        list_elem = list_elem[-index:] + list_elem[:-index]
        for elem in list_elem:
            temp.val = elem
            temp = temp.next
        return head
```
