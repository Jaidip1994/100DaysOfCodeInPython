Problem Description: https://leetcode.com/problems/maximize-distance-to-closest-person/

![image](https://user-images.githubusercontent.com/11685096/149651395-87aa3671-a345-44e6-96ec-327e2ae3bce2.png)
![image](https://user-images.githubusercontent.com/11685096/149651400-8f891754-3be7-41f7-846d-e13f36c355db.png)
![image](https://user-images.githubusercontent.com/11685096/149651406-963b5b64-90c8-4771-aebf-ca5405d1cb4a.png)

Solution 1
```python
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start = None
        max_dist = -9999
        start_end_dict = []
        for index, seat in enumerate(seats):
            if seat == 1:
                if index != 0 and len(start_end_dict) == 0:
                    max_dist = (index - 0)
                    start_end_dict = [0, index]
                elif start is None and not index:
                    start = index
                elif (index - start) > max_dist:
                    if seats[start_end_dict[1]] != seats[start_end_dict[0]] and (index - start)//2 > max_dist:
                        max_dist = (index - start)
                        start_end_dict = [start, index]
                    elif seats[start_end_dict[1]] == seats[start_end_dict[0]]:
                        max_dist = (index - start)
                        start_end_dict = [start, index]
                start = index
            
        if seats[-1] == 0 and start_end_dict:
            if seats[start_end_dict[1]] == seats[start_end_dict[0]] and (start_end_dict[1] - start_end_dict[0])//2 < (len(seats)-1 - start):
                start_end_dict = start, len(seats)-1
            elif (start_end_dict[1] - start_end_dict[0]) < (len(seats)-1 - start):
                start_end_dict = start, len(seats)-1
        if not start_end_dict:
            if start is not None:
                return max(start - 0, len(seats)-1-start )
        elif seats[start_end_dict[1]] != seats[start_end_dict[0]]:
            return start_end_dict[1] - start_end_dict[0]
        else:
            return (start_end_dict[1] - start_end_dict[0])//2
```

Solution2: Explanation [here](https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/1693404/C%2B%2BJavaPython-One-Pass-O(N)-oror-Count-Zeros-oror-Image-Explained)
```python
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        pre_zeros, suf_zeros, max_zeros, zeros = -1, -1, -1, 0
        for seat in seats:
            if seat == 0: zeros += 1
            else:
                if pre_zeros == -1: 
                    pre_zeros = zeros
                else:
                    max_zeros = max(max_zeros, zeros)
                zeros = 0
        suf_zeros = zeros
        return max(pre_zeros, suf_zeros, (max_zeros + 1) // 2)
```
