Problem Description: https://www.hackerrank.com/challenges/2d-array/problem

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def fetch_row_sum(arr):
    max_sum = -9999
    for i in range(len(arr[0])-2):
        max_sum = max(max_sum, sum(arr[0][i:i+3])+ arr[1][i+1]+ sum(arr[2][i:i+3]))
    return max_sum
def hourglassSum(arr):
    # Write your code here
    sum_arr = -9999
    for i in range(len(arr)-2):
        # print(arr[i:i+3])
        sum_arr = max(sum_arr, fetch_row_sum(arr[i:i+3]))
    return sum_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
```
