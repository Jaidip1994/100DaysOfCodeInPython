# Problem Description : https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tj = [0] * (n+1)
        for a,b in trust:
            tj[a] -= 1
            tj[b] += 1
        for i in range(1, n+1):
            if tj[i] == n-1:
                return i
        return -1 
