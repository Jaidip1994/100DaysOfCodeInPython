Problem Description: https://leetcode.com/problems/string-to-integer-atoi/
![image](https://user-images.githubusercontent.com/11685096/149455111-4a2767d7-1ee8-42d5-9ad8-d93b55514ea4.png)
![image](https://user-images.githubusercontent.com/11685096/149455148-8f491a54-6098-48ac-9628-ca736357ba81.png)
![image](https://user-images.githubusercontent.com/11685096/149455172-a05ee4ce-3539-4216-8a31-1af901c15376.png)


Solution 1
```python
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        s = s.split(' ')[0]
        regex = r"([-|\+]?\d+)"
        if s[0] not in list(map(lambda x: str(x), list(range(0,10)))) + ['-', '+']:
            return 0
        if len(s)> 1 and s[0] in ['-', '+'] and s[1] not in list(map(lambda x: str(x), list(range(0,10)))):
            return 0
        if len(s) == 1 and s[0] in ['-', '+']:
            return 0
        integ_val = int(re.search(regex, s).group())
        if -2**31 <= integ_val and integ_val <= (2**31 - 1):
            integ_val =  integ_val        
        elif  integ_val < 0:
            integ_val = -2**31
        else:
            integ_val = 2**31 - 1
        return integ_val
```

Solution 2
```python
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        s = s.split(' ')[0]
        regex = r"([-|\+]?\d+)"
        sign = 1
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else sign
            s = s[1:]
        if len(s) == 0:
            return 0
        if s[0] not in list(map(lambda x: str(x), list(range(0,10)))):
            return 0
        integ_val = int(re.search(regex, s).group()) * sign
        return max(-2**31, min(integ_val, (2**31 - 1)))
 ```
