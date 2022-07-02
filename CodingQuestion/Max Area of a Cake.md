Problem Description: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

Solution
```python
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts=[0]+horizontalCuts+[h]; verticalCuts=[0]+verticalCuts+[w]
        horizontalCuts.sort(); verticalCuts.sort()

        difhor=[horizontalCuts[i+1]-horizontalCuts[i]  for i in range(len(horizontalCuts)-1)]
        difver=[verticalCuts[i+1]-verticalCuts[i]  for i in range(len(verticalCuts)-1)]
        return max(difhor)*max(difver)%(10**9+7)
        
        
 ```
