# Sum of n natural numbers
# example
# i/p = 3
# o/p = 6

# i/p = 5
# o/p = 15

i = int(input('Enter the number: '))

def sol1(i):
    sum_op = 0
    for i in range(1, i+1):
        sum_op += i
    return sum_op


sum_op = sol1(i)
print(f'Sol 1 Sum of n natural numbers is : {sum_op}')


def sol2(i):
    return int((i*(i+1))/2)

sum_op = sol2(i)
print(f'Sol 2 Sum of n natural numbers is : {sum_op}')