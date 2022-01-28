Problem Description
![image](https://user-images.githubusercontent.com/11685096/151602376-e7978e5e-fe7a-4dd7-8ddf-54fb4338d5b4.png)

Solution
```python
def binarySearch(array, target):
    # Write your code here.
    low = 0
	high = len(array) - 1
	while low <= high:
		mid = (low + high)//2
		print(array[mid])
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			high = mid - 1
		else:
			low = mid  + 1
	return -1
```
