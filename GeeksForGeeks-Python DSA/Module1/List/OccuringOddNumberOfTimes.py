ip = [10, 30, 30, 10, 30, 30, 20]
# o/p 20
ip = [20,10, 10, 10, 10, 10, 20]

# Solution 1 : Using a Frequency count operation
freq_count = dict()
for elem in ip:
    if elem in freq_count:
        freq_count.pop(elem, None)
    else:
        freq_count[elem] = 1

print(list(freq_count.keys())[0])

# Solution2 : Using XOR operator [Efficient Solution] 
# x ^ 0 = x & x ^ x = 0
# x ^ y ^ x = y

res = 0
for elem in ip:
    res ^= elem
print(res)