Problem Description: https://leetcode.com/problems/add-two-numbers/
![image](https://user-images.githubusercontent.com/11685096/157705784-f96b6745-071a-400a-83fe-14d73e63652e.png)

Solution 1
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        final_list = temp
        carry = 0
        
        while l1 and l2:
            sum_val = l1.val + l2.val + carry
            final_list.next = ListNode(sum_val % 10)
            carry = sum_val // 10
            final_list = final_list.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            final_list, carry = self.returnFunction(l1, final_list, carry)
        if l2:
            final_list, carry = self.returnFunction(l2, final_list, carry)
        if carry > 0:
            final_list.next = ListNode(carry)
        return temp.next
    def returnFunction(self,list_val, final_list, carry):
        print
        if carry == 0:
            final_list.next = list_val
        else:
            while list_val:
                sum_val = list_val.val + carry
                final_list.next = ListNode(sum_val % 10)
                carry = sum_val // 10
                final_list = final_list.next
                list_val = list_val.next
            if carry > 0:
                final_list.next = ListNode(carry)
                final_list = final_list.next
                carry = 0
        return final_list, carry
```

Solution 2
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        from functools import reduce
        arr1 = []
        arr2 = []
        arr1.append(l1.val)
        arr2.append(l2.val)
        
        while(l1.next != None):
            l1 = l1.next
            arr1.append(l1.val)
            
        while(l2.next != None):
            l2 = l2.next
            arr2.append(l2.val)
        final_sum = reduce(lambda x, y : (x*10)+y , arr1[::-1]) + reduce(lambda x, y : (x*10)+y , arr2[::-1])
        
        final_sum_list = list(map(int, str(final_sum))) 
        tempListNode = None
        for index, elem in enumerate(final_sum_list):
            if tempListNode == None:
                finalListNode = ListNode(elem)
            else:
                finalListNode = ListNode(elem, tempListNode)
            tempListNode = finalListNode
        return finalListNode
```
