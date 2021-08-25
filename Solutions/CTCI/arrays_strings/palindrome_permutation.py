# https://leetcode.com/problems/palindrome-permutation/

# Hash counter Approach
# O(n) time | O(n) space
class Solution(object):
    def canPermutePalindrome(self, s):
        counter = {}
        odd_count = 0
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else: 
                counter[char] += 1
        
        for val in counter.values():
            # increment odd_count if val is odd
            if val % 2 == 1:
                odd_count += 1
            # Permutated palindromes only allow for one odd 
            if odd_count > 1:
                return False
        
        return True

# Set Approach
# O(n) time | O(1) space because a set can grow up to a maximum number
#                  of all distinct elements. However, the number of 
#                  distinct characters are bounded, so as the space complexity.
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        unpaired_chars = set()
        
        for char in s:
            if char not in unpaired_chars:
                unpaired_chars.add(char)
            else:
                unpaired_chars.remove(char)
                
        return len(unpaired_chars) <= 1