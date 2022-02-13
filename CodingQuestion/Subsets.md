Problem Description: https://leetcode.com/problems/subsets/
![image](https://user-images.githubusercontent.com/11685096/153741015-f5de70f5-c4fa-4c33-b733-60164525d1f1.png)

Solution 1
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_arr = [[]]
        for i in range(1, 2**(len(nums))):
            bin_list = list(bin(i)[2:])
            if len(bin_list) < len(nums):
                bin_list = ['0']*(len(nums) - len(bin_list)) + bin_list
            # print(bin_list)
            temp_list = []
            for i in range(len(bin_list)):
                if bin_list[i] == '1':
                    temp_list.append(nums[i])
            final_arr.append(temp_list)
            # print(final_arr)
        return final_arr 
```

Solution 2 via Cascading
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        op = [[]]
        for num in nums:
            op += [cur + [num] for cur in op] 
            print(op)
        return op
```
