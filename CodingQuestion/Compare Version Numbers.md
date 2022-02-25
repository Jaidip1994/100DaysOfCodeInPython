Problem Description: https://leetcode.com/problems/compare-version-numbers/
![image](https://user-images.githubusercontent.com/11685096/155672174-e6e4ecbe-76cf-4f04-9084-060802cf239f.png)

Solution 1
```python 
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_split = list(map(lambda x: int(x), version1.split(".")))
        v2_split = list(map(lambda x: int(x),version2.split(".")))
        v1_len = len(v1_split)
        v2_len = len(v2_split)
        if v1_len > v2_len:
            v2_split += [0] * (v1_len - v2_len)
        elif v1_len < v2_len:
            v1_split += [0] * (v2_len - v1_len)
        
        for i in range(len(v2_split)):
            if v2_split[i]  > v1_split[i]:
                return -1
            elif v1_split[i]  > v2_split[i]:
                return 1
        return 0
```

Solution 2
```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_split = list(map(lambda x: int(x), version1.split(".")))
        v2_split = list(map(lambda x: int(x),version2.split(".")))
        i = 0
        while i <len(v2_split) and i < len(v1_split):
            if v2_split[i]  > v1_split[i]:return -1
            if v1_split[i]  > v2_split[i]:return 1
            i+= 1
        if sum(v1_split[i:]): return 1
        if sum(v2_split[i:]): return -1
        return 0
```
