Problem Description: https://leetcode.com/problems/merge-two-sorted-lists/
![image](https://user-images.githubusercontent.com/11685096/157087455-cf792296-4954-4a2d-a030-3ae326441137.png)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_list = ListNode(0)
        temp = final_list
        while list1 and list2:
            tempNode = ListNode()
            if list1.val <= list2.val:
                tempNode.val = list1.val
                list1 = list1.next
            else:
                tempNode.val = list2.val
                list2 = list2.next
            temp.next = tempNode
            temp = temp.next
        
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return final_list.next
```
