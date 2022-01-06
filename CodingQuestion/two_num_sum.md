```python
def twoNumberSum(array, targetSum):
    # Write your code here.
	array = sorted(array)
    low = 0
	high = len(array) - 1
	while low <= high:
		if (array[low] + array[high]) == targetSum:
			return [array[low], array[high]]
		elif (array[low] + array[high]) < targetSum:
			low += 1
		else:
			high -= 1
	return []
		
```
