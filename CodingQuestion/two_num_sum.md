![image](https://user-images.githubusercontent.com/11685096/148440464-7366e98c-b7d4-45b2-9bf6-804c0f53a42d.png)

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
