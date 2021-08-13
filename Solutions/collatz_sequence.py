# https://binarysearch.com/problems/Collatz-Sequence

# IDK the time :( | O(1) space
class Solution:
    def solve(self, n):
        count = 1
        
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                count += 1
            elif n % 2 == 1:
                n = n * 3 + 1
                count += 1

        return count