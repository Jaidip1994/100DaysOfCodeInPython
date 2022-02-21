Problem Description: https://leetcode.com/problems/majority-element/
![image](https://user-images.githubusercontent.com/11685096/154896540-ee5b1b03-4f50-4f93-9af6-ac2bea90f8b6.png)

Solution1
```python
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_cnt = Counter(nums)
        return max(freq_cnt.keys(), key=freq_cnt.get)
```

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
```
