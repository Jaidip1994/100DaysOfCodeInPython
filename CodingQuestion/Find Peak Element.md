Problem Description: https://leetcode.com/problems/find-peak-element/
![image](https://user-images.githubusercontent.com/11685096/155685507-8a2799bf-9dc1-4a24-87f0-5dd49a1cf5bb.png)

Solution 1
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-math.inf] + nums + [-math.inf]
        start = 0
        while start + 1 < len(nums):
            if start + 2 < len(nums):
                if nums[start] < nums[start + 1] > nums[start + 2]:
                    return start
            else:
                if nums[start] < nums[start + 1]:
                    return start
            start += 1
        return start
```

Solution 2
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) -1
```
