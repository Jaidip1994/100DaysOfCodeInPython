Problem Description: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

```python
def plusMinus(arr):
    # Write your code here
    count = [0,0,0]
    for elem in arr:
        if elem > 0:
           count[0] += 1
        elif elem < 0:
            count[1] += 1
        else:
            count[-1] += 1
    for elem in count:
        # print(round(elem/len(arr), 6)) 
        print(f"{elem/len(arr):,{'.6f'}}")
```
