Problem Description: https://leetcode.com/problems/length-of-last-word/

![image](https://user-images.githubusercontent.com/11685096/148998237-ae69f74b-d90f-481e-aed0-011be1e9868e.png)

Solution 1
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        cnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                flag = True
                cnt  += 1
            if s[i] == ' ' and flag:
                break
        return cnt
```

Solution 2
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
```
