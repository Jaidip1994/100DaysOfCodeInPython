Problem Description: https://leetcode.com/problems/can-place-flowers/
![image](https://user-images.githubusercontent.com/11685096/149970824-bddcd2fd-2443-4c3c-a9cd-5f73ad2b4963.png)

Solution
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        free_spots = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                free_spots += 1
            if free_spots >= n:
                return True
        return False
```
