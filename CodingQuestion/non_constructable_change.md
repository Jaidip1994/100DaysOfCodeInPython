![image](https://user-images.githubusercontent.com/11685096/148648457-b763dafb-7fe9-4137-b27a-26be20564d5e.png)

Solution
```python
def nonConstructibleChange(coins):
    # Write your code here.
	coins.sort()
	change = 0
	for elem in coins:
		if elem > change + 1:
			return change + 1
		change += elem
		print(change)
	return change + 1

```
