# Problem description: https://leetcode.com/problems/complement-of-base-10-integer/

# Solution 1

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_rpr = bin(n)
        num = 0
        final = 0
        for elem in bin_rpr[::-1]:
            if elem == '0':
                final += 2 ** num
            if elem == 'b':
                return final
            num += 1
            
            
# Solution 2
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        base_of_num = len(bin(N).replace("0b",""))
        return 2**base_of_num + ~(N)
