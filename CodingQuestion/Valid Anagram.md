Problem Description: https://leetcode.com/problems/valid-anagram/
![image](https://user-images.githubusercontent.com/11685096/152212562-bfb9ecb9-2e11-4189-96f3-fa6d6545a7c9.png)

Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        sCount, pCount = {}, {}
        for i in range(len(t)):
            pCount[t[i]] = 1 + pCount.get(t[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        return sCount == pCount
```
