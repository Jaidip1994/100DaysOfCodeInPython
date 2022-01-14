Prolem Description:https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
![image](https://user-images.githubusercontent.com/11685096/149459236-5219392c-5885-4e08-b222-8cfcae4971fa.png)

Solution
```python
def staircase(n):
    # Write your code here
    for i in range(n):
        str = ''
        for j in range(n-i-1):
            str += ' '
        for k in range(i+1):
            str += '#'
        print(str)
```
