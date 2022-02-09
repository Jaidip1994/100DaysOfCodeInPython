Problem Description: https://leetcode.com/problems/k-diff-pairs-in-an-array/
![image](https://user-images.githubusercontent.com/11685096/153255867-2cf9a78e-4a88-4584-bd0e-34fa1b54991e.png)

Solution1

```python
class Solution:
  def binary_search(self, arr,low,high,x):
    if (high >= low):
      mid = low + (high - low) // 2
      if x == arr[mid]:
        return mid
      elif( x > arr[mid]):
        return self.binary_search(arr, (mid+1), high, x)
      else:
        return self.binary_search(arr, low, (mid-1), x)
      
    return -1
    
  def findPairs(self, nums: List[int], k: int) -> int:
      nums.sort()
      count = 0
      n = len(nums)
      arr = []
      
      for i in range(0, n):
        index = self.binary_search(nums, i+1, n-1, nums[i]+k)
        if( index != -1 and [nums[i], nums[index]] not in arr):
          arr.append([nums[i], nums[index]])
          count += 1
      return count
```

Solution 2

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        var_cnt = Counter(nums)
        if k == 0:
            for key, val in var_cnt.items():
                if val > 1:
                    cnt += 1
        else:
            for key, val in var_cnt.items():
                if key + k in var_cnt:
                    cnt += 1
        return cnt
```
