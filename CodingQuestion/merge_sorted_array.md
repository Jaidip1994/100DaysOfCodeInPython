Problem Description: https://leetcode.com/problems/merge-sorted-array/

![image](https://user-images.githubusercontent.com/11685096/148828370-659ebf06-6d72-4471-bdaf-4dd3eea73cbe.png)

Solution
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m > 0 and n == 0:
            return 
        if m == 0 and n > 0:
            nums1[:] = nums2[:]
            return
        cnt1 = cnt2 = 0
        for idx in range(len(nums1)):
            if nums1[idx] > nums2[cnt2]:
                nums1[idx], nums1[idx+1:] = nums2[cnt2], nums1[idx:-1]
                cnt2 += 1
            else:
                cnt1 += 1
            if cnt1 == m and cnt2 != n:
                nums1[idx+1:] = nums2[cnt2:]
                break
            if cnt2 == n:
                break    
```
