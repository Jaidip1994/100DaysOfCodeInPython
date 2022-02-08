Problem Description: https://leetcode.com/problems/add-digits/
![image](https://user-images.githubusercontent.com/11685096/152952850-933110b0-c836-44b5-b4a2-08166b00c5d1.png)

Solution
```python
class Solution:
    def addDigits(self, num: int) -> int:
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10
            if num == 0 and digital_root > 9:
                num, digital_root = digital_root, 0
        return digital_root
```
