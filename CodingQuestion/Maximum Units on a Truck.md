Problem Description: https://leetcode.com/problems/maximum-units-on-a-truck/

<img width="713" alt="image" src="https://user-images.githubusercontent.com/11685096/176986731-f5f41676-3ac5-4b3c-932b-a754cfef4447.png">

Solution
```python
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes = sorted(boxTypes, key=lambda x:x[1],reverse=True)
        maxCount = 0
        for even in boxTypes:
            if truckSize > even[0]:
                maxCount += even[0] * even[1]
                truckSize -= even[0]
            else:
                maxCount += truckSize * even[1]
                break
        return maxCount
```
