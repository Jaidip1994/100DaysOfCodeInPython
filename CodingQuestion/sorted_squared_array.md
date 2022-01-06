![image](https://user-images.githubusercontent.com/11685096/148446999-45535ca9-725d-4a11-8b9c-2a1391ad00f4.png)

Solution
```python
def sortedSquaredArray(array):
    # Write your code here.
	final_arr = [0] * len(array)
	left = 0
	right = len(array) - 1
    for idx in range(len(array)-1, -1, -1):
		if abs(array[left]) <= abs(array[right]):
			final_arr[idx] = array[right]**2
			right -= 1
		else:
			final_arr[idx] = array[left]**2
			left += 1
	return final_arr
```
