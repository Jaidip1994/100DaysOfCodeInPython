Problem Description: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
![image](https://user-images.githubusercontent.com/11685096/155669881-f17b5fac-2dc8-46bf-9a99-eb2e8b979a1b.png)

Solution
```python
from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        freq_count = Counter(s)
        print(freq_count)
        lis=[]
        a=0
        for values in freq_count.values():
            # print(lis, values)
            while values in lis:
                values-=1
                a+=1
            if values!=0:
                lis.append(values)
        return a
```
