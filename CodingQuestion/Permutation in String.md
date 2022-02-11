Problem Description: https://leetcode.com/problems/permutation-in-string/
![image](https://user-images.githubusercontent.com/11685096/153643400-1d5179e4-48d2-451a-926e-bcc7d3b60492.png)

Solution 1
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = dict()
        s2_count = dict()
        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        if s1_count == s2_count:
            return True
        for i in range(len(s1), len(s2)):
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            # print(s2_count)
            s2_count[s2[i - len(s1)]] -= 1
            if s2_count[s2[i - len(s1)]] == 0:
                s2_count.pop(s2[i - len(s1)])
            if s1_count == s2_count:
                return True
        return False
```

Solution2
```python
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count, s2_count = Counter(s1), Counter(s2[:len(s1)])
        
        for i in range(len(s2)-len(s1)):
            # print(s1_count, s2_count)
            if s1_count == s2_count: return True
            
            if s2_count[s2[i]] == 1: 
                del s2_count[s2[i]]
            else: 
                s2_count[s2[i]] -= 1
            if s2[i+len(s1)] in s2_count: 
                s2_count[s2[i+len(s1)]] += 1
            else: 
                s2_count[s2[i+len(s1)]] = 1
                
        return s1_count == s2_count
```

Solution3
```python
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        for i in range(len(s2)):
            sub = s2[i:i+len(s1)]
            d2 = Counter(sub)
            if d1 == d2:
                return True
        return False
```
