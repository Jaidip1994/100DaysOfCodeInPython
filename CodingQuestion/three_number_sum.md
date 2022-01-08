![image](https://user-images.githubusercontent.com/11685096/148650760-9457d01e-284f-4e64-8377-38bbad35b1e4.png)
Solution
```python
def threeNumberSum(array, targetSum):
    # Write your code here.
    final_arr = []
	left = 1
	right = len(array) - 1
	cur = 0
	array.sort()
	while cur < len(array):
		print(cur, left, right)
		if not left < right:
			cur += 1
			left = cur + 1
			right = len(array) - 1
			continue
		trip_sum = array[cur] + array[left] + array[right]
		if trip_sum == targetSum:
			final_arr.append([array[cur], array[left] , array[right]])
			left += 1
			right -= 1
		elif trip_sum < targetSum:
			left += 1
		else:
			right -= 1
	return final_arr
```
