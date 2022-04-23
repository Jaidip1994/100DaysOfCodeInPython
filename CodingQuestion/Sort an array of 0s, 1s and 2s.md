Problem Description: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1#
![image](https://user-images.githubusercontent.com/11685096/158416283-12b3d29b-e64c-4fc1-8527-fa4d32aa85e5.png)

Solution 1
```python
#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        cnt_dict = dict()
        for elem in arr:
            cnt_dict[elem] = 1 if not cnt_dict.get(elem, None) else cnt_dict[elem] + 1
        arr[:] = []
        for key, values in cnt_dict.items():
            arr += [key]*values
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
```

Solution 2
Optimized
```pyhon
def sort012(self,arr,n):
        # code here
        low = mid = 0
        high = n -1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 2:
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1
            else:
                mid += 1
        return arr
```
