Problem Description: https://leetcode.com/problems/word-pattern/
![image](https://user-images.githubusercontent.com/11685096/149736560-5e6bfacc-3a1f-4805-991d-8631bf240dce.png)

Solution1
```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(" ")
        if len(pattern) != len(word_list) or len(set(pattern)) != len(set(word_list)):
            return False
        words = list(zip(list(pattern), word_list))
        final_dict = {}
        for key, value in words:
            if key in final_dict.keys():
                if final_dict[key] != value:
                    return False
            else:
                final_dict[key] = value
        return True
```

Solution 2
```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        s = pattern
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
```

Solution3
```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        s = pattern
        return list(map(s.find, s)) == list(map(t.index, t))
```
