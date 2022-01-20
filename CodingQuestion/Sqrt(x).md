Problem Description: https://leetcode.com/problems/sqrtx/
![image](https://user-images.githubusercontent.com/11685096/150356285-770648d7-fc58-4110-ab3a-6a68a73c1989.png)

Solution
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        
        # base case
        if x==0 or x ==1:
            return x
        start = 1
        end = x
        while start <= end:
            mid = (start + end)//2
            if (mid*mid == x):
                return mid
            
            if mid * mid < x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans
```
