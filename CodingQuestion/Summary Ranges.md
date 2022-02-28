Problem Description: https://leetcode.com/problems/summary-ranges/
![image](https://user-images.githubusercontent.com/11685096/155983243-72a9aef8-44cd-4069-b46d-ed8c990e84a6.png)

Solution
```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        start = []
        final_arr = []
        for i in nums:
            if not start:
                start = [i,i]
                continue
            if i - 1 == start[-1]:
                start[-1] = i
            else:
                final_arr.append(f'{start[0]}->{start[1]}' if start[0] != start[1] else f'{start[0]}')
                start = [i,i]
        else:
            if start:
                final_arr.append(f'{start[0]}->{start[1]}' if start[0] != start[1] else f'{start[0]}')
        return final_arr
```
