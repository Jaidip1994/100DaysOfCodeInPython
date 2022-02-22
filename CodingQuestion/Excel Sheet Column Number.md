Problem Description: https://leetcode.com/problems/excel-sheet-column-number/
![image](https://user-images.githubusercontent.com/11685096/155068086-4e7d239b-e5ab-4b1f-8275-77bb536ac7a4.png)

Solution 1
```python
import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dict_elem = {key:val+1 for val, key in enumerate(string.ascii_uppercase) }
        index_val = dict_elem[columnTitle[0]]
        if len(columnTitle) == 1:
            return index_val
        
        for i in range(1, len(columnTitle)):
            index_val = index_val * 26 + dict_elem[columnTitle[i]]
        return index_val
```

Solution 2

``` python
import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dict_elem = {key:val+1 for val, key in enumerate(string.ascii_uppercase) }
        n= len(columnTitle) - 1
        cnt = 0
        for i in columnTitle:
            cnt += (26**n) * dict_elem[i]
            n -= 1
        return cnt
```

Solution 3

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n= len(columnTitle) - 1
        cnt = 0
        for i in columnTitle:
            cnt += (26**n) * (ord(i) - 64)
            n -= 1
        return cnt
```
