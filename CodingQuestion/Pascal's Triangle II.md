Problem Description: https://leetcode.com/problems/pascals-triangle-ii/
![image](https://user-images.githubusercontent.com/11685096/152653998-a2044131-a49e-42c0-8434-c4bffdd95ffb.png)

Solution
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        final_arr = [1,1]
        if rowIndex == 0:
            final_arr = [1]
        elif rowIndex == 1:
            final_arr = [1, 1]
        else:
            for i in range(rowIndex - 1):
                temp_arr = []
                for i in range(1, len(final_arr)):
                    temp_arr.append(final_arr[i-1] + final_arr[i])
                final_arr = [1] + temp_arr + [1]
        return final_arr
```
