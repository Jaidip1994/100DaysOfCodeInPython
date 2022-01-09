[Problem Link](https://leetcode.com/problems/plus-one/)

![image](https://user-images.githubusercontent.com/11685096/148693580-adea0f9a-a393-48fd-9b17-a9b0bdca3288.png)

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for elem in digits:
            num = num * 10 + elem
        return list(map(lambda x: int(x), list(str(num+1))))
```
