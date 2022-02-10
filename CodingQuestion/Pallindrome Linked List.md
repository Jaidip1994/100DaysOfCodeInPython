Problem Description:https://leetcode.com/problems/palindrome-linked-list/

![image](https://user-images.githubusercontent.com/11685096/152402044-1f25e7dc-51f2-4218-b554-7e50bdbf2a9a.png)

Solution 1
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        point = head
        arr = []
        while point:
            arr.append(point.val)
            point = point.next
        point = head
        while point:
            if point.val == arr[-1]:
                arr.pop()
            else:
                return False
            point = point.next
        return True
```
Solution 2
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        point = head
        arr = []
        while point:
            arr.append(point.val)
            point = point.next
        return arr == arr[::-1]
```
