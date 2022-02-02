Problem Description: https://leetcode.com/problems/find-all-anagrams-in-a-string/
![image](https://user-images.githubusercontent.com/11685096/152210348-5057f72c-a902-4173-91f8-b51c49be3bd1.png)

Solution
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        res = [0] if pCount == sCount else []
        l = 0
        for i in range(len(p), len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l+= 1
            if sCount == pCount:
                res.append(l)
        return res
```
