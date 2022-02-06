Problem Description: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
![image](https://user-images.githubusercontent.com/11685096/152670189-04eaf177-2fa9-4ffe-8d5d-91bf02eedd80.png)

Solution
```python
from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        freq_count = Counter(nums)
        while True:
            if freq_count[nums[cur]] <= 2:
                cur += freq_count.pop(nums[cur])
            else:
                balance = freq_count.pop(nums[cur]) - 2
                cur += 2
                nums[cur:] = nums[cur+balance:]
            if not freq_count:
                break
        return cur
```
