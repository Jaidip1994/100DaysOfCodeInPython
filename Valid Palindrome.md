Problem description: https://leetcode.com/problems/valid-palindrome/
![image](https://user-images.githubusercontent.com/11685096/152394531-e4f4a707-0812-4cce-99e8-638e787a2996.png)


Solution 1
```python
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == ' ':
            return True
        regex = r"[a-zA-Z0-9]+"
        final_str = re.findall(regex, s)
        final_str = ''.join(list(map(lambda x: x.lower(), final_str)))
        return final_str == final_str[::-1]
```

Solution 2
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s  = ''.join([elem for elem in s if elem.isalnum()])
        return s == s[::-1]
```
