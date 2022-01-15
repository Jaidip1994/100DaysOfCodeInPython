Problem description: https://leetcode.com/problems/intersection-of-two-arrays-ii/

![image](https://user-images.githubusercontent.com/11685096/149613117-808e4976-58be-4aa8-b8c8-06935fd812ad.png)

Solution
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        count1 = count2 = 0
        while (count1 < len(nums1) and count2 < len(nums2)):
            if nums1[count1] < nums2[count2]:
                count1 += 1
            elif nums1[count1] > nums2[count2]:
                count2 += 1
            else:
                res.append(nums1[count1])
                count1 += 1
                count2 += 1
        return res
```
