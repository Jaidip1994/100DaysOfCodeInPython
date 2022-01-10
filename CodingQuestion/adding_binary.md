Problem Description: https://leetcode.com/problems/add-binary/

![image](https://user-images.githubusercontent.com/11685096/148821379-ff722893-142d-4fa0-b767-5c24d85e6369.png)

Solution 1
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
```

Solution 2
```python
class Solution:
    def convertToDec(self, a):
        final_elem = 0
        for index, elem in enumerate(a[::-1]):
            final_elem = final_elem + int(elem) * (2 ** index)
        return final_elem
    def addBinary(self, a: str, b: str) -> str:
        x = self.convertToDec(a)
        y = self.convertToDec(b)
        return bin(x+y)[2:]
        
```
