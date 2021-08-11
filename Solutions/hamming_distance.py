# https://binarysearch.com/problems/Hamming-Distance

# Takeaway: I need to practice more bit manipulation :(

# O(n) time | O(1) space
class Solution_1:
    def solve(self, x, y):
        n = x ^ y
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count

# O(log n) | O(1) space
class Solution_2:
    def solve(self, x, y):
        return bin(x ^ y).count("1")