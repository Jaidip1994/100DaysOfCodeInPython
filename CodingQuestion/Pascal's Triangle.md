Problem description: https://leetcode.com/problems/pascals-triangle/
![image](https://user-images.githubusercontent.com/11685096/152653255-cdbc4252-9bac-44e3-8cb2-b1119f704c1d.png)

Solution
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            if i == 0:
                arr.append([1])
                continue
            temp_arr = []
            if i > 1:
                for i in range(1, len(arr[-1])):
                    temp_arr.append(arr[-1][i]+arr[-1][i-1])
            if not temp_arr:
                arr.append([1, 1])
            else:
                arr.append([1]+temp_arr+[1])
        return arr
```
