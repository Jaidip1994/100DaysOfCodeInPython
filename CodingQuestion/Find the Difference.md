Problem Description: https://leetcode.com/problems/find-the-difference/
![image](https://user-images.githubusercontent.com/11685096/152748021-f0866cf4-0f1a-4918-b5ac-cfbe053d4e10.png)

Solution
```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for i in s:
            c ^= ord(i)
        for i in t:
            c ^= ord(i)
        return chr(c)
```
