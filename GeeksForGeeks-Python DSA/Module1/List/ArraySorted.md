Problem Description:
![image](https://user-images.githubusercontent.com/11685096/150997666-d099ef85-5f0b-4c32-bf7a-480c4e25cc63.png)


```python
class Solution:
    def isSorted(self,arr,n):
        #code here
        if n <= 1:
            return 1
        result_asc = True
        result_desc = True
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                result_asc = False
                break
        for i in range(1, n):
            if arr[i] >= arr[i-1]:
                result_desc = False
                break
        return int(result_asc or result_desc)
```
