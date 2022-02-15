Problem Description: https://leetcode.com/problems/single-number/submissions/
![image](https://user-images.githubusercontent.com/11685096/153998154-c2617823-9c14-4672-8555-8982f21128ac.png)

Solution
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for elem in nums:
            x ^= elem
        return x
```
