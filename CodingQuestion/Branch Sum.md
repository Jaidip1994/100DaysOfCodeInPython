Problem Description: https://www.algoexpert.io/questions/Branch%20Sums
![image](https://user-images.githubusercontent.com/11685096/154812308-5be68f31-090c-4f28-89f4-6b0b1155172c.png)

```python
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	final_op = []
    preorder(root, 0, final_op)
	return final_op

def preorder(root, sum_val, final_op):
	if root:
		# print(root.value, end = "=>")
		preorder(root.left, sum_val+root.value,final_op)
		preorder(root.right, sum_val+root.value,final_op)
		
		if not root.left and not root.right:
			# print(f'Sum: {sum_val+root.value}')
			final_op.append(sum_val+root.value)
```
