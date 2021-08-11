# https://binarysearch.com/problems/Hamming-Distance

# O(n) time | O(1) space
class Solution:
    def solve(self, x, y):
        x = x ^ y
        count = 0
        while x:
            count += 1
            x = x & (x - 1)
        return count