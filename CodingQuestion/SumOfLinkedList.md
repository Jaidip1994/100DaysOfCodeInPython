Problem Description:
![image](https://user-images.githubusercontent.com/11685096/151601470-caaf480d-5fc1-452b-9690-f72fa103dd92.png)

Solution

```python
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    carry = 0
	seninal = LinkedList(0)
	final_List = seninal
	while linkedListOne or linkedListTwo:
		sum_num = 0
		if linkedListOne:
			print(linkedListOne.value)
			sum_num += linkedListOne.value
			linkedListOne = linkedListOne.next
		if linkedListTwo:
			print(linkedListTwo.value)
			sum_num += linkedListTwo.value
			linkedListTwo = linkedListTwo.next
		sum_num += carry
		final_List.next = LinkedList(sum_num%10)
		carry = sum_num//10
		final_List = final_List.next
	if carry != 0:
		final_List.next = LinkedList(carry)
	return seninal.next
```
