# This approach takes O(n) time complexity and O(1) auxiliary space
# Using three rotations the list will be shifted by d positions
# ex for i/p [10,20,30,40,50]
# After 1 st rotation
# [30,20,10, 40 ,50]
# After 2nd rotation
# [30,20,10, 50 ,40]
# After 3rd rotation
# [ 40 ,50, 10, 20, 30]

def reverse(l,b,e):
    while b<e:
        l[b],l[e]=l[e],l[b]
        b=b+1
        e=e-1


def leftRotate(l,d):
    n=len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)


l=[10,20,30,40,50]
d=3
leftRotate(l, d)
print(l)