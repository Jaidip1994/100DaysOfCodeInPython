Problem Description: https://leetcode.com/problems/richest-customer-wealth/
![image](https://user-images.githubusercontent.com/11685096/151808551-b7b13b01-3fcc-424d-ab8b-39efe75b1744.png)

Solution
```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_elem = 0
        for elem in accounts:
            sum_elem = max(sum_elem, sum(elem))
        return sum_elem
```
