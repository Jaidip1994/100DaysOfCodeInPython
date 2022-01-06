![image](https://user-images.githubusercontent.com/11685096/148415610-54819b75-e44d-4eb4-9fd7-a5cf8ccf6cbd.png)

Solution

```python
def isValidSubsequence(array, sequence):
    # Write your code here.
	pointer = 0
	for elem in array:
		if pointer < len(sequence) and elem == sequence[pointer]:
			pointer += 1
	return pointer == len(sequence)
```
