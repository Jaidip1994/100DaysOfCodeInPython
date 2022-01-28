Problem Descripion
![image](https://user-images.githubusercontent.com/11685096/151597925-92f6b119-16bc-44be-86b2-b6c289236b1f.png)

Solution
```python
def isPalindrome(string):
    # Write your code here.
	if not string or len(string) == 1:
		return True
  for i in range(len(string)//2):
    if string[i] != string[-(i+1)]:
      return False
	return True
```
