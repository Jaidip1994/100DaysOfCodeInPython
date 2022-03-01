Problem Description: https://leetcode.com/problems/counting-bits/
![image](https://user-images.githubusercontent.com/11685096/156109222-1b052066-9cf1-49e9-bc5b-d631598ad0f4.png)

Soltion 1
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            while i:
                if i & 1 == 1:
                    count += 1
                i >>= 1
            res.append(count)
        return res
```

Solution 2
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(bin(i)[2:].count('1'))
        return res
```


Solution 3

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        return map(lambda i: bin(i).count('1'), range(n+1))
```
