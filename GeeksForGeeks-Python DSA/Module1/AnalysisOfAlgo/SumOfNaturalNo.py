# Sum of n natural numbers
# example
# i/p = 3
# o/p = 6

# i/p = 5
# o/p = 15

i = int(input('Enter the number: '))
sum_op = 0
for i in range(1, i+1):
    sum_op += i
print(f'Sum of n natural numbers is : {sum_op}')