[Problem Link](https://leetcode.com/problems/maximum-subarray/)
![image](https://user-images.githubusercontent.com/11685096/148693210-c8e83fab-90cc-4b71-9173-9837a8c8e301.png)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_sum = max_sum = nums[0]
        for elem in nums[1:]:
            cur_sum = max(elem, cur_sum + elem)
            max_sum = max(max_sum, cur_sum)
        return max_sum
        
```
