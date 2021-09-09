# https://leetcode.com/problems/first-unique-character-in-a-string/

# O(n) time | O(1) --> O(26) cuz of 26 char in alphabet 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        # to count occurrences
        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
                
        for i, char in enumerate(s):
            if seen[char] == 1:
                return i
        return -1