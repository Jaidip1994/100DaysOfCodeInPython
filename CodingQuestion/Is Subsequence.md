Problem Description: https://leetcode.com/problems/is-subsequence/
![image](https://user-images.githubusercontent.com/11685096/156409231-295b1b3e-5b0f-4ed2-a548-e6145631b9f9.png)

Solution
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and t:
            return True
        if s and not t:
            return False
        final_str = list(s)
        count = 0
        for elem in t:
            if final_str[count] == elem:
                count += 1
            if count == len(final_str):
                break
        return count == len(final_str)
```
