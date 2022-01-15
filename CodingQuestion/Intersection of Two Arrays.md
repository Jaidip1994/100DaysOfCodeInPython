Problem Description: https://leetcode.com/problems/intersection-of-two-arrays/

![image](https://user-images.githubusercontent.com/11685096/149612223-7e6019ea-9293-42e1-bd45-f8ace7946351.png)

Solution1
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
```

Solution2
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        final_arr = set()
        for elem in nums1:
            if elem in nums2:
                final_arr.add(elem)
        return list(final_arr)
```

Solution3
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(res) and nums1[i] == res[len(res)-1]):
                    res.append(nums1[i])
                i += 1
                j += 1

        return res
```
