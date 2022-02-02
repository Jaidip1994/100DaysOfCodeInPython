Problem description:
![image](https://user-images.githubusercontent.com/11685096/152148287-f80b2431-39b4-4085-81c0-ad2c020d3c55.png)

Solution
```python
def bubbleSort(array):
    # Write your code here.
    for i in range(len(array)):
		isSorted = True
		for j in range(1, len(array)-i):
			if array[j-1] > array[j]:
				array[j-1], array[j] = array[j], array[j-1]
				isSorted = False
		if isSorted:
			break
	return array
```
