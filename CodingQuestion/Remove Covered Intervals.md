Problem Description: https://leetcode.com/problems/remove-covered-intervals/
![image](https://user-images.githubusercontent.com/11685096/154831439-8e8b0bbf-1f3c-4f40-91f7-ccf90ad7721b.png)

```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        len_ar = len(intervals)
        cnt = 1
        while cnt < len_ar:
            # print(intervals)
            if intervals[cnt][1]<=intervals[cnt-1][1]:
                len_ar -= 1
                intervals.pop(cnt)
                continue
            if intervals[cnt-1][0]==intervals[cnt][0] and intervals[cnt-1][1] < intervals[cnt][1]:
                len_ar -= 1
                intervals.pop(cnt-1)
                continue
            cnt += 1
        return len_ar
```
