# https://binarysearch.com/problems/Unique-Ab-Strings

# Takeaway: Every occurance of "a" in the given string double the # of unique strings possible

# First Solution
# O(n) time | O(1) space
class Solution_1:
    def solve(self, s):
        result = 1
        for char in s:
            if char == "a":
                result = result * 2

        return result

# Second Solution 
# O(n) time | O(1) space
class Solution_2:
    def solve(self, s):
        # count() returns # of occurrences of substring
        count = s.count("a") 
        # ans is 2 ^ of occurences of "a" in given string
        return 2 ** count