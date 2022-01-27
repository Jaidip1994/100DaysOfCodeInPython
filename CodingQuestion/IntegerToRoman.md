Problem Description: https://leetcode.com/problems/integer-to-roman/

![image](https://user-images.githubusercontent.com/11685096/151415287-a34f2dbe-40cd-4058-a764-30d47229f69e.png)
![image](https://user-images.githubusercontent.com/11685096/151415345-35af86a4-4247-43db-9031-7e7857ba488f.png)

Solution

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9 , 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
        for k, v in zip(values, numerals):
            res += (num//k)*v
            num %= k
        return res
```
