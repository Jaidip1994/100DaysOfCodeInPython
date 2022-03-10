Problem Description: https://leetcode.com/problems/add-strings/
![image](https://user-images.githubusercontent.com/11685096/157710469-9ad1005b-5d69-4ebc-95c8-8c708de906ce.png)

Solution
```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2, carry = list(num1), list(num2), 0
        final_data = ''
        while l1 or l2 or carry:
            val1 = int(l1.pop()) if l1 else 0 
            val2 = int(l2.pop()) if l2 else 0
            
            sum_d = val1 + val2 + carry
            final_data += str(sum_d % 10)
            carry = sum_d // 10
        return final_data[::-1]
```
