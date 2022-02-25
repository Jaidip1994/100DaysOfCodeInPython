Problem Description: https://leetcode.com/problems/first-missing-positive/
![image](https://user-images.githubusercontent.com/11685096/155681853-6d042b22-d753-4115-8a57-85bd59330382.png)

Solution:
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num > 0]
        nums.sort()
        start = 1
        for i in nums:
            if start < i:
                break
            elif start > i:
                start -= 1
            start += 1
        return start
```
