# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""
1 = [0]
2 = [-1, 1]
3 = [-1, 0, 1]
4 = [-2, -1, 1, 2]

1) Check if n is even or odd, 
    - If odd, we need to add a [0]
2) Append + and - starting from 1 to n // 2
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        L, rem = n // 2, n % 2
        if rem != 0: ans = [0]
        else: ans = []
        for i in range(1,L+1):
            ans.append(-i)
            ans.append(i) 
        return ans